import math
a=float(input("Podaj długość boku a :"))
b=float(input("Podaj długość boku b :"))
c=float(input("Podaj długość boku c :"))
p=(a+b+c)/2
Połowa_obwodu_trojkata=print("Szukana długość połowy obwodu tego trójkąta to: ", p)
if p-a<=0 or p-b<=0 or p-c<=0:
    print("Pole trójkąta wynosi 0")
else:
    P = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Pole trójkąta wynosi", P)