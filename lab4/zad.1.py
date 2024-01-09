def poleKola(r):
    if r > 0:
        pole = (r*r*3.14)
        return pole
    else:
        print("Koło nie istnieje - nie można obliczyć")
print(poleKola(2))