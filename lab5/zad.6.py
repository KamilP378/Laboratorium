import math
import keyword

print("Funkcje w module math:")
for name in dir(math):
    if callable(getattr(math, name)):
        print(name)

print("\nMetody dla obiektu typu tuple:")
for name in dir(tuple):
    if callable(getattr(tuple, name)):
        print(name)

print("\nFunkcje w module keyword:")
for name in dir(keyword):
    if callable(getattr(keyword, name)):
        print(name)