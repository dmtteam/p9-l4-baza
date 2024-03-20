import sys

name = ""
surname = ""
classroom = ""
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


class Student:
    def __init__(self):
        self.nazwa = ""
        self.classroom = ""

    def pobierz(self):
        self.nazwa = input().strip()
        self.classroom = input().strip()
        grupa = get_group(self.classroom)
        grupa.uczniowie.append(self)
        add_person(self)

    def display(self):
        print(self.nazwa)
        grupa = get_group(self.classroom)
        for teacher in grupa.teachers:
            print(teacher.subject)
            print(teacher.nazwa)


class Teacher:
    def __init__(self):
        self.nazwa = ""
        self.subject = ""
        self.klasy = []

    def pobierz(self):
        self.nazwa = input().strip()
        self.subject = input().strip()

        while True:
            classroom = input().strip()
            if not classroom:
                break
            self.klasy.append(classroom)
            grupa = get_group(classroom)
            grupa.teachers.append(self)
        add_person(self)

    def display(self):
        print(self.nazwa)
        for classroom in self.klasy:
            grupa = get_group(classroom)
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
            classroom = input().strip()
            if not classroom:
                break
            self.klasy.append(classroom)
            grupa = get_group(classroom)
            grupa.supervisor = self
        add_person(self)

    def display(self):
        for classroom in self.klasy:
            grupa = get_group(classroom)
            for student in grupa.uczniowie:
                print(student.nazwa)


while True:
    typ = input().strip()       # typ = input("Podaj typ: ").strip()
    if typ not in typy:
        print("Bad choice, please try again!")
        continue
    elif typ == "student":
        person = Student()
    elif typ == "teacher":
        person = Teacher()
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
