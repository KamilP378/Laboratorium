a=float(input("Podaj wartość a: "))
b=float(input("Podaj wartość b: "))
c=float(input("Podaj wartość c: "))

import math
def poleTrojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Długości boków muszą być większe od zera")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Suma długości dwóch boków musi być większa niż długość trzeciego boku")
        return
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return pole
pole = poleTrojkata(a, b, c)
if pole is not None:
    print("Pole trójkąta wynosi:", pole)