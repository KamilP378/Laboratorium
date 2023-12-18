imie=input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")
wiek=input("Podaj wiek: ")
#a
print("Witaj", imie)
#b
print("Twój wiek to:", wiek)
#c
inicjały = imie[0] + "." + nazwisko[0]
print("Twoje inicjały to:", inicjały)
#d
łańcuch = imie + nazwisko + wiek
print(łańcuch*5)
#e
łańcuch1 = imie + nazwisko + wiek
łańcuch2 = imie + nazwisko + wiek
łańcuch3 = łańcuch1 + łańcuch2
print(łańcuch3)
#f
łańcuch1 = imie + nazwisko + wiek
łańcuch2 = imie + nazwisko + wiek
połowa1 = łańcuch1[:len(łańcuch1)//2]
połowa2 = łańcuch2[len(łańcuch2)//2:]
łańcuch3 = połowa1 + połowa2
print(łańcuch3)



