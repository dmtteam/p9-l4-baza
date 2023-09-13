import sys

name = ""
nazwisko = ""
klasa = ""
typy = ["uczen", "nauczyciel", "wychowawca", "end"]
grupy = {}
osoby = {}


class Grupa:
    def __init__(self, number):
        self.number = number
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie = []

    def display(self):
        if self.wychowawca:
            print(self.wychowawca.nazwa)
        else:
            print(f"Grupa {grupa.number} nie ma wychowawcy")
        for uczen in self.uczniowie:
            print(uczen.nazwa)

    def numberklasy(self):
        self.number = True


def get_group(number):
    if number not in grupy:
        grupa = Grupa(number)
        grupy[number] = grupa
    return grupy[number]


def add_person(osoba):
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
        grupa = get_group(self.klasa)
        grupa.uczniowie.append(self)
        add_person(self)

    def display(self):
        print(self.nazwa)
        grupa = get_group(self.klasa)
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
            grupa = get_group(klasa)
            grupa.nauczyciele.append(self)
        add_person(self)

    def display(self):
        print(self.nazwa)
        for klasa in self.klasy:
            grupa = get_group(klasa)
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
            grupa = get_group(klasa)
            grupa.wychowawca = self
        add_person(self)

    def display(self):
        for klasa in self.klasy:
            grupa = get_group(klasa)
            for uczen in grupa.uczniowie:
                print(uczen.nazwa)


while True:
    typ = input().strip()       # typ = input("Podaj typ: ").strip()
    if typ not in typy:
        print("Bad choice, try again!")
        continue
    elif typ == "uczen":
        osoba = Uczen()
    elif typ == "nauczyciel":
        osoba = Nauczyciel()
    elif typ == "wychowawca":
        osoba = Wychowawca()
    elif typ == "end":
        break

    osoba.pobierz()

# argv
if sys.argv[1] in grupy:
    grupa = grupy[sys.argv[1]]
    grupa.display()

if sys.argv[1] in osoby:
    selected_people = osoby[sys.argv[1]]
    for osoba in selected_people:
        osoba.display()
