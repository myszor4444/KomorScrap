import requests
from bs4 import BeautifulSoup
import unicodedata
import re

def scrap_komor(x, y):
    url_base = "https://licytacje.komornik.pl/Notice/Details/"
    id_to_scrap = x
    numer_kw_regex = re.compile("[0-9 | A-z]{4}\/[0-9]{8}\/[0-9]")
    adres_regex = re.compile("położon.{70}")

    for i in range(y):
        site = requests.get(url_base + str(id_to_scrap))
        soup = BeautifulSoup(site.text,"html.parser")
        announce = soup.find_all("div", {"id" : "Preview" })
        kw_nums = soup.find_all("strong")

        if announce == '[]':
            continue
        else:
            with open("notices.html", "a") as plik:
                print(announce)
                plik.write("--------------------------\n")
                plik.write(unicodedata.normalize('NFKC', str(announce)) + "\n")

                numer_kw = re.findall(numer_kw_regex, str(announce))
                adres = re.findall(adres_regex, str(announce))

                with open("books", "a") as plik2:
                    print("Znaleziono numer kw: {} oraz adres {}".format(numer_kw, adres))
                    plik2.write("--------------------------\n")
                    plik2.write("Znaleziono numer kw: {} oraz adres {} \n".format(numer_kw, unicodedata.normalize('NFKC', str(adres)) + "\n"))

        id_to_scrap += 1
