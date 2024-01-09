a=float(input("Podaj liczbę a: "))
n=int(input("Podaj potęge,do której podnieść liczbę:"))
def potega(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return potega(a, n/2) ** 2
    else:
        return a * potega(a, n-1)

print(potega(a, n))