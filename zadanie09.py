import requests
import sys
from datetime import datetime

startTime = datetime.now()
link_flagi = 'https://zajecia-programowania-xd.pl/flagi'

def pobierz_strone_www_jako_text(orangutan):
    # Pobranie tekstu ze strony (jako tafla tesktu).
    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text

def stworz_liste_flag(orangutan):
    '''
    Zamienia tekst ze strony na liste flag.
    '''
    
    text_strony_www = pobierz_strone_www_jako_text(orangutan)
    lista_linii = text_strony_www.split('</p>')
    linki = []
    # Iteruje po wszystkich fragmentach tekstu z html
    # i dodaje do listy tylko te ktore maja link url.
    for linia in lista_linii:

        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        if link:
            linki.append(link)
    
    return linki

'''
if __name__ == '__main__':
    argument = sys.argv[0]
    lista_flag = stworz_liste_flag(argument)
    #print(lista_flag)
'''
#print(stworz_liste_flag(link_flagi))

def ile_pl(): ### funkcja 1 
    lista_z_pl = []
    for l in stworz_liste_flag(link_flagi):        
        if l.find('.pl.') != -1:
            lista_z_pl.append(l)
            continue     
        if l.endswith('.pl'):
            lista_z_pl.append(l)
    
    dlug_pl = len(lista_z_pl)
    return dlug_pl

def ile_com(): ### funkcja 2
    wynik = 0
    for l in stworz_liste_flag(link_flagi):
        if l.endswith('.com'):
            #print(l)
            wynik += 1
    return wynik

def ile_a(): ### funkcja 3
    listaliterek = []
    wynik = 0
    stringzlisty = str(stworz_liste_flag(link_flagi))
    for literka in stringzlisty:
        listaliterek.append(literka)
    for l in listaliterek:
        if l == 'a':
            wynik += 1
    return wynik

def najdlusza_i_najkrotsza(): ### funkcja 4
    liczba_najdlusza = 0 
    for ld in stworz_liste_flag(link_flagi):
        if len(ld) > liczba_najdlusza:
            liczba_najdlusza = len(ld)
            domena_najdlusza = ld
    
    liczba_najkrotsza = liczba_najdlusza
    for lk in stworz_liste_flag(link_flagi):
        if len(lk) < liczba_najkrotsza:
            liczba_najkrotsza = len(lk)
            domena_najkrotsza = lk

    zwrot = [liczba_najdlusza, domena_najdlusza, liczba_najkrotsza, domena_najkrotsza]
    return zwrot

print('Funkcja 1. Ile jest domen które mają ".pl" (nie ważne czy mają ".edu.pl")')
print('Z', len(stworz_liste_flag(link_flagi)),'domen,',ile_pl(),'ma ".pl"')
print()
print("Funkcja 2. Ile jest domen które mają samo '.com'")
print(ile_com(),'domen ma końcówke ".com"')
print()
print("Funkcja 3. Ile jest literek 'a' we wszstkich domenach razem.")
print('Jest ich:',ile_a())
print()
print('Funkcja 4. Jaka jest najdłuższa i najkrótsza domena w liście flag.')
print('Najdłusza domena:',najdlusza_i_najkrotsza()[1], "ma",najdlusza_i_najkrotsza()[0],'znaków')
print('Najkrótsza domena:',najdlusza_i_najkrotsza()[3], "ma",najdlusza_i_najkrotsza()[2],'znaków')
print()
print('Czas wykonania skrytu:', datetime.now() - startTime)