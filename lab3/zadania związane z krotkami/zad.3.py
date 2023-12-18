rachunki_za_prąd = {
    'maj': 459.59,
    'czerwiec': 490.45,
    'lipiec': 500.54,
    'sierpień': 390.56,
    'wrzesień': 467.21
}
#a
wartosci = list(rachunki_za_prąd.values())
maksimum = max(wartosci)
minimum = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)
#b
ostatni_miesiac = wartosci[-1]
if ostatni_miesiac > srednia:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")