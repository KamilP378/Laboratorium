n=int(input("Podaj liczbę n: "))
def fibonacci(n):
    if n <= 0:
        return "Błąd: n musi być liczbą dodatnią."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

wyraz_ciągu_fibonacciego=fibonacci(n)
print("Wynik: ", wyraz_ciągu_fibonacciego)