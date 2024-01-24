from datetime import datetime, timedelta
import time

# Użytkownik podaje rok, miesiąc i dzień
rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

# Tworzenie daty
data = datetime(rok, miesiac, dzien)

#a Dzień roku
dzien_roku = data.timetuple().tm_yday
print("Dzień roku:", dzien_roku)

#b Numer tygodnia
numer_tygodnia = data.isocalendar()[1]
print("Numer tygodnia:", numer_tygodnia)

#c Data na 2 tygodnie przed i po
data_przed = data - timedelta(weeks=2)
data_po = data + timedelta(weeks=2)
print("Data na 2 tygodnie przed:", data_przed)
print("Data na 2 tygodnie po:", data_po)

#d Data najbliższej niedzieli
najblizsza_niedziela = data + timedelta(days=(6-data.weekday()+7)%7)
print("Data najbliższej niedzieli:", najblizsza_niedziela)

#e Czas unixowy bieżącej godziny w podanym dniu
czas_unix = time.mktime(data.timetuple())
print("Czas unixowy bieżącej godziny w podanym dniu:", czas_unix)