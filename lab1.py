#zad1

def oblicz_cene_biletu(wiek):
    if wiek < 4:
        return 0
    elif wiek <= 18:
        return 10
    else:
        return 20
wiek=int(input("Podaj wiek: "))
cena_biletu=oblicz_cene_biletu(wiek)
print("Cena biletu to: {} zł".format(cena_biletu))

#zad2
litera = input("Podaj literę: ")
if litera.islower():
    print("Podana litera jest mała.")
elif litera.isupper():
    print("Podana litera jest duża.")
else:
    print("Podany znak nie jest literą.")

#zad3
def dodawanie (x, y):
    return x+y
def odejmowanie (x, y):
    return x-y
def mnożenie (x, y):
    return x*y
def dzielenie (x, y):
    return x/y
def potęga (x, y):
    return x ** y

print("Witaj w prostym kalkulatorze")
print("Wybierz operację, która ma zostać wykonana:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")

wybór=input("Wybierz numer operacji (1/2/3/4/5): ")

if wybór in ['1', '2', '3', '4', '5']:
    x=float(input("Podaj 1 liczbę: "))
    y=float(input("Podaj 2 liczbę: "))

    if wybór == '1':
        wynik = dodawanie(x, y)
        print("Wynik dodawania:", wynik)

    elif wybór == '2':
        wynik = odejmowanie(x, y)
        print("Wynik odejmowania:", wynik)

    elif wybór == '3':
        wynik = mnożenie(x, y)
        print("Wynik mnożenia:", wynik)

    elif wybór == '4':
        if y != 0:
           wynik = dzielenie(x, y)
           print("Wynik dzielenia:", wynik)
        else :
            print("Nie można dzielić przez zero!")

    elif wybór == '5':
        wynik = potęga(x, y)
        print("Wynik potęgowania:", wynik)
else:
    print("Nieprawidłowy wybór operacji!")

#zad4
import cmath

# wprowadzanie współczynników przez użytkownika
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Obliczanie deltę
delta = b**2 - 4*a*c

# Sprawdzenie wartości delty i obliczanie rozwiązań
if delta > 0:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print("Równanie ma dwa rozwiązania:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Równanie ma jedno rozwiązanie:")
    print("x =", x)
else:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print("Równanie ma dwa pierwiastki zespolone:")
    print("x1 =", x1)
    print("x2 =", x2)

#zad5
# Pobieranie trzech liczb od użytkownika
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
z = float(input("Podaj trzecią liczbę: "))

# Porządkowanie liczb
if x <= y and x <= z:
    smallest = x
    if y <= z:
        middle = y
        largest = z
    else:
        middle = z
        largest = y
elif y <= x and y <= z:
    smallest = y
    if x <= z:
        middle = x
        largest = z
    else:
        middle = z
        largest = x
else:
    smallest = z
    if x <= y:
        middle = x
        largest = y
    else:
        middle = y
        largest = x

# Wyświetlanie posortowanych liczb
print("Posortowane liczby:", smallest, middle, largest)