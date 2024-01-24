#a
imie=input("Podaj imię :")
print("Witaj", imie)
#b
wiek=int(input("Podaj wiek :"))
print("Twój wiek to:", wiek)
#c
nazwisko=input("Podaj nazwisko :")
inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały to:", inicjaly)
#d
print(inicjaly*5)
#e
łańcuch1 = imie + nazwisko
łańcuch2 = imie + nazwisko
łańcuch3 = łańcuch1 + łańcuch2
print(łańcuch3)
#f
łańcuch1 = imie + nazwisko
łańcuch2 = imie + nazwisko
połowa1 = łańcuch1[:len(łańcuch1)//2]
połowa2 = łańcuch2[len(łańcuch2)//2:]
łańcuch3 = połowa1 + połowa2
print(łańcuch3)
