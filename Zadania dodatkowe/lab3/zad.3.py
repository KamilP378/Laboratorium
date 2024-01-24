zdanie = input("Podaj zdanie: ")
nowe_zdanie = ' '.join([slowo[0].upper() + slowo[1:-1] + slowo[-1].upper() for slowo in zdanie.split()])
print("Zdanie, w którym każdy wyraz zaczyna się i kończy wielką literą:", nowe_zdanie)