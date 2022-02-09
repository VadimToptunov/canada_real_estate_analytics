import json
import random
import time
import urllib.parse
from bs4 import BeautifulSoup
from seleniumwire import webdriver

from realtor_enums.RealtorEnums import RealtorEnums
from rent_helpers.GeoHelper import GeoHelper
from db.DBConnector import DBConnector

data = []


def run(input_list):
    for i in input_list:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument(
            '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 '
            'Edge/12.10166"')
        driver = webdriver.Chrome(RealtorEnums.CHROME_PATH.value, chrome_options=options)
        scrape(driver, i[0], i[1], i[2], i[3])
    time.sleep(random.randint(10, 26))
    driver.close()
    driver.quit()


def scrape(driver, pagination, province, map_bounds, region_selection):
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
    driver.get(link)
    time.sleep(random.randint(3, 38))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    heading = soup.select_one("body pre").text
    resp = json.loads(heading)
    results = resp.get("cat1")
    total_pages = results.get("searchList").get("totalPages")
    search_results = results.get("searchResults").get("mapResults")
    for i in search_results:
        lat = i.get("latLong").get("latitude")
        long = i.get("latLong").get("longitude")
        try:
            zip_code = i.get("hdpData").get("homeInfo").get("zipcode")
            fsa = zip_code[:3]
        except Exception:
            geohelper = GeoHelper(lat, long)
            zip_code = geohelper.get_zip_outer()
            fsa = zip_code[:3]
        price = int(
            str(i.get('price')).replace("/mo", "").replace("C$", "").replace("$", "").replace("+", "").replace(",", ""))
        item = {
            "latitude": float(lat),
            "longitude": float(long),
            "postal_code": str(zip_code),
            "fsa": fsa,
            "rent_price": int(price),
        }
        data.append(item)

    pug = pagination["currentPage"] + 1
    if pug <= total_pages:
        pagination["currentPage"] = pug
        scrape(driver, pagination, province, map_bounds, region_selection)
    db_conn = DBConnector("database/apptdata.db")
    db_conn.add_data_to_db(data)


def run_zillow_scraping():
    run(RealtorEnums.ZILLOW_INPUTLIST.value)


if __name__ == "__main__":
    run_zillow_scraping()
