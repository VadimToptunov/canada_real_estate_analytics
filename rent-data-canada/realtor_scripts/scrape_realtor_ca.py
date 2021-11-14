import requests
import json
from datetime import date
from realtor_enums.RealtorEnums import RealtorEnums


data_set = []


def scrape(current_page):
    print(current_page)
    data = RealtorEnums.REALTOR_CA_DATA.value
    data["CurrentPage"] = str(current_page)

    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=RealtorEnums.REALTOR_CA_HEADERS.value,
                             cookies=RealtorEnums.REALTOR_CA_COOKIES.value, data=data)
    total_pages = response.json().get('Paging').get("TotalPages")
    results = response.json().get("Results")
    for property in results:
        item = []
        d = property.get("Property")
        rent = d.get("LeaseRent").replace("$", "").replace("/", "").replace(",", "").replace("Monthly", "")
        if "Seasonal" in rent:
            rent = int(int(rent.replace("Seasonal", "")) / 3)
        lat = d.get("Address").get("Latitude")
        long = d.get("Address").get("Longitude")
        item.append(float(lat))
        item.append(float(long))
        item.append(int(rent))
        data_set.append(item)

    if current_page <= total_pages:
        scrape(current_page + 1)
    with open(f"{RealtorEnums.CIRCLEMAP_DATASETS.value}/realtor-ca_data_{date.today()}.json", "w+") as file:
        file.write(json.dumps(data_set))


def run_scraping():
    scrape(1)


if __name__ == '__main__':
    run_scraping()
