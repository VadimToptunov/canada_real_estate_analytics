import asyncio
import json
import urllib.parse
from pyppeteer import launch

from gathering_scripts.realtor_enums.RealtorEnums import RealtorEnums
from gathering_scripts.rent_helpers.GeoHelper import GeoHelper
from gathering_scripts.db.DBConnector import DBConnector

data = []


async def run(input_list):
    browser = await launch({"headless": False, "args": ["--start-maximized"]})
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(50000)
    pagination = 0
    for item in input_list:
        pagination = item[0]
        await scrape(page, pagination, item[1], item[2], item[3])
    await browser.close()


async def scrape(page, pagination, province, map_bounds, region_selection):
    print(pagination, province)
    req_d = {"pagination": pagination, "usersSearchTerm": province, "mapBounds": map_bounds, "mapZoom": 4,
             "regionSelection": region_selection, "isMapVisible": True,
             "filterState": {"beds": {"min": 1}, "baths": {"min": 1}, "isForSaleForeclosure": {"value": False},
                             "isAllHomes": {"value": True}, "isAuction": {"value": False},
                             "isNewConstruction": {"value": False}, "isForRent": {"value": True},
                             "isSingleFamily": {"value": False}, "isTownhouse": {"value": False},
                             "isForSaleByOwner": {"value": False}, "isComingSoon": {"value": False},
                             "isForSaleByAgent": {"value": False}}, "isListVisible": True}

    str_to_encode = {"searchQueryState": req_d, 'wants': {"cat1": ["mapResults"]}, "requestId": 2}

    link = RealtorEnums.ZILLOW_BASE_LINK.value + urllib.parse.urlencode(str_to_encode) + '&wants={"cat1":[' \
                                                                                         '"mapResults"]}"&requestId=36 '
    await page.setViewport({"width": 1600, "height": 900})
    await page.goto(link)
    apptdata = await page.querySelector("body pre")
    resp = await (await apptdata.getProperty('textContent')).jsonValue()
    res = json.loads(resp)
    results = res.get("cat1")
    total_pages = results.get("searchList").get("totalPages")
    search_results = results.get("searchResults").get("mapResults")
    for i in search_results:
        try:
            appt_id = i.get("zpid")
        except Exception:
            appt_id = i.get("buildingId")
        lat = i.get("latLong").get("latitude")
        long = i.get("latLong").get("longitude")
        try:
            zip_code = i.get("hdpData").get("homeInfo").get("zipcode")
            fsa = zip_code[:3]
        except Exception:
            geohelper = GeoHelper(lat, long)
            zip_code = geohelper.get_zip_outer()
            try:
                fsa = zip_code[:3]
            except TypeError:
                fsa = None

        price = int(
            str(i.get('price')).replace("/mo", "").replace("C$", "").replace("$", "").replace("+", "").replace(",", ""))
        item = {
            "_id": appt_id,
            "latlong": str(float(lat)) + str(float(long)),
            "latitude": str(float(lat)),
            "longitude": str(float(long)),
            "postal_code": str(zip_code),
            "fsa": fsa,
            "rent_price": int(price),
        }
        data.append(item)

    pug = pagination["currentPage"] + 1
    if pug <= total_pages:
        pagination["currentPage"] = pug
        await scrape(page, pagination, province, map_bounds, region_selection)
    db_conn = DBConnector()
    db_conn.save_distinct_to_db(data)


async def run_zillow_scraping():
    await run(RealtorEnums.ZILLOW_INPUTLIST.value)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_zillow_scraping())
