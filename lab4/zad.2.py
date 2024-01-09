a=float(input("Podaj długość a: "))
b=float(input("Podaj długość b: "))
h=float(input("Podaj wysokość: "))
def poleTrapezu(a, b, h):
    if h > 0:
        pole = (((a+b)*h)/2)
        return pole
    else:
        print("Ten trapez nie istnieje")
Pole=poleTrapezu(a, b, h)
print("Pole trapezu wynosi:",Pole)