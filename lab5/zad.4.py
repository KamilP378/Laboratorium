from datetime import datetime
import locale

# Ustawienie lokalizacji na polską
locale.setlocale(locale.LC_TIME, "pl_PL")

# Data ostatnich laboratoriów
data_laboratoriow = datetime(2023, 12, 10)

# Data kolokwium
data_kolokwium = datetime(2024, 2, 11)

# Obecna data
obecna_data = datetime.now()

# Obliczanie różnicy dni
dni_od_laboratoriow = (obecna_data - data_laboratoriow).days
dni_do_kolokwium = (data_kolokwium - obecna_data).days

print(f"Od ostatnich laboratoriów minęło {dni_od_laboratoriow} dni.")
print(f"Do kolokwium pozostało {dni_do_kolokwium} dni.")
print(f"Obecna data to {obecna_data.strftime('%d %B %Y')}.")