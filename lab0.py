#Zad3
import random

bok1=int(input("Podaj długość 1 boku prostokąta" ))
print(bok1)
print(type(bok1))

bok2=int(input("Podaj długość 2 boku prostokąta" ))
print(bok2)
print(type(bok2))

poleP=bok1*bok2
obwódP=(bok1+bok2)*2


print(f"Pole prostokąta wynosi: {poleP}")
print(f"Obwód prostokąta wynosi: {obwódP}")


#Zad4

import random
#droga=float((input)"Przebyta droga")
droga=random.randint(1, 100000)
cena=6.5
print(f"Przejechana trasa to: {droga}")
spalanie=float(input("Ile wynosi spalanie ?"))

zużycie=droga*cena/100
koszt=cena*zużycie

print(f"Zużycie wynosi: {zużycie}")
print(f"Koszt wynosi: {koszt}")