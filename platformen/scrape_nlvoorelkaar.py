import requests
import json

from bs4 import BeautifulSoup

# Category 45 is the one for Corona
URL = 'https://www.nlvoorelkaar.nl/hulpvragen/update/resultmarkers.json?categories[]=45'
page = requests.get(URL)
result = page.json()

hulpvragen = []
for marker in result['markers']:
    markerurl = 'https://www.nlvoorelkaar.nl/hulpvragen/%s' % marker['id']
    detail = requests.get(markerurl)
    soup = BeautifulSoup(detail.content, 'html.parser')
    table = soup.find("dl")
    records = table.findAll("dd")
    description = soup.find("p").text.strip(' \t\n\r')
    hulpvragen.append({'source': markerurl, 'source_id': marker['id'], 'category': records[1].text, 'location': {
                      'title': records[0].text}, 'description': description, 'frequency': records[2].text, "group": "demand"})
with open('./nlvoorelkaar.json', 'w') as f:
    json.dump(hulpvragen, f, skipkeys=True, ensure_ascii=True,
              indent=2, separators=None, default=None, sort_keys=True)
