import random

# Tworzenie zbiorów X i Y
a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

#a
if 5 in X:
    print("Zbiór X zawiera liczbę 5.")
else:
    print("Zbiór X nie zawiera liczby 5.")

#b
if X.issubset(Y):
    print("Zbiór X jest podzbiorem zbioru Y.")
else:
    print("Zbiór X nie jest podzbiorem zbioru Y.")

#c
if Y.issubset(X):
    print("Zbiór Y jest podzbiorem zbioru X.")
else:
    print("Zbiór Y nie jest podzbiorem zbioru X.")

#d
if X.issuperset(Y):
    print("Zbiór X jest nadzbiorem zbioru Y.")
else:
    print("Zbiór X nie jest nadzbiorem zbioru Y.")

#e
if Y.issuperset(X):
    print("Zbiór Y jest nadzbiorem zbioru X.")
else:
    print("Zbiór Y nie jest nadzbiorem zbioru X.")

#f
suma = X.union(Y)
print("Suma zbiorów X i Y:", suma)

#g
roznica = X.difference(Y)
print("Różnica zbiorów X i Y:", roznica)

#h
roznica2 = Y.difference(X)
print("Różnica zbiorów Y i X:", roznica2)

#i
iloczyn = X.intersection(Y)
print("Iloczyn zbiorów X i Y:", iloczyn)

#j
roznica_symetryczna = X.symmetric_difference(Y)
print("Różnica symetryczna zbiorów X i Y:", roznica_symetryczna)

#k
najwyzszy_element = max(X.union(Y))
print("Najwyższy element w obu zbiorach:", najwyzszy_element)

#l
first_element = X.pop()
Y.add(first_element)
print("Zbiór X po usunięciu pierwszego elementu:", X)
print("Zbiór Y po dodaniu pierwszego elementu:", Y)

#m
Y.update(X)
print("Zbiór Y po skopiowaniu elementów ze zbioru X:", Y)

#n
X.clear()
Y.clear()
print("Zbiór X po wyczysczeniu:", X)
print("Zbiór Y po wyczyszczeniu:", Y)