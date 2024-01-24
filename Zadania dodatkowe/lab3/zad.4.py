ciag = input("Wprowadź ciąg znaków: ")
wynik = ''
for znak in ciag:
  if ciag.count(znak) > 1:
    wynik += '@'
  else:
    wynik += znak
print("Wynik: ", wynik)
