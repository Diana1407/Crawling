import requests
from bs4 import BeautifulSoup
import re
nr_reparatii=0
nr_transporturi=0
nr_telefoane=0
nr_preturi=0
nr_mobila=0
nr_foraje=0
nr_masini=0
nr_meditatii=0
nr_inchirieri=0
nr_service=0
altceva=0
lista_service=[]
lista_inchiriere=[]
lista_meditatii=[]
lista_foraje=[]
lista_telefon=[]
lista_reparatii=[]
lista_transport=[]
lista_preturi=[]
lista_mobila=[]
lista_masini=[]
for i in range(25):
    page=requests.get("https://www.olx.ro/d/servicii-afaceri-colaborari/"+f"?page={i}")
    soup = BeautifulSoup(page.content, 'html.parser')
    anunturi=soup.find_all('h6')
    nr_anunt=-1
    for anunt in anunturi:
        nr_anunt+=1
        if re.findall('[rR]eparatii',anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche=[]
            pereche.append(anunt.get_text())
            pereche.append( "https://www.olx.ro"+contine_link[nr_anunt].get('href'))
            ok=1
            for element in lista_reparatii:
                if anunt.get_text()==element[0]:
                    ok=0
                    break
            if ok==1:
                nr_reparatii += 1
                lista_reparatii.append(pereche)
        if re.findall('[tT]ransport', anunt.get_text()) or re.findall( '[tT]ransporturi', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_transport:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_transporturi += 1
                lista_transport.append(pereche)
        if re.findall('((\+40)[ -])?\d{3}[ -]?\d{3}[ -]?\d{4}',anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_telefon:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_telefoane += 1
                lista_telefon.append(pereche)
        if re.findall('[lL]ei', anunt.get_text()) or re.findall('[Rr]on', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_preturi:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_preturi += 1
                lista_preturi.append(pereche)
        if re.findall('[Mm]obil[aă]', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_mobila:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_mobila += 1
                lista_mobila.append(pereche)
        if re.findall('([fF]oraj)([fF]oraje)*', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_foraje:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_foraje += 1
                lista_foraje.append(pereche)
        if re.findall('[mM]editatii',anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche=[]
            pereche.append(anunt.get_text())
            pereche.append( "https://www.olx.ro"+contine_link[nr_anunt].get('href'))
            ok=1
            for element in lista_meditatii:
                if anunt.get_text()==element[0]:
                    ok=0
                    break
            if ok==1:
                nr_meditatii += 1
                lista_meditatii.append(pereche)
        if re.findall('([Aa]uto)([aA]utoturism)([aA]utoturisme)*',anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche=[]
            pereche.append(anunt.get_text())
            pereche.append( "https://www.olx.ro"+contine_link[nr_anunt].get('href'))
            ok=1
            for element in lista_masini:
                if anunt.get_text()==element[0]:
                    ok=0
                    break
            if ok==1:
                nr_masini += 1
                lista_masini.append(pereche)
        if re.findall('[îÎIi]nchiriere', anunt.get_text()) or re.findall( '[îÎIi]nchirieri', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_inchiriere:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_inchirieri += 1
                lista_inchiriere.append(pereche)
        if re.findall('[Ss]ervice', anunt.get_text()):
            contine_link = soup.find_all('a', class_='css-1bbgabe')
            pereche = []
            pereche.append(anunt.get_text())
            pereche.append("https://www.olx.ro" + contine_link[nr_anunt].get('href'))
            ok = 1
            for element in lista_service:
                if anunt.get_text() == element[0]:
                    ok = 0
                    break
            if ok == 1:
                nr_service += 1
                lista_service.append(pereche)
        else:
            altceva+=1

print("hei, numarul total de reparatii este de:" , end="")
print(nr_reparatii)
print("Anunturile:")
print()
for element in lista_reparatii:
    print (element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii de transporturi este de:", end="")
print(nr_transporturi)
print("Anunturile:")
print()
for element in lista_transport:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii care au numar de telefon este de:", end="")
print(nr_telefoane)
print("Anunturile:")
print()
for element in lista_telefon:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii care au pret este de:", end="")
print(nr_preturi)
print("Anunturile:")
print()
for element in lista_preturi:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii foraje:", end="")
print(nr_foraje)
print("Anunturile:")
print()
for element in lista_foraje:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de meditatii:", end="")
print(nr_meditatii)
print("Anunturile:")
print()
for element in lista_meditatii:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii autoturisme:", end="")
print(nr_masini)
print("Anunturile:")
print()
for element in lista_masini:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii cu mobila:", end="")
print(nr_mobila)
print("Anunturile:")
print()
for element in lista_mobila:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii inchirieri:", end="")
print(nr_inchirieri)
print("Anunturile:")
print()
for element in lista_inchiriere:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul total de servicii tip service:", end="")
print(nr_service)
print("Anunturile:")
print()
for element in lista_service:
    print(element[0], end="")
    print("->", end="")
    print(element[1])
    print()
print("Numarul anunturilor ce nu au putut fi filtrate: ", altceva)