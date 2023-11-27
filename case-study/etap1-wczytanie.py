import pandas as pd
import glob

# jezeli mamy w jednym miejscu pliki csv
dane_csv = glob.glob("../data/*.csv")

# wczytujemy pliki csv do listy
dane = [pd.read_csv(file, skiprows=1, sep=";", decimal=",", names=["kod", "nazwa", "wsk", "rok", "wartosc", "jednostka", "atrybut"], na_values="-", dtype={"kod": str, "nazwa": str, "wsk": str, "rok": int, "wartosc": float, "jednostka": str, "atrybut": str}) for file in dane_csv]

# laczymy zbiory danych w jeden
dane_all = pd.concat(dane, ignore_index=True)

# zamieniamy poziomy zmiennej
dane_all["wsk2"] = dane_all["wsk"].map({
  "przeciętna powierzchnia użytkowa 1 mieszkania": "mieszk_powuz_1m", 
  "przeciętna powierzchnia użytkowa mieszkania na 1 osobę": "mieszk_powuz_1os", 
  "mieszkania na 1000 mieszkańców": "mieszk_na_1000k", 
  "przeciętna liczba izb w 1 mieszkaniu": "mieszk_izb_1m", 
  "przeciętna liczba osób na 1 mieszkanie": "mieszk_osob_1m", 
  "przeciętna liczba osób na 1 izbę": "mieszk_osob_1i", 
  "ludność w wieku poprodukcyjnym na 100 osób w wieku produkcyjnym": "ludn_poprod_1000prod", 
  "współczynnik obciążenia demograficznego osobami starszymi": "ludn_wsk_obciazenia", 
  "w wieku przedprodukcyjnym": "ludn_udz_prze", 
  "w wieku produkcyjnym": "ludn_udz_prod", 
  "udział powierzchni terenów zieleni w powierzchni ogółem": "zielen_pow", 
  "liczba nasadzeń drzew i krzewów w zadrzewieniach oraz terenach zieleni na 1 km2 powierzchni danej jednostki terytorialnej": "zielen_nasadzenia"})

# tworzymy szeroka ramke danych
dane_all_wide = dane_all.pivot(index=["kod", "nazwa", "rok"], columns="wsk2", values="wartosc").reset_index()

# Print the summary statistics of the dataframe
dane_all_wide.describe()
