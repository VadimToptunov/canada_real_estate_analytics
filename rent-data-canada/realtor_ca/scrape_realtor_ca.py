import requests
import json
from datetime import date


data_set = []

def scrape(current_page):
    print(current_page)
    cookies = {
    'visid_incap_2269415': '2gcQI9EkRCeULFsblGFTMBDHb2EAAAAAQUIPAAAAAABhJgyXar55MIqtKufSu+GP',
    'nlbi_2269415': 'wlXDVklPNw/Ai0wPkG5lugAAAABRHywEZnidIDW8FqSRKs4+',
    'incap_ses_1293_2269415': 'J7H8Ir/ZDy5h44XP6ajxERHHb2EAAAAAdR8+HLMCnRDiz/Awh+LQ4g==',
    'incap_ses_583_2269415': 'nK4Yc5ycPF7c+AksKDwXCBLHb2EAAAAAdOpicPWSZt5Tx7HEI++pig==',
    'nlbi_2269415_2147483646': '82XRGKe4LUqRnabGkG5lugAAAABaQH+/ZUC7rmNYXm5P3F94',
    'gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko': 'gigya-pr_ver4',
    'reese84': '3:wu8ed/31GzAMLo2U6PdBxw==:5/KIg0Pel8nyELMHRzbqcAaiefm2+Du2DdNz4tS4nMVKQ9+m03x1nrAJDKJAqBPEXovUnUhq2kgC7G9fSjfCrwBvVi9uDdBL7GbsbTXmDS/xnbm8kXwfzUfxMXP7nbiPX4eh2z18HbT9Eh1FIx1BizAWUfGWCbNLRgKuB3oec5njzQgAlqcgMK9sZalFJW7TomIioT5xZwrgxsToS1Vaf33YNy3y0Ypo4nQaoSqQDTO7irMt1txt5JRxuFTsJQuGrvXhju87/ny1/A/XLjqH6mP5/riZD8wrSiG7MP4H2aQO3FMKaLMd25fdTMbBmr9juKIIw7TaNO3o9rGa28KqPmTMu2QCIqyXVvflIB97FtoBYk9ou8/jcLXR1S9YsvQhD06BNMKTjiRzaZ75EsOkN6pmHFer+9G+UmiwzYTp5OwoBwTA0jsbZETPum8SKocS:Fy+9gBL7WsyjzNqgyM2sZ2+HQcBbmKFdhoywb1YQvnI=',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.realtor.ca',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Referer': 'https://www.realtor.ca/',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        }

    data = {
    'ZoomLevel': '4',
    'LatitudeMax': '64.14416',
    'LongitudeMax': '-32.65137',
    'LatitudeMin': '42.96446',
    'LongitudeMin': '-165.98145',
    'Sort': '6-D',
    'PropertyTypeGroupID': '1',
    'PropertySearchTypeId': '1',
    'TransactionTypeId': '3',
    'BedRange': '1-1',
    'BathRange': '1-0',
    'BuildingTypeId': '17',
    'Currency': 'CAD',
    'RecordsPerPage': '100',
    'ApplicationId': '1',
    'CultureId': '1',
    'Version': '7.0',
    'CurrentPage': '1'
    }

    data["CurrentPage"] = str(current_page)

    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, cookies=cookies, data=data)
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
        # print(lat, long, rent)
        item.append(float(lat))
        item.append(float(long))
        item.append(int(rent))
        data_set.append(item)
    
    if current_page <= total_pages:
        scrape(current_page + 1)
    with open(f"rent-data-canada/rent_fast/circlemap_datasets/realtor-ca_data_{date.today()}.json", "w+") as file:
        file.write(json.dumps(data_set))

def run_scraping():
    scrape(1)

if __name__ == '__main__':
    run_scraping()    
