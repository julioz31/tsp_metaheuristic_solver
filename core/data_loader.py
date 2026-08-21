import csv
import gzip
from pathlib import Path
from tkinter import filedialog
# funkcja do ekstrakcji danych z plików
def load_cities_from_file():
    file_path = Path(filedialog.askopenfilename(filetypes=[
        ("CSV files", "*.csv"), ("TSP files","*.gz")]))
    if not file_path:
        return None

    try:
        cities = []  # lista miast

        if file_path.suffix == ".csv" :
            try:
                with open(file_path, mode='r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader, None)  # skip nagłówka
                    for row in reader:
                        if len(row) >= 2:
                            x, y, priority = float(row[-3]), float(row[-2]), float(row[-1])  # x jest przed y
                            cities.append((x, y, priority))  # dodajemy do listy
                return cities

            except Exception as e:
                print("Błąd wczytywania pliku:", e)
                return None

        elif file_path.suffix == ".gz":
            nodes = {}
            node_section = False
            with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith("NODE_COORD_SECTION"):
                        node_section = True
                        continue
                    if line.startswith("EOF") or line.startswith("TOUR_SECTION"):
                        break
                    if node_section:
                        parts = line.split()
                        node_id = int(parts[0])
                        x = float(parts[1])
                        y = float(parts[2])
                        nodes[node_id] = (x, y)

            for node in nodes:
                x, y = nodes[node]
                priority = 1
                cities.append((x, y, priority))

            return cities

    except Exception as e:
        print("Błąd wczytywania pliku:", e)
        return None

