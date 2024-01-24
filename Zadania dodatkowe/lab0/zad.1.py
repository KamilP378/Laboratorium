a = float(input("Podaj wartość współczynnika a: "))
b = float(input("Podaj wartość współczynnika b: "))

if a == 0 and b == 0:
    print("Równanie tożsamościowe - nieskończenie wiele rozwiązań.")
elif a == 0 and b != 0:
    print("Równanie sprzeczne - brak rozwiązań.")
else:
    x = -b/a
    print(f"Rozwiązanie równania: x = {x}")
