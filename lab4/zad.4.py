Liczba=float(input("Podaj wartośc x: "))
def sprawdz_czy_dodatnie(x):
    if x > 0:
        return True
    else:
        return False
czy_dodatnie=sprawdz_czy_dodatnie(Liczba)
if czy_dodatnie:
    print("Jest dodatnie")
else:
    print("Nie jest dodatnie")