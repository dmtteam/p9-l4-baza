import sys

name = ""
surname = ""
klasa = ""
typy = ["student", "nauczyciel", "wychowawca", "end"]
grupy = {}
osoby = {}


class Grupa:
    def __init__(self, number):
        self.number = number
        self.wychowawca = None
        self.teachers = []
        self.uczniowie = []

    def display(self):
        if self.wychowawca:
            print(self.wychowawca.nazwa)
        else:
            print(f"The group  {grupa.number} does not have a supervising teacher")
        for student in self.uczniowie:
            print(student.nazwa)

    def numberklasy(self):
        self.number = True


def get_group(number):
    if number not in grupy:
        grupa = Grupa(number)
        grupy[number] = grupa
    return grupy[number]


def add_person(person):
    if person.nazwa not in osoby:
        osoby[person.nazwa] = []
    osoby[person.nazwa].append(person)


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
        for nauczyciel in grupa.teachers:
            print(nauczyciel.subject)
            print(nauczyciel.nazwa)


class Nauczyciel:
    def __init__(self):
        self.nazwa = ""
        self.subject = ""
        self.klasy = []

    def pobierz(self):
        self.nazwa = input().strip()
        self.subject = input().strip()

        while True:
            klasa = input().strip()
            if not klasa:
                break
            self.klasy.append(klasa)
            grupa = get_group(klasa)
            grupa.teachers.append(self)
        add_person(self)

    def display(self):
        print(self.nazwa)
        for klasa in self.klasy:
            grupa = get_group(klasa)
            if grupa.wychowawca:
                print(grupa.wychowawca.nazwa)
            else:
                print(f"The group {grupa.number} does not have a supervising teacher")


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
            for student in grupa.uczniowie:
                print(student.nazwa)


while True:
    typ = input().strip()       # typ = input("Podaj typ: ").strip()
    if typ not in typy:
        print("Bad choice, try again!")
        continue
    elif typ == "student":
        person = Uczen()
    elif typ == "nauczyciel":
        person = Nauczyciel()
    elif typ == "wychowawca":
        person = Wychowawca()
    elif typ == "end":
        break

    person.pobierz()

# argv
if sys.argv[1] in grupy:
    grupa = grupy[sys.argv[1]]
    grupa.display()

if sys.argv[1] in osoby:
    selected_people = osoby[sys.argv[1]]
    for person in selected_people:
        person.display()
