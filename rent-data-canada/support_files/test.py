# import requests
# from bs4 import BeautifulSoup
from seleniumwire import webdriver

basic_url = "https://ca.indeed.com/"
"jobs?q=(tester+or+QA+or+quality+or+assurance)&l=Vancouver,+BC&jt=fulltime&limit=50&taxo1=eXAh-UqhTh2uUxY71DdIeQ"

companies = []

def get_cookies(city, province):
    # driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    main_url = f"{basic_url}jobs?q=(tester+or+QA+or+quality+or+assurance)&l={city},+{province}&jt=fulltime&limit=50&taxo1=eXAh-UqhTh2uUxY71DdIeQ"
    driver.get(main_url)

    for req in driver.requests:
        if req.url.find("jobs?q=(tester+or+QA+or+quality+or+assurance)") != -1:
            headers = dict(req.headers)
            params = req.params

    company_names = driver.find_elements_by_class_name("companyName")
    for company in company_names:
        companies.append(company.text)

    driver.find_elements_by_class_name("pn").click()
    driver.quit()
    print(companies)


if __name__ == '__main__':
    get_cookies("Vancouver", "BC")
    # get_data(*cookies)