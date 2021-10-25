import requests
import csv
import json
from datetime import date

basic_path = "rent-data-canada/rent_fast/"
total_data = []

def run_request(city):
    print(city)
    cookies = {
    'PHPSESSID': '8f1e54939c157e084f99d585ef438ff5',
    'lastcity': city,
    'lastcommunity': 'apartment',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.rentfaster.ca/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.rentfaster.ca',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
    'beds': '1,1 + Den',
    'baths': '1',
    'smoking': 'Non-Smoking',
    'lease_term': 'Long Term',
    'type[]': 'Apartment',
    'exclude': ''
    }

    response = requests.post('https://www.rentfaster.ca/api/map.json', headers=headers, cookies=cookies, data=data)
    resp = response.json().get("listings")
    cityname = city[5:]
    get_heatmap_data(resp, cityname)
    write_to_file(resp, city)


def write_to_file(resp, city):
    ct_name = city.replace("%2F","__")
    filename = f"{basic_path}full_appartments_data/{ct_name}_data_{date.today()}.csv"
    with open(filename, 'a+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(("City", "Address", "Sq Feet", "Sq Feet2", "Latitude", "Longtitude", "Price"))
        for i in resp:
            try:
                sqfeet2 = i.get("sq_feet2")
            except:
                sqfeet2 = ""
            csv_writer.writerow((i.get("city"), i.get("intro"), i.get("sq_feet"), sqfeet2, i.get("latitude"), i.get("longitude"), i.get("price")))

def get_heatmap_data(resp, city):
    for i in resp:
        data = []
        data.append(i.get("latitude"))
        data.append(i.get("longitude"))
        if i.get("price") == '' or i.get("price") == None:
            price = 0
        else:
            price = int(i.get("price"))
        data.append(price)
        total_data.append(data)

    # ct_name = city.replace("%2F","__")
    filename = f"r_data_{date.today()}.json"
    data_set = list(set(map(tuple, total_data)))
    with open(f"{basic_path}circlemap_datasets/{filename}", "w+") as file:
        file.write(json.dumps(data_set))


def scrape_rent_fast():
    list_of_cities=[
        "ab%2Fcalgary",
        "ab%2Fedmonton",
        "ab%2Fred-deer",
        "bc%2Fvancouver",
        "bc%2Fsurrey", 
        "bc%2Fburnaby", 
        "bc%2Frichmond",
        "bc%2Fabbotsford", 
        "bc%2Fcoquitlam",
        "bc%2Fkelowna",
        "mb%2Fwinnipeg",
        "on%2Ftoronto",
        "on%2Fottawa",
        "on%2Fmississauga",
        "on%2Fbrampton",
        "on%2Fhamilton",
        "on%2Flondon",
        "on%2Fmarkham",
        "on%2Fvaughan",
        "on%2Fkitchener",
        "on%2Fwindsor",
        "on%2Frichmond-hill",
        "qc%2Fmontreal",
    ]

    for city in list_of_cities:
        run_request(city)


if __name__ == '__main__':
    scrape_rent_fast()