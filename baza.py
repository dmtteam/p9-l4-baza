import sys

name = ""
nazwisko = ""
klasa = ""
typy = ["uczen", "nauczyciel", "wychowawca", "koniec"]
grupy = {}
osoby = {}


class Grupa:
    def __init__(self, number):
        self.number = number
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie = []

    def wyswietl(self):
        if self.wychowawca:
            print(self.wychowawca.nazwa)
        else:
            print(f"Grupa {grupa.number} nie ma wychowawcy")
        for uczen in self.uczniowie:
            print(uczen.nazwa)

    def numberklasy(self):
        self.number = True


def pobierz_grupe(number):
    if number not in grupy:
        grupa = Grupa(number)
        grupy[number] = grupa
    return grupy[number]


def dodaj_osobe(osoba):
    if osoba.nazwa not in osoby:
        osoby[osoba.nazwa] = []
    osoby[osoba.nazwa].append(osoba)


class Uczen:
    def __init__(self):
        self.nazwa = ""
        self.klasa = ""

    def pobierz(self):
        self.nazwa = input().strip()
        self.klasa = input().strip()
        grupa = pobierz_grupe(self.klasa)
        grupa.uczniowie.append(self)
        dodaj_osobe(self)

    def wyswietl(self):
        print(self.nazwa)
        grupa = pobierz_grupe(self.klasa)
        for nauczyciel in grupa.nauczyciele:
            print(nauczyciel.przedmiot)
            print(nauczyciel.nazwa)


class Nauczyciel:
    def __init__(self):
        self.nazwa = ""
        self.przedmiot = ""
        self.klasy = []

    def pobierz(self):
        self.nazwa = input().strip()
        self.przedmiot = input().strip()

        while True:
            klasa = input().strip()
            if not klasa:
                break
            self.klasy.append(klasa)
            grupa = pobierz_grupe(klasa)
            grupa.nauczyciele.append(self)
        dodaj_osobe(self)

    def wyswietl(self):
        print(self.nazwa)
        for klasa in self.klasy:
            grupa = pobierz_grupe(klasa)
            if grupa.wychowawca:
                print(grupa.wychowawca.nazwa)
            else:
                print(f"Grupa {grupa.number} nie ma wychowawcy")


class Wychowawca:
    def __init__(self):
        self.nazwa = ""
        self.klasy = []

    def pobierz(self):
        self.nazwa = input().strip()
        while True:
            klasa = input().strip()
            if not klasa:
                break
            self.klasy.append(klasa)
            grupa = pobierz_grupe(klasa)
            grupa.wychowawca = self
        dodaj_osobe(self)

    def wyswietl(self):
        for klasa in self.klasy:
            grupa = pobierz_grupe(klasa)
            for uczen in grupa.uczniowie:
                print(uczen.nazwa)


while True:
    typ = input().strip()       # typ = input("Podaj typ: ").strip()
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

# argv
if sys.argv[1] in grupy:
    grupa = grupy[sys.argv[1]]
    grupa.wyswietl()

if sys.argv[1] in osoby:
    wybrane_osoby = osoby[sys.argv[1]]
    for osoba in wybrane_osoby:
        osoba.wyswietl()
