import math

while True:
    dana = int(input("Podaj liczbę: "))
    if dana >= 0:
        print("To jest liczba")
        continue
    print("Pierwiastek kwadratowy z liczby", dana, "to", math.sqrt(dana))
    print("Dziękujemy za skorzystanie z naszej aplikacji")
    break
#b
import math

while True:
    dana = int(input("Podaj liczbę: "))
    if dana >= 0:
        print("To jest liczba")
    else:
        print("Pierwiastek kwadratowy z liczby", dana, "to", math.sqrt(dana))
        print("Dziękujemy za skorzystanie z naszej aplikacji")
        break
