waga=float(input("Podaj swoją wagę w kilogramach: "))
wzrost=float(input("Podaj swój wzrost w metrach: "))

def obliczanie_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    if 18.5 <= bmi <= 24.99:
        print("Twoje BMI jest prawidłowe.")
    elif bmi < 18.5:
        print("Jesteś niedożywiony.")
    else:
        print("Masz nadwagę.")

obliczanie_bmi(waga, wzrost)  #wywołanie funkcji