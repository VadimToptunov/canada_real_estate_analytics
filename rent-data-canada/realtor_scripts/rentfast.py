import requests
import csv
import json
from datetime import date

from realtor_enums.RealtorEnums import RealtorEnums

total_data = []


def run_request(city):
    print(city)
    cookies = RealtorEnums.RENTFAST_COOKIES.value
    cookies['lastcity'] = city
    response = requests.post(RealtorEnums.RENTFAST_URL.value, headers=RealtorEnums.RENTFAST_HEADERS.value,
                             cookies=cookies,
                             data=RealtorEnums.RENTFAST_DATA.value)
    resp = response.json().get("listings")
    cityname = city[5:]
    get_circlemap_data(resp, cityname)
    write_to_file(resp, city)


def write_to_file(resp, city):
    ct_name = city.replace("%2F", "__")
    filename = f"{RealtorEnums.DATA_PATH.value}{ct_name}_data_{date.today()}.csv"
    with open(filename, 'a+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(("City", "Address", "Sq Feet", "Sq Feet2", "Latitude", "Longtitude", "Price"))
        for i in resp:
            try:
                sqfeet2 = i.get("sq_feet2")
            except:
                sqfeet2 = ""
            csv_writer.writerow((i.get("city"), i.get("intro"), i.get("sq_feet"), sqfeet2, i.get("latitude"),
                                 i.get("longitude"), i.get("price")))


def get_circlemap_data(resp, city):
    for i in resp:
        data = [i.get("latitude"), i.get("longitude")]
        if i.get("price") == '' or i.get("price") is None:
            price = 0
        else:
            price = int(i.get("price"))
        data.append(price)
        total_data.append(data)
    filename = f"r_data_{date.today()}.json"
    data_set = list(set(map(tuple, total_data)))
    with open(f"{RealtorEnums.CIRCLEMAP_DATASETS.value}{filename}", "w+") as file:
        file.write(json.dumps(data_set))


def scrape_rent_fast():
    list_of_cities = RealtorEnums.RENTFAST_CITIES.value

    for city in list_of_cities:
        run_request(city)


if __name__ == '__main__':
    scrape_rent_fast()
