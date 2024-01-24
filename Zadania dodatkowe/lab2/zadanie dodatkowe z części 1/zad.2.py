n=int(input("Podaj liczbę studentów: "))
suma_punktow = 0
i = 0

while True:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Liczba punktów powinna być w przedziale od 0 do 100. Spróbuj ponownie.")
        continue
    suma_punktow += punkty
    i += 1
    if i >= n:
        break

srednia = suma_punktow / n

print(f"Średnia liczba punktów w grupie wynosi: {srednia}")