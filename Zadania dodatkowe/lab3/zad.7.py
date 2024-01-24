import random
import string

n=int(input("Podaj liczbę n: "))
x=int(input("Podaj liczbę x: "))

lista = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, x))) for _ in range(n)]
print("Lista:", lista)

#a
ilosc_znakow = sum(len(ciag) for ciag in lista)
print("Ilość znaków w liście:", ilosc_znakow)

#b
ilosc_k = sum(ciag.count('k') for ciag in lista)
print("Ilość liter 'k' w liście:", ilosc_k)

#c
ilosc_kt=sum(ciag.count('kt') for ciag in lista)
print("Ilość ciągów znaków 'kt' w liście:", ilosc_kt)

#d
s=int(input("Podaj liczbę s: "))
ilosc_dluzszych=sum(1 for ciag in lista if len(ciag) > s)
print("Ilość ciągów znaków dłuższych niż", s, "w liście:", ilosc_dluzszych)

#e
nowa_lista = ['a' + ciag + 'z' for ciag in lista]
print("Nowa lista:", nowa_lista)