import random

n = int(input("Ile elementów powinna mieć lista?: "))
x = int(input("Ile znaków ma się znależć w łańcuchu?: "))

lista = []
k = 0
kt = 0

for _ in range(n):
    słowo = ""
    for _ in range(random.randint(1, x)):
        słowo += chr(random.randint(65, 90))
    lista.append(słowo)

print("Lista: ", lista)

krotka = tuple(lista)
print("Krotka: ", krotka)

#a
znaki = sum(len(s) for s in krotka)
print("Ilość znaków w liście: ", znaki)

#b
for s in lista:
    k += s.count('K')
print("Ilość liter 'K': ", k)
#c
for s in lista:
    kt += s.count('KT')
print("Ilość ciągów znaków 'KT': ", kt)

#d
s = int(input("Podaj wartość s: "))
dlugie = sum(1 for _ in filter(lambda x: len(x) > s, krotka))
print("Ilość ciągów znaków dłuższych niż s: ", dlugie)
