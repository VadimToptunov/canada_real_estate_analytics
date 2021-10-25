import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"

response = requests.get(url)
text = response.text
data = []
soup = BeautifulSoup(response.text, 'lxml')
cities = soup.findAll('table', {'class' : 'wikitable'})
for city in cities:
    info = city.findAll("th")
    for inf in info:
        if "Quebec" in inf.text:
            c = city.findAll("a", title=True)
            for cc in c:
                t = cc.text
                if ("No.") not in t:
                    data.append("qc%2F" + f"{cc.text}".replace(" ", "").lower())

print(list(set(data)))