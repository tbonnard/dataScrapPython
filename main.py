# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests

from urllib.request import urlopen
import ssl
import json


URL_SOURCE = "https://metsvins.fr"

# CHOISIR L'URL EN FONCTION
URL = "https://metsvins.fr/mets"
# URL = "https://metsvins.fr/vins"


context = ssl._create_unverified_context()
res = urlopen(URL,
              context=context)
soup = BeautifulSoup(res, "html.parser")
data = soup.select(selector="li a")

urls_mets = []

for item in data:
    href_item = item.get_text()
    urls_mets.append(f"{URL_SOURCE}{item.get('href')}")
    # print(href_item, ";", item.get('href'))
print(urls_mets)


vins_mets = []

for i in urls_mets:
    context = ssl._create_unverified_context()
    res = urlopen(i,
                  context=context)
    soup = BeautifulSoup(res, "html.parser")
    data = soup.select(selector="li a")
    wines = []
    # CHANGER ICI met/vin et mets/vins
    new_dict = {
        "URL": i,
        "met": i.replace("https://metsvins.fr/", "").replace("-", " "),
        "vins": wines
    }
    for item in data:
        wines.append(item.get_text())
    vins_mets.append(new_dict)

# CHANGER ICI mets_vins et vins_mets
with open('mets_vins_reco', "w") as f:
    json.dump(vins_mets, f, indent=4, ensure_ascii=False)






