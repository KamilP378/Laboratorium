lista_zakupow = {
    'jabłka': 5.50,
    'chleb': 2.20,
    'masło': 6.80,
    'jajka': 12.00,
    'mleko': 2.50
}
print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(artykul + " : " +str(kwota))

suma_wydatkow = sum(lista_zakupow.values())

print("Podsumowanie wydatków:")
print("Łączna kwota: " + str(suma_wydatkow))