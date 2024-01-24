import random

def gra():
    zakres_minimalny = int(input("Podaj zakres minimalny: "))
    zakres_maksymalny = int(input("Podaj zakres maksymalny: "))

    if zakres_minimalny >= zakres_maksymalny:
        print("Podany zakres jest nieprawidłowy. Dolna granica musi być mniejsza od górnej granicy.")
        return

    liczba = random.randint(zakres_minimalny, zakres_maksymalny)

    for i in range(3):
        odpowiedz = int(input("Podaj swoją odpowiedź: "))

        if odpowiedz < liczba:
            print("Za mało!")
        elif odpowiedz > liczba:
            print("Za dużo!")
        else:
            print("Gratulacje, zgadłeś liczbę!")
            return

    print("Niestety nie udało Ci się zgadnąć liczby. Spróbuj ponownie!")
gra()