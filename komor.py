import requests
from bs4 import BeautifulSoup
import unicodedata

def scrap_komor(x, y):
    url_base = "https://licytacje.komornik.pl/Notice/Details/"
    id_to_scrap = x

    for i in range(y):
        site = requests.get(url_base + str(id_to_scrap))
        soup = BeautifulSoup(site.text,"html.parser")
        announce = soup.find_all("div", {"id" : "Preview" })

        with open("notices.txt", "a") as plik:
            print(announce)
            plik.write("--------------------------\n")
            plik.write(unicodedata.normalize('NFKC', str(announce)) + "\n")

        id_to_scrap += 1
