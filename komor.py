import requests
from bs4 import BeautifulSoup
import unicodedata
import re

def scrap_komor(x, y):
    url_base = "https://licytacje.komornik.pl/Notice/Details/"
    id_to_scrap = x
    numer_kw_regex = re.compile("[0-9 | A-z]{4}\/[0-9]{8}\/[0-9]")
    adres_regex = re.compile("położon.{170}")

    for i in range(y):
        site = requests.get(url_base + str(id_to_scrap))
        soup = BeautifulSoup(site.text,"html.parser")
        announce = soup.find_all("div", {"id" : "Preview" })
        kw_nums = soup.find_all("strong")

        if len(announce) == 0:
            print("Obwieszczenie nr {} jest puste".format(id_to_scrap))
        else:
            with open("notices.html", "a") as plik:
                print(announce)
                plik.write("--------------------------\n")
                plik.write(unicodedata.normalize('NFKC', str(announce)) + "\n")

                numer_kw = re.findall(numer_kw_regex, str(announce))
                adres = re.findall(adres_regex, str(announce))

                with open("books.txt", "a") as plik2:
                    print("Znaleziono numer kw: {} oraz adres {}".format(numer_kw, adres))
                    plik2.write("--------------------------\n")
                    plik2.write("Znaleziono numer kw: {} oraz adres {} \n".format(numer_kw, unicodedata.normalize('NFKC', str(adres)) + "\n"))
        id_to_scrap += 1


print("To jest KomorScrap. Program do scrapowania obwieszczeń komorniczych \n\n")
start_notice = int(input("Podaj nr obwieszczenia, od którego mam zacząć scrapowanie: "))
how_many = int(input("Podaj liczbę obwieszczeń do zescrapowania: "))
print("Rozpoczynam scrapowanie...")
scrap_komor(start_notice, how_many)
print("Scrapowanie zakończone.\nPobrane obwieszczenia znajdziesz w pliku notices.html, zaś numery ksiąg wieczystych w bliku books.txt")
print("Dzięki i do następnego razu :)")
