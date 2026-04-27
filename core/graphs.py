import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Graphs:
    def __init__(self, frame_left, frame_right):
        self.fig_left = Figure(figsize=(5, 4), dpi=100)
        self.fig_right = Figure(figsize=(5, 4), dpi=100)

        self.ax_left = self.fig_left.add_subplot(111)
        self.ax_right = self.fig_right.add_subplot(111)
        self.ax_left.set_xlim(0, 100)
        self.ax_left.set_ylim(0, 100)
        self.ax_right.set_xlim(0, 100)
        self.ax_right.set_ylim(0, 100)

        self.canvas_left = FigureCanvasTkAgg(self.fig_left, master = frame_left)
        self.canvas_left.get_tk_widget().pack(fill = "both", expand=True)
        self.canvas_right = FigureCanvasTkAgg(self.fig_right, master=frame_right)
        self.canvas_right.get_tk_widget().pack(fill="both", expand=True)

    def cities_random(self, ile): # metoda do tworzenia randomnych miast na mapie
        self.ax_left.clear() # wyczyszczamy wykresy
        self.ax_right.clear()

        x = np.random.randint(0, 101, size = ile) #generujemy miasta
        y = np.random.randint(0, 101, size = ile)

        self.ax_left.scatter(x, y, color="Blue", s=30)
        self.ax_right.scatter(x, y, color="Blue", s=30)

        self.ax_left.set_xlim(0, 100)
        self.ax_left.set_ylim(0, 100)
        self.ax_right.set_xlim(0, 100)
        self.ax_right.set_ylim(0, 100)

        self.canvas_left.draw() # rysujemy miasta
        self.canvas_right.draw()

        return list(zip(x, y)) # zwracamy listę miast dla algorytmów

    def cities_doc(self): #metoda do tworzenia miast z pliku
        pass

    def animation(self):
        pass