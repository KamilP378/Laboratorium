zdanie=input("Podaj zdanie: ")

def zamien_litery(zdanie):
    nowe_zdanie = ""
    for litera in zdanie:
        if litera.islower():
            nowe_zdanie += litera.upper()
        else:
            nowe_zdanie += litera.lower()
    return nowe_zdanie

Zamienione_zdanie = zamien_litery(zdanie)

print("Zdanie po zamianie: ", Zamienione_zdanie)