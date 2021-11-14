from enum import Enum


class RealtorEnums(Enum):
    CHROME_PATH = './drivers/chromedriver'
    CIRCLEMAP_DATASETS = "./circlemap_generator/circlemap_datasets/"
    DATA_PATH = "./data/"
    GENERATED_CIRCLEMAPS_PATH = './circlemaps/'
    REALTOR_CA_COOKIES = {
        'visid_incap_2269415': '2gcQI9EkRCeULFsblGFTMBDHb2EAAAAAQUIPAAAAAABhJgyXar55MIqtKufSu+GP',
        'nlbi_2269415': 'wlXDVklPNw/Ai0wPkG5lugAAAABRHywEZnidIDW8FqSRKs4+',
        'incap_ses_1293_2269415': 'J7H8Ir/ZDy5h44XP6ajxERHHb2EAAAAAdR8+HLMCnRDiz/Awh+LQ4g==',
        'incap_ses_583_2269415': 'nK4Yc5ycPF7c+AksKDwXCBLHb2EAAAAAdOpicPWSZt5Tx7HEI++pig==',
        'nlbi_2269415_2147483646': '82XRGKe4LUqRnabGkG5lugAAAABaQH+/ZUC7rmNYXm5P3F94',
        'gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko': 'gigya-pr_ver4',
        'reese84': '3:wu8ed/31GzAMLo2U6PdBxw==:5/KIg0Pel8nyELMHRzbqcAaiefm2+Du2DdNz4tS4nMVKQ9'
                   '+m03x1nrAJDKJAqBPEXovUnUhq2kgC7G9fSjfCrwBvVi9uDdBL7GbsbTXmDS'
                   '/xnbm8kXwfzUfxMXP7nbiPX4eh2z18HbT9Eh1FIx1BizAWUfGWCbNLRgKuB3oec5njzQgAlqcgMK9sZalFJW7TomIioT5xZwrgxsToS1Vaf33YNy3y0Ypo4nQaoSqQDTO7irMt1txt5JRxuFTsJQuGrvXhju87/ny1/A/XLjqH6mP5/riZD8wrSiG7MP4H2aQO3FMKaLMd25fdTMbBmr9juKIIw7TaNO3o9rGa28KqPmTMu2QCIqyXVvflIB97FtoBYk9ou8/jcLXR1S9YsvQhD06BNMKTjiRzaZ75EsOkN6pmHFer+9G+UmiwzYTp5OwoBwTA0jsbZETPum8SKocS:Fy+9gBL7WsyjzNqgyM2sZ2+HQcBbmKFdhoywb1YQvnI=',
    }
    REALTOR_CA_HEADERS = {
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
    REALTOR_CA_DATA = {'ZoomLevel': '4', 'LatitudeMax': '64.14416', 'LongitudeMax': '-32.65137',
                       'LatitudeMin': '42.96446',
                       'LongitudeMin': '-165.98145', 'Sort': '6-D', 'PropertyTypeGroupID': '1',
                       'PropertySearchTypeId': '1',
                       'TransactionTypeId': '3', 'BedRange': '1-1', 'BathRange': '1-0', 'BuildingTypeId': '17',
                       'Currency': 'CAD',
                       'RecordsPerPage': '100', 'ApplicationId': '1', 'CultureId': '1', 'Version': '7.0',
                       "CurrentPage": '1'}
    RENTFAST_COOKIES = {
        'PHPSESSID': '8f1e54939c157e084f99d585ef438ff5',
        'lastcity': 'Toronto',
        'lastcommunity': 'apartment',
    }
    RENTFAST_HEADERS = {
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
    RENTFAST_DATA = {
        'beds': '1,1 + Den',
        'baths': '1',
        'smoking': 'Non-Smoking',
        'lease_term': 'Long Term',
        'type[]': 'Apartment',
        'exclude': ''
    }
    RENTFAST_CITIES = [
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
    RENTFAST_URL = 'https://www.rentfaster.ca/api/map.json'
    ZILLOW_INPUTLIST = [
        [{"currentPage": 1}, "AB",
         {"west": -163.253122125, "east": -66.749215875, "south": 46.61367884585051, "north": 61.72767648346558},
         [{"regionId": 404364, "regionType": 2}]],
        [{"currentPage": 1}, "BC",
         {"west": -174.803827625, "east": -78.299921375, "south": 46.25476397586688, "north": 61.48001177218533},
         [{"regionId": 404365, "regionType": 2}]],
        [{"currentPage": 1}, "ON", {"west": -133.00111312500002, "east": -36.49720687499999, "south": 40.67528087446994,
                                    "north": 57.58277224736895}, [{"regionId": 404375, "regionType": 2}]],
        [{"currentPage": 1}, "MB",
         {"west": -143.745199625, "east": -47.24129337499999, "south": 46.61526044757908, "north": 61.72876707649884},
         [{"regionId": 404366, "regionType": 2}]],
        [{"currentPage": 1}, "NS", {"west": -75.09758778125, "east": -50.97161121874999, "south": 42.233426826928486,
                                    "north": 48.287604943570564}, [{"regionId": 404371, "regionType": 2}]]
    ]

    ZILLOW_BASE_LINK = "https://www.zillow.com/search/GetSearchPageState.htm?"
