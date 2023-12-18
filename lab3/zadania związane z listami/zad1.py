Lista=["Adam", "Kamil", "Michał", "Agnieszka"]
#a
Lista.sort()
print(Lista)
#b
Lista.append("Basia")
Lista.append("Adrian")
ostatniaOsoba=Lista.pop()
print(ostatniaOsoba)
#c
Lista.insert(2, "Ola")
print(Lista)
#d
Lista.reverse()
listaZdublowana=Lista*2
for name in listaZdublowana:
    print(name)