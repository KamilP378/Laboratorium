import random

cyfry=input("Podaj pięć cyfr rozdzielonych przecinkiem: ")

tablica=cyfry.split(',')
if len(tablica) != 5:
    print("Podano nieprawidłową ilość liczb. Proszę podać dokładnie pięć liczb.")
else:
    kolekcja = set(tablica)
    wylosowany_element = random.choice(list(kolekcja))
    print(f"Wylosowany element to: {wylosowany_element}")

    if wylosowany_element == min(kolekcja):
        print("Wylosowany element jest najmniejszą z podanych liczb.")
    elif wylosowany_element == max(kolekcja):
        print("Wylosowany element jest największą z podanych liczb.")