import requests
import json

from bs4 import BeautifulSoup

URL = 'https://heldnodig.nl/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='container')

questions = results.find_all(class_='card')
hulpvragen = []
for card in questions:
    title = card.find('h5').text.strip(' \t\n\r')
    rawlocation = card.find('h6').text.strip(' \t\n\r')
    #remove (maps) from rawlocation, split on first space
    rawlocation = rawlocation.strip('(Maps)')
    locationobject = rawlocation.split(' ', 1)
    location = { 'postalcode': locationobject[0].strip(), 'city': locationobject[1].strip(), 'title': rawlocation.strip()}

    description = card.find('p', class_='card-text').text.strip(' \t\n\r')
    hulpvragen.append({'source': URL, 'category': title, 'location': location, 'description': description, "group": "demand"})
with open('./heldnodig.json', 'w') as f:
    json.dump(hulpvragen, f, skipkeys=True, ensure_ascii=True, indent=2, separators=None, default=None, sort_keys=True)
