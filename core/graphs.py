import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from core.data_loader import load_cities_from_file

class Graphs:
    def __init__(self, frame_left, frame_right):
        self.fig_left = Figure(figsize=(5, 4), dpi=100)
        self.fig_right = Figure(figsize=(5, 4), dpi=100)

        self.ax_left = self.fig_left.add_subplot(111)
        self.ax_right = self.fig_right.add_subplot(111)
        self.x, self.y, self.priority = [], [], []
        self.canvas_left = FigureCanvasTkAgg(self.fig_left, master=frame_left)
        self.canvas_left.get_tk_widget().pack(fill="both", expand=True)
        self.canvas_right = FigureCanvasTkAgg(self.fig_right, master=frame_right)
        self.canvas_right.get_tk_widget().pack(fill="both", expand=True)

    def cities_random(self, ile): # metoda do tworzenia randomnych miast na mapie
        self.ax_left.clear() # wyczyszczamy wykresy
        self.ax_right.clear()

        self.x = np.random.randint(0, 101, size = ile) #generujemy miasta
        self.y = np.random.randint(0, 101, size = ile)
        self.priority = np.random.randint(1, 10, size = ile)

        self.ax_left.scatter(self.x, self.y, color="Blue", s=self.priority)
        self.ax_right.scatter(self.x, self.y, color="Blue", s=self.priority)

        self.ax_left.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_left.set_ylim(min(self.y)-0.5, max(self.y)+0.5)
        self.ax_right.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_right.set_ylim(min(self.y)-0.5, max(self.y)+0.5)

        self.canvas_left.draw() # rysujemy miasta
        self.canvas_right.draw()

        return list(zip(self.x, self.y, self.priority)) # zwracamy listę miast dla algorytmów

    def cities_file(self, list_of_cities): #metoda do tworzenia miast z pliku
        self.x, self.y, self.priority = zip(*list_of_cities)  # rozpakujemy naszą listę koordynat

        self.ax_left.clear()  # wyczyszczamy wykresy
        self.ax_right.clear()

        sizes = [20 + (val * 40) for val in self.priority]  # rozmiar miasta zależy od prioritetu

        self.ax_left.scatter(self.x, self.y, color="Blue", s=sizes)
        self.ax_right.scatter(self.x, self.y, color="Blue", s=sizes)

        self.ax_left.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_left.set_ylim(min(self.y)-0.5, max(self.y)+0.5)
        self.ax_right.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_right.set_ylim(min(self.y)-0.5, max(self.y)+0.5)

        self.canvas_left.draw()  # rysujemy miasta
        self.canvas_right.draw()

        return list(zip(self.x, self.y, self.priority))

    def clear_graphs(self):
        self.ax_left.clear() # wyczyszczamy wykresy
        self.ax_right.clear()

        self.ax_left.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_left.set_ylim(min(self.y)-0.5, max(self.y)+0.5)
        self.ax_right.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_right.set_ylim(min(self.y)-0.5, max(self.y)+0.5)

        self.canvas_left.draw()  # rysujemy czyste wykresy
        self.canvas_right.draw()

    def draw_route_left(self, cities, route): # finalny wykres
        self.ax_left.clear()

        # rysowanie miast
        x = [c[0] for c in cities]
        y = [c[1] for c in cities]
        sizes = [20 + (val * 40) for val in self.priority]
        #self.priority = [c[2] for c in cities]
        self.ax_left.scatter(x, y, color="Blue", s=sizes, zorder=3)

        # rysujemy wszystke linie ze skierowanymi strzałkami
        for i in range(len(route)):
            start_city = cities[route[i]]
            end_city = cities[route[(i + 1) % len(route)]]

            # rysowanie strzałki
            self.ax_left.annotate('',
                                  xy=(end_city[0], end_city[1]),
                                  xytext=(start_city[0], start_city[1]),
                                  arrowprops=dict(arrowstyle="->", color="Green", lw=1.5, mutation_scale=12)
                                  )

        self.ax_left.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_left.set_ylim(min(self.y)-0.5, max(self.y)+0.5)
        self.canvas_left.draw()

    def draw_route_right(self, cities, route): #wykres rysowany co iterację
        self.ax_right.clear()

        # rysowanie miast
        x = [c[0] for c in cities]
        y = [c[1] for c in cities]
        sizes = [20 + (val * 40) for val in self.priority]
        #priority = [c[2] for c in cities]
        self.ax_right.scatter(x, y, color="Blue", s=sizes, zorder=3)

        # rysujemy wszystke linie ze skierowanymi strzałkami
        for i in range(len(route)):
            start_city = cities[route[i]]
            end_city = cities[route[(i + 1) % len(route)]]

            self.ax_right.annotate('',
                                   xy=(end_city[0], end_city[1]),
                                   xytext=(start_city[0], start_city[1]),
                                   arrowprops=dict(arrowstyle="->", color="Red", lw=1, mutation_scale=10, alpha=0.6)
                                   )

        self.ax_right.set_xlim(min(self.x)-0.5, max(self.x)+0.5)
        self.ax_right.set_ylim(min(self.y)-0.5, max(self.y)+0.5)
        self.canvas_right.draw()