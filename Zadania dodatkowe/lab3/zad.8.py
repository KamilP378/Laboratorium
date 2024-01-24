import string
alfabet = list(string.ascii_lowercase)

n=int(input("Podaj liczbę n: "))

podlisty=[alfabet[i:i+n] for i in range(0, len(alfabet), n)]

print("Podlisty:", podlisty)