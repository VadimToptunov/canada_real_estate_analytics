from bs4 import BeautifulSoup
import json
import random
import re
import requests
import time


companies = []

def get_data(start, city, province):

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    }
    attrs = f'{city}, {province}'

    params = (
        ('q', '(tester or QA or quality or assurance)'),
        ('l', attrs),
        ('jt', 'fulltime'),
        ('limit', '50'),
        ('taxo1', 'eXAh-UqhTh2uUxY71DdIeQ'),
        ('start', start),
        )

    session = requests.Session()
    response = session.get('https://ca.indeed.com/jobs', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.request.url)
    print(response.text)
    print(city, province)
    jobs = soup.find('div', {'class' : 'searchCountContainer'})
    all_jobs = jobs.text.replace(",", "")
    quantity = re.findall(r'(\d+)', all_jobs)[1].strip().replace(",", "")
    slider = soup.find_all('span', {"class" :'companyName'})
    for i in slider:
        companies.append(i.text)
    
    while start < int(quantity):
        start = start + 50
        time.sleep(random.randint(5, 73))
        get_data(start, city, province)
        break
    


if __name__ == '__main__':
    cities = [
        ("Toronto", "ON"),
        ("Winnipeg", "MB"),
        ("Calgary", "AB"),
        ("Montreal", "QC"),
        ("Vancouver", "BC")
    ]
    save = []
    for i in cities:
        get_data(0, *i)
        companies_set = set(companies)
        print(companies_set)
        print(len(companies_set))
        data = {
            "city_parameters" : i,
            "companies" : companies_set,
            "quantity_of_companies": len(companies_set)
        }
        save.append(data)
        companies = []

    data_to_save = json.dumps(save, indent=4)

    with open("work_analytics.json", "a+") as f:
        f.writelines(save)
