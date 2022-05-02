## Da immobilienscout eine sehr starke Roboter-Erkennung hat und auch der Weg über den Chrome Webdriver(Selenium) nicht funktionierte,
## nutze ich statt .get einen .post Befehl beim Request und erhalte dadurch ein JSON Packet. 

# Requests wird benötigt, um einen GET Request zu stellen
import requests

# Zusammensetzen der Daten in DataFrames
import pandas as pd

## Variablen für die gesammelten Daten
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

#Abfragen für die Suche. Kein Try-Catch eingebaut, bitte fehlerhafte Eingaben vermeiden!
# BITTE KLEINBUCHSTABEN BEI BUNDESLAND/STADT BENUTZEN
preis_untergrenze = input('Bitte geben Sie eine Untergrenze für den Preis an: ') # z.B.: 0
preis_obergrenze = input('Bitte geben Sie eine Obergrenze für den Preis an: ')  # z.B.: 2000
bundesland = input('Bitte geben Sie das Bundesland mit einem Kleinbuchstaben an: ') # z.B.: hamburg oder schleswig-holstein 
stadt1 = input('Bitte geben Sie die Stadt mit einem Kleinbuchstaben an: ') # z.B.: hamburg oder kiel
wohnfläche_untergrenze = input('Bitte geben Sie die Untegrenze der Wohnfläche an (min:0): ')
wohnfläche_obergrenze = input('Bitte geben Sie die Obergrenze der Wohnfläche an (min:1): ')

# speichern des Suchergebnisses (Link) in eine Variable
url = ("https://www.immobilienscout24.de/Suche/de/" + bundesland + "/" + stadt1 + "/wohnung-mieten?price=" + preis_untergrenze + 
"-" + preis_obergrenze + "&livingspace=" + wohnfläche_untergrenze + "-" + wohnfläche_obergrenze +
"&pricetype=rentpermonth&enteredFrom=result_list")

# Falls der generierte Link warum auch immer nicht funktionieren sollte, bitte den nachstehenden Link auskommentieren
#url = "https://www.immobilienscout24.de/Suche/de/schleswig-holstein/kiel/wohnung-mieten?price=0.0-500.0&livingspace=25.0-55.0&pricetype=rentpermonth&enteredFrom=result_list"

# variable speichert das ergebnis des POST-Requests als encodierte json. 
jsonData = requests.post(url).json()

## for schleifen, um die Daten des json Pakets zu extrahieren.
for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        titel_temp=item['resultlist.realEstate']['title'] 
        titel.append(titel_temp)
    except KeyError:
        titel.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        kaltmiete_temp=item['attributes'][0]['attribute'][0]['value'].replace('€','').replace('.',',')
        kaltmiete.append(kaltmiete_temp)
    except KeyError:
        kaltmiete.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        fläche_temp=item['attributes'][0]['attribute'][1]['value'].replace('m²', '')
        fläche.append(fläche_temp)
    except KeyError:
        fläche.append("")    

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        zimmer_temp=item['attributes'][0]['attribute'][2]['value']
        zimmer.append(zimmer_temp)
    except KeyError:
        zimmer.append("")        

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        straße_temp=item['resultlist.realEstate']['address']['street']
        straße.append(straße_temp)
    except KeyError:
        straße.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        hausnummer_temp=item['resultlist.realEstate']['address']['houseNumber']
        hausnummer.append(hausnummer_temp)
    except KeyError:
        hausnummer.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try: 
        postleitzahl_temp=item['resultlist.realEstate']['address']['postcode']
        postleitzahl.append(postleitzahl_temp)
    except KeyError:
        postleitzahl.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        stadt_temp=item['resultlist.realEstate']['address']['city']
        stadt.append(stadt_temp)
    except KeyError:
        stadt.append("")

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        stadtviertel_temp=item['resultlist.realEstate']['address']['quarter']
        stadtviertel.append(stadtviertel_temp)
    except KeyError:
        stadtviertel.append("")                   

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    try:
        ansprechperson_temp_vorname=item['resultlist.realEstate']['contactDetails']['firstname']
    except KeyError:
        ansprechperson_temp_vorname =""  
    try: 
        ansprechperson_temp_nachname=item['resultlist.realEstate']['contactDetails']['lastname'].replace('.','').replace(' ', '')
    except KeyError:
        ansprechperson_temp_nachname = ""
    try:
        ansprech_person_temp_telefon=item['resultlist.realEstate']['contactDetails']['phoneNumber'].replace(' ','')
    except KeyError:
        ansprech_person_temp_telefon = ""
    ansprechperson.append(ansprechperson_temp_vorname + " " +ansprechperson_temp_nachname + " " + ansprech_person_temp_telefon)

## Zusammensetzen der Daten
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

## export zu einer CSV Datei
inserat.to_csv('inserate.csv')

input("Bitte schauen Sie sich jetzt die CSV Datei an und drücken eine Taste zum Beenden des Programms")