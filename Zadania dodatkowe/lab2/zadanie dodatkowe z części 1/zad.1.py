n=int(input("Podaj liczbę studentów: "))
suma_punktow = 0

i = 0

while i < n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
    suma_punktow += punkty
    i += 1

srednia = suma_punktow / n

print(f"Średnia liczba punktów w grupie wynosi: {srednia}")