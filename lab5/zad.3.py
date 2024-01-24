import time
Czas=int(input("Podaj liczbę sekund: "))
while Czas > 0:
    print("Pozostało", Czas, "s")
    time.sleep(1)
    Czas -= 1
print("Koniec czasu")