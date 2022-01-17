import sys
# uwaga w in.txt wychowaca i uczen tak samo sie nazywaja
imie = ""
nazwisko = ""
klasa = ""
typy = ["uczen", "nauczyciel", "wychowawca", "koniec"]
grupy = {}

class Grupa:
    def __init__(self, numer):
        self.numer = numer
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie = []
        self.przedmioty = []    # nowe

    def numerklasy(self):
        self.numer = True

def pobierz_grupe(numer):
    if numer not in grupy:
        grupa = Grupa(numer)
        grupy[numer] = grupa
    return grupy[numer]


class Uczen:
    def __init__(self):
        self.nazwa=""
        self.klasa=""

    def pobierz(self):
        self.nazwa = input("Imie nazwisko: ")
        self.klasa = input("Klasa: ")
        grupa=pobierz_grupe(self.klasa)
        grupa.uczniowie.append(self)



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
# self.przedmiot.append(klasa)    # nowe - czy potrzebne

        while True:
            klasa = input("Klasa: ")
            if not klasa:
                break
            self.klasy.append(klasa)



            grupa=pobierz_grupe(self.klasa)
            grupa.nauczyciele.append(self)

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
            grupa=pobierz_grupe(self.klasy)   # (self.klasa) było
            grupa.wychowawca=self   # do ktoreefo self to sie odnosi - z def init ?



#    def show(self):
#    return "Wychowawca {} ma klasy {}".format(self.nazwa, self.klasy)

#    jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca




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
#pobierz.grupe()
    print(osoba.__dict__)
#print(grupy.__dict__)

    continue


if sys.argv[1] in typy:
    os = typ[sys.argv[1]]

    #for o in os:
        # o.show()
        # print(osoba.__dict__)
        # print(osoba)


"""  
    def pobierz_grupe(numer):
            if numer not in grupy:
                grupa = Grupa(numer)
                grupy[numer] = grupa
            return grupy[numer]
"""

