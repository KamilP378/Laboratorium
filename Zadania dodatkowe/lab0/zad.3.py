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

print("Witaj")
print("Wybierz operację, która ma zostać wykonana:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybór=input("Wybierz numer operacji (1/2/3/4): ")

if wybór in ['1', '2', '3', '4']:
    a=float(input("Podaj 1 liczbę:"))
    b=float(input("Podaj 2 liczbę:"))

if wybór == '1':
    wynik = dodawanie(a, b)
    print("Wynik dodawania:", wynik)

elif wybór == '2':
    wynik = odejmowanie(a, b)
    print("Wynik odejmowania:", wynik)

elif wybór == '3':
    wynik = mnożenie(a, b)
    print("Wynik mnożenia:", wynik)

elif wybór == '4':
    if y != 0:
        wynik = dzielenie(a, b)
        print("Wynik dzielenia:", wynik)
    else:
        print("Nie można dzielić przez zero!")

