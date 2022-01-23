import sys
# w in.txt wychowaca i uczen tak samo sie nazywaja

"""jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą"""

imie = ""
nazwisko = ""
klasa = ""
typy = ["uczen", "nauczyciel", "wychowawca", "koniec"]
grupy = {}
osoby ={}


class Grupa:
    def __init__(self, numer):
        self.numer = numer
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie = []

    def wyswietl(self):
        print(self.wychowawca.nazwa)
        for uczen in self.uczniowie:
            print(uczen.nazwa)

    def numerklasy(self):
        self.numer = True


def pobierz_grupe(numer):
    if numer not in grupy:
        grupa = Grupa(numer)
        grupy[numer] = grupa
    return grupy[numer]


def dodaj_osobe(osoba):
    if osoba.nazwa not in osoby:
        osoby[osoba.nazwa]=[]
    osoby[osoba.nazwa].append(osoba)


class Uczen:
    def __init__(self):
        self.nazwa=""
        self.klasa=""


    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ").strip()
        self.klasa = input("Klasa: ").strip()
        grupa=pobierz_grupe(self.klasa)
        grupa.uczniowie.append(self)
        dodaj_osobe(self)

    def wyswietl(self):  # nowe, sprawdzic
        print(self.nazwa.nazwa)
        print(self.klasa.numer)


class Nauczyciel:
    def __init__(self):
        self.nazwa=""
        self.przedmiot=""
        self.klasy=[]

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ").strip()
        self.przedmiot = input("Przedmiot: ").strip()

        while True:
            klasa = input("Klasa: ").strip()
            if not klasa:
                break
            self.klasy.append(klasa)

            grupa=pobierz_grupe(klasa)
            grupa.nauczyciele.append(self)
        dodaj_osobe(self)

#    def show(self):
#    return "Nauczyciel {} uczy przedmiotu {} w klasach {}".format(self.nazwa,self.przedmiot, self.klasy)
# jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel


class Wychowawca:
    def __init__(self):
        self.nazwa=""
        self.klasy=[]

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ").strip()
        while True:
            klasa = input("Klasa: ").strip()
            if not klasa:
                break
            self.klasy.append(klasa)
            grupa=pobierz_grupe(klasa)
            grupa.wychowawca=self
        dodaj_osobe(self)


#    def show(self):
#    return "Wychowawca {} ma klasy {}".format(self.nazwa, self.klasy)
#    jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
# jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie

while True:
    typ = input("Podaj typ: ").strip()
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
#pobierz.grupe()
    print(osoba.__dict__)
#print(grupy.__dict__)
    continue

# argv
if sys.argv[1] in grupy:
    grupa = grupy[sys.argv[1]]
    grupa.wyswietl()