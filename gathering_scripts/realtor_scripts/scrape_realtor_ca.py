import requests

from gathering_scripts.realtor_enums.RealtorEnums import RealtorEnums
from gathering_scripts.rent_helpers.GeoHelper import GeoHelper
from gathering_scripts.db.DBConnector import DBConnector


items = []


def scrape(current_page):
    print(current_page)
    data = RealtorEnums.REALTOR_CA_DATA.value
    data["CurrentPage"] = str(current_page)

    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post',
                             headers=RealtorEnums.REALTOR_CA_HEADERS.value,
                             cookies=RealtorEnums.REALTOR_CA_COOKIES.value, data=data)
    total_pages = response.json().get('Paging').get("TotalPages")
    results = response.json().get("Results")
    for prop in results:
        d = prop.get("Property")
        rent = d.get("LeaseRent").replace("$", "").replace("/", "").replace(",", "").replace("Monthly", "")
        if "Seasonal" in rent:
            rent = int(int(rent.replace("Seasonal", "")) / 3)
        elif "Yearly" in rent:
            rent = int(int(rent.replace("Yearly", "")) / 12)
        lat = d.get("Address").get("Latitude")
        long = d.get("Address").get("Longitude")
        postal_code = prop.get("PostalCode")
        if postal_code is None or postal_code == "":
            geohelper = GeoHelper(lat, long)
            postal_code = geohelper.get_zip_outer()
            fsa = str(postal_code)[:3]
        else:
            fsa = postal_code[:3]

        item = {
            "latitude": str(float(lat)),
            "longitude": str(float(long)),
            "postal_code": str(postal_code),
            "fsa": str(fsa),
            "rent_price": int(rent),
        }
        items.append(item)

    if current_page <= total_pages:
        scrape(current_page + 1)
    return items


def run_scraping():
    data = scrape(1)
    db_conn = DBConnector()
    db_conn.save_distinct_to_db(data)


if __name__ == '__main__':
    run_scraping()
