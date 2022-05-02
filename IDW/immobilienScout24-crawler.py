

# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Übernehmen der URL
url = "https://www.immobilienscout24.de/Suche/de/schleswig-holstein/kiel/wohnung-mieten?price=0.0-500.0&livingspace=25.0-55.0&pricetype=rentpermonth&enteredFrom=result_list"
# Vorgaukeln eines "echten" Browser
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
            'Accept-Language': 'de'})

# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url, headers=HEADERS)

# Übersetzen des Inhalts von result
soup = BeautifulSoup(results.text, "html.parser")


# Separieren der benötigten Informationen aus dem gesamten Code heraus.
item_div = soup.find_all('div', class_='result-list-entry__data')

print(item_div)