autobus=input("Czy jest autobus ?  (tak/nie)")
deszcz=input("Czy pada deszcz ? (tak/nie)")
if deszcz == "tak" and autobus == "tak":
    print("Weź parasol")
    print("Dostaniesz się na uczelnie")
elif deszcz == "tak" and autobus == "nie":
    print("Nie dostaniesz się na uczelnię")
elif deszcz == "nie" and autobus == "tak":
    print("Dostaniesz się na uczelnię")
    print("Miłego dnia i pięknej pogody")