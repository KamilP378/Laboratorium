import random
#a
print("Szczęśliwy numerek to: ", random.randint(1, 11))
#b
Szczęśliwy_rocznik= [1994, 1998, 2001, 2002, 2003, 2004]
print("Szczęśliwy rocznik to: ", random.choice(Szczęśliwy_rocznik))
#c
Szczęśliwe_kule= random.sample(range(1, 50),6)
print("Szczęśliwe kule to: ", Szczęśliwe_kule)
