import csv
from tkinter import filedialog
# funkcja do ekstrakcji danych z plików
def load_cities_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[
        ("CSV files", "*.csv")])
    if not file_path:
        return None

    cities = [] # lista miast
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None) #skip nagłówka
            for row in reader:
                if len(row) >= 2:
                    x, y = float(row[-2]), float(row[-1]) # x jest przed y
                    cities.append((x,y)) # dodajemy do listy
        return cities

    except Exception as e:
        print("Błąd wczytywania pliku:", e)
        return None
