import sys

imie = ""
nazwisko = ""
klasa = ""
typy = ["uczen", "nauczyciel", "wychowawca", "koniec"]


class Uczen:
    def __init__(self):
        self.nazwa=""
        self.klasa=""

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ")
        self.klasa = input("Klasa: ")

#    def show(self):
#        return "Uczen {} jest w klasie {}".format(self.nazwa, self.klasa)

# jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą


class Nauczyciel:
    def __init__(self):
        self.nazwa=""
        self.przedmiot=""
        self.klasy=[]

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ")
        self.przedmiot = input("Przedmiot: ")
        while True:
            klasa = input("Klasa: ")
            if not klasa:
                break
            self.klasy.append(klasa)

#    def show(self):
#    return "Nauczyciel {} uczy przedmiotu {} w klasach {}".format(self.nazwa,self.przedmiot, self.klasy)

# jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel


class Wychowawca:
    def __init__(self):
        self.nazwa=""
        self.klasy=[]

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ")
        while True:
            klasa = input("Klasa: ")
            if not klasa:
                break
            self.klasy.append(klasa)

#    def show(self):
#    return "Wychowawca {} ma klasy {}".format(self.nazwa, self.klasy)

#    jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca


class Klasasys:
    def __init__(self):
        self.numer=""

    def numerklasy(self):
        self.numer = True

# jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie


while True:
    typ = input("Podaj typ: ")
    if typ not in typy:
        print("Zły wybor. Jeszcze raz!")
        continue
    elif typ == "uczen":
        osoba = Uczen()
    elif typ == "nauczyciel":
        osoba = Nauczyciel()
    elif typ == "wychowawca":
        osoba = Wychowawca()
    elif typ == "koniec":
        break

    osoba.pobierz()
    print(osoba.__dict__)

    continue



if sys.argv[1] in typy:
    os = typ[sys.argv[1]]

    #for o in os:
        # o.show()
        # print(osoba.__dict__)
        # print(osoba)

