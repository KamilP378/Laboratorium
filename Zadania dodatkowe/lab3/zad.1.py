zdanie = input("Podaj zdanie: ")
litery = sorted([litera for litera in zdanie.lower() if litera.isalpha()])
print("Litery w kolejności alfabetycznej:", ''.join(litery))
brakujace_litery = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in litery]
print("Brakujące litery:", ''.join(brakujace_litery))