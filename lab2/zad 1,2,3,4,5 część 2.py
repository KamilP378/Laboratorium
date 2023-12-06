#zad1
#a
for i in range(1,101):
    print(i, end=", ")
#b
for i in range(100,-1,-1):
    print(i, end=", ")
#c
for i in range(7,78,7):
    print(i, end=", ")
#d
for i in range(20,-1,-2):
    print(i, end=", ")

#zad2
liczba=int(input("Podaj liczbę gwiazdek: "))

for i in range(3):

    for i in range(liczba):
        print("* ", end="")
    print()

#zad3
#a
liczba=int(input("Podaj liczbę gwiazdek: "))

for i in range(liczba):

    for i in range(i+1):
        print("* ", end="")
    print()

#b
liczba=int(input("Podaj liczbę gwiazdek: "))

for i in range(liczba):

    for j in range(liczba - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()

#zad4
n=int(input("Do którego wyrazu ciągu policzyć?"))
a=int(input("Podaj 1 wyraz ciągu: "))
r=int(input("Podaj różnicę ciągu: "))

koniec=a+(n-1)*r
if(r>0):
    koniec = a + (n - 1) * r + 1
else:
    koniec = a + (n - 1) * r - 1
for i in range(a, koniec+1, r):
    print(i)

#zad5
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

n = int(input("Podaj liczbę naturalną n: "))
wynik = silnia(n)
print(f"Silnia liczby {n} wynosi: {wynik}")