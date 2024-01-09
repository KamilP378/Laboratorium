imie = input("Podaj imię: ")
wiek = input("Podaj wiek: ")

def wypisz_imie(imie):
    """
    To funkcja związana jest z wyświetlaniem imienia.
    Jeśli zostanie podanie imię, wyświetli je.
    W przeciwnym razie zostanie wyświetlona tylko informacja "Nie podano imienia.".
    """
    if imie:
        print(f"Imię: {imie}")
    else:
        print("Nie podano imienia.")

def wypisz_wiek(wiek):
    """
    Ta funkcja związana jest z wyświetlaniem wieku.
    Jeśli wiek jest podany, wyświetla go.
    W przeciwnym razie ustawia wiek na 20 i wyświetla tę wartość.
    """
    if wiek:
        print(f"Wiek: {wiek}")
    else:
        wiek = 20
        print(f"Wiek: {wiek}")

wypisz_imie(imie)
wypisz_wiek(wiek)

print("Dokumentacja funkcji związanej z imieniem:")
print(wypisz_imie.__doc__)
print("Dokumentacja funkcji związanej z wiekiem:")
print(wypisz_wiek.__doc__)