import sys

imie = ""
nazwisko = ""
# jak zapisac ponizej ????
imie_nazwisko = [imie, nazwisko]

uczen = ()              # jest w 1 klasie
nauczyciel = []         # ma przypisany 1 przedmiot i wiele klas
wychowawca = ()         # ma przypisane wiele klas
klasa = ""
a=True

typ = ["uczen", "nauczyciel", "wychowawca", "koniec"]

"""
Class uczeniowe():
Class nauczuciele():
Class wychowawcy():
"""

#def start():
# czy mozna tu tez zdefiniować IF i wkleic w while?

def rodo():
    imie = input('Imie: ')
    nazwisko = input('Nazwisko: ')
# imie_nazwisko = [imie, nazwisko] ?
    return imie, nazwisko
# czy bez return mozliwe?

def kl():
    klasa = input('Podaj nr klasy:')
    return klasa

while True:
# def start()
    print(f'typy: {typ}')
    wybor = input('Jaki typ? ')
    if wybor not in typ:
        print("Zły wybor. Jeszcze raz!")
        continue
    if wybor == "koniec":
        break


    if wybor == "uczen":
        rodo()
        kl()
# tu slownik (uczen, imie, nazwisko, nr klasy) ?

        baza_uczen = (imie, nazwisko, klasa)

        print(baza_uczen)
        print('uczen END')
        continue


    if wybor == "nauczyciel":

        rodo()


        przedmiot = str(input("Jaki przedmiot? "))
# czy potrzebna petla w petli?
        a = 'stop'
        while a == 'stop':
            kl()
            if not kl():
                break
            else:
                continue
        # tu stworzyc slownik (nauczyciel, imie, nazwisko, przedmiot, nr klasy1, nr klasy2)
        print('nauczyciel end')

    if wybor == "wychowawca":
        rodo()

        a = 'stop'
        while a == 'stop':
            kl()
            if not kl():
                break
            else:
                continue

        # tu stworzyc słownik (wychowawca, imie, nazwisko, nr klasy1, nr klasy2)
        print('wychowawca END')

# argv start here
wybor = sys.argv[1]

# argv uczen

if wybor == "uczen":
    imie = str(sys.argv[2])
    nazwisko = str(sys.argv[3])
    klasa = str(sys.argv[4])

    print(f"Uczen z argv wprowadzono: {imie}, {nazwisko}, klasa: {klasa}")

# argv nauczyciel

if wybor == "nauczyciel":
    imie = str(sys.argv[2])
    nazwisko = str(sys.argv[3])
    przedmiot = str(sys.argv[4])
# moze byc w wielu klasach
    klasa = str(sys.argv[5])

    print(f"Nauczciel z argv wprowadzono:\n {imie}, \n{nazwisko},\n{przedmiot} \nklasy: {klasa}")


# argv wychowawca

if wybor == "wychowawca":
    imie = str(sys.argv[2])
    nazwisko = str(sys.argv[3])
# moze byc w wielu klasach
# jak w argv zrobic ?
#   for in
    klasa = str(sys.argv[4])
#   ktore_klasy= (klasa + )

    print(f"Nauczciel z argv wprowadzono:\n {imie},\n {nazwisko},\n {klasa}")