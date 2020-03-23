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
    title = card.find('h5').text
    subtitle = card.find('h6').text
    description = card.find('p', class_='card-text').text
    hulpvragen.append({'title': title, 'location': subtitle, 'description': description})
with open('heldnodig.json', 'w') as f:
    json.dump(hulpvragen, f)




