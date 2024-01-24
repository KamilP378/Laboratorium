import math

a=float(input("Podaj długość boku a: "))
b=float(input("Podaj długość boku b: "))
kat=int(input("Podaj miarę kąta: "))
def pole_trojkata(a, b, kat):
    if a <= 0 or b <= 0 or kat <= 0 or kat >= 180:
        return "Trójkąt nie istnieje."
    if kat >= 90:
        return "Trójkąt nie jest ostrokątny."

    kat_rad = math.radians(kat)
    pole = 0.5 * a * b * math.sin(kat_rad)
    return pole
print("Pole trójkąta:", pole_trojkata(a, b, kat))