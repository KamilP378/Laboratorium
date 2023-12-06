#zad1
a=int(input("Podaj 1 liczbę: "))
b=int(input("Podaj 2 liczbę: "))
if a>b:
    while b<=a:
        print(b)
        b+=1
elif a==b:
    print("Liczby są równe: ", a)
else:
    while a <= b:
        print(a)
        a +=1

#zad2
def funkcja_y(x):
    return 2*x**2 - 5*x - 8

x = -4.0
krok = 0.5

while x <= 4.0:
    y = funkcja_y(x)
    print("y =", y, "dla x =", x)
    x += krok

#zad3
while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        break

#zad4
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))

if a > b:
    while b <= a:
        if b % 2 == 0:
            print(b)
        b += 1
elif a == b:
    if a % 2 == 0:
        print("Liczby są równe: ", a)
else:
    while a <= b:
        if a % 2 == 0:
            print(a)
        a += 1
