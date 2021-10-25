from datetime import date
import json
import time
import random
import urllib.parse
from seleniumwire import webdriver
from bs4 import BeautifulSoup

data = []

def run(input_list):
    for i in input_list:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '
                                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 '
                                    'Edge/12.10166"')
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)
        scrape(driver, i[0], i[1], i[2], i[3])
    data_set = list(set(map(tuple, data)))
    with open(f"rent-data-canada/rent_fast/circlemap_datasets/dump_{date.today()}.json", "a+") as f:
        f.write(json.dumps(data_set))
    time.sleep(random.randint(10, 26))
    driver.close()
    driver.quit()


def scrape(driver, pagination, province, map_bounds, region_selection):
    print(pagination, province)
    base_link = "https://www.zillow.com/search/GetSearchPageState.htm?"
    req_d = {"pagination":{},"usersSearchTerm":"NS","mapBounds":{"west":-111.28655262500001,"east":-14.782646374999985,"south":42.62267051385993,"north":47.93550872885281},"mapZoom":4,"regionSelection":[{"regionId":404371,"regionType":2}],"isMapVisible":True,"filterState":{"beds":{"min":1},"baths":{"min":1},"isForSaleForeclosure":{"value":False},"isAllHomes":{"value":True},"isAuction":{"value":False},"isNewConstruction":{"value":False},"isForRent":{"value":True},"isSingleFamily":{"value":False},"isTownhouse":{"value":False},"isForSaleByOwner":{"value":False},"isComingSoon":{"value":False},"isForSaleByAgent":{"value":False}},"isListVisible":True}
    req_d["pagination"] = pagination
    req_d["usersSearchTerm"] = province
    req_d["mapBounds"] = map_bounds
    req_d["regionSelection"] = region_selection
        
    str_to_encode = {"searchQueryState":req_d, 'wants':{"cat1":["mapResults"]},"requestId":2}

    link = base_link + urllib.parse.urlencode(str_to_encode) + '&wants={"cat1":["mapResults"]}"&requestId=36'
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
        item = []
        lat = i.get("latLong").get("latitude")
        long = i.get("latLong").get("longitude")
        price = int(str(i.get('price')).replace("/mo", "").replace("C$", "").replace("$", "").replace("+", "").replace(",", ""))
        item.append(lat)
        item.append(long)
        item.append(price)
        data.append(item)
        
    pug = pagination["currentPage"] + 1
    if pug <= total_pages:
        pagination["currentPage"] = pug
        scrape(driver, pagination, province, map_bounds, region_selection)

def run_zillow_scraping():
    input_list = [
        [{"currentPage":1}, "AB", {"west":-163.253122125,"east":-66.749215875,"south":46.61367884585051,"north":61.72767648346558}, [{"regionId":404364,"regionType":2}]],
        [{"currentPage":1}, "BC", {"west":-174.803827625,"east":-78.299921375,"south":46.25476397586688,"north":61.48001177218533}, [{"regionId":404365,"regionType":2}]],
        [{"currentPage":1}, "ON", {"west":-133.00111312500002,"east":-36.49720687499999,"south":40.67528087446994,"north":57.58277224736895},[{"regionId":404375,"regionType":2}]],
        [{"currentPage":1}, "MB", {"west":-143.745199625,"east":-47.24129337499999,"south":46.61526044757908,"north":61.72876707649884}, [{"regionId":404366,"regionType":2}]],
        [{"currentPage":1}, "NS", {"west":-75.09758778125,"east":-50.97161121874999,"south":42.233426826928486,"north":48.287604943570564}, [{"regionId":404371,"regionType":2}]]
    ]
    run(input_list)
    

if __name__ == "__main__":
    run_zillow_scraping()
        