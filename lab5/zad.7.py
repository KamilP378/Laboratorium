import random
import math

najnizszy_przedzial =int(input("Podaj najniższy przedział: "))
najwyzszy_przedzial =int(input("Podaj najwyższy przedział: "))

krotka = tuple(random.randint(najnizszy_przedzial, najwyzszy_przedzial) for _ in range(10))

print("Wygenerowana krotka:", krotka)

iloczyn = math.prod(krotka)
srednia_geometryczna = iloczyn ** (1/len(krotka))

print("Średnia geometryczna krotki:", srednia_geometryczna)