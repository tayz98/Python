## Da immobilienscout eine sehr starke Roboter-Erkennung hat und auch der Weg über den Chrome Webdriver(Selenium) nicht funktionierte,
## nutze ich statt .get einen .post Befehl beim Request und erhalte dadurch ein JSON Packet. 

# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Cookie senden
import urllib
import http.cookiejar

titel = []
kaltmiete = []
adresse = []
zimmer = []
fläche = []
straße = []
hausnummer = []
postleitzahl = []
stadt = []
stadtviertel = []
ansprechperson = []
telefon = []


# Übernehmen der URL
url = "https://www.immobilienscout24.de/Suche/de/schleswig-holstein/kiel/wohnung-mieten?price=0.0-500.0&livingspace=25.0-55.0&pricetype=rentpermonth&enteredFrom=result_list"


# Variable in der das Ergebnis des GET Requests gespeichert wird
jsonData = requests.post(url).json()



for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    titel_temp=item['resultlist.realEstate']['title'] 
    titel.append(titel_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    kaltmiete_temp=item['attributes'][0]['attribute'][0]['value'].replace('€','').replace('.',',')
    kaltmiete.append(kaltmiete_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    fläche_temp=item['attributes'][0]['attribute'][1]['value'].replace('m²', '')
    fläche.append(fläche_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    zimmer_temp=item['attributes'][0]['attribute'][2]['value']
    zimmer.append(zimmer_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    straße_temp=item['resultlist.realEstate']['address']['street']
    straße.append(straße_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    hausnummer_temp=item['resultlist.realEstate']['address']['houseNumber']
    hausnummer.append(hausnummer_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    postleitzahl_temp=item['resultlist.realEstate']['address']['postcode']
    postleitzahl.append(postleitzahl_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    stadt_temp=item['resultlist.realEstate']['address']['city']
    stadt.append(stadt_temp)

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    stadtviertel_temp=item['resultlist.realEstate']['address']['quarter']
    stadtviertel.append(stadtviertel_temp)                   

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    ansprechperson_temp_vorname=item['resultlist.realEstate']['contactDetails']['firstname']
    ansprechperson_temp_nachname=item['resultlist.realEstate']['contactDetails']['lastname'].replace('.','').replace(' ', '')
    ansprechperson.append(ansprechperson_temp_vorname + " " +ansprechperson_temp_nachname)           


inserat =  pd.DataFrame({
    'Titel': titel,
    'Kaltmiete': kaltmiete,
    'Wohnfläche' : fläche,
    'Anz. Zimmer': zimmer,
    'Straße': straße,
    'Hausnummer': hausnummer,
    'Postleitzahl': postleitzahl,
    'Stadt': stadt,
    'Stadtviertel': stadtviertel,
    'Ansprechperson': ansprechperson

})

inserat.to_csv('inserate.csv')
