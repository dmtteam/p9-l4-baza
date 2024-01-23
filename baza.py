import sys

name = ""
surname = ""
klasa = ""
typy = ["student", "teacher", "supervisor", "end"]
grupy = {}
persons = {}


class Grupa:
    def __init__(self, number):
        self.number = number
        self.supervisor = None
        self.teachers = []
        self.uczniowie = []

    def display(self):
        if self.supervisor:
            print(self.supervisor.nazwa)
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
    if person.nazwa not in persons:
        persons[person.nazwa] = []
    persons[person.nazwa].append(person)


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
        for teacher in grupa.teachers:
            print(teacher.subject)
            print(teacher.nazwa)


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
            if grupa.supervisor:
                print(grupa.supervisor.nazwa)
            else:
                print(f"The group {grupa.number} does not have a supervising teacher")


class Supervisor:
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
            grupa.supervisor = self
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
    elif typ == "teacher":
        person = Nauczyciel()
    elif typ == "supervisor":
        person = Supervisor()
    elif typ == "end":
        break

    person.pobierz()

# argv
if sys.argv[1] in grupy:
    grupa = grupy[sys.argv[1]]
    grupa.display()

if sys.argv[1] in persons:
    selected_people = persons[sys.argv[1]]
    for person in selected_people:
        person.display()
