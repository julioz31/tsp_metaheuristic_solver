import tkinter as tk
from tkinter import ttk, Button, Toplevel, messagebox
import time
from core.graphs import Graphs
from core.data_loader import load_cities_from_csv
from algorithms.genetic import Genetyczny_alg


class Window(tk.Tk):
    #------------------------------------------------------------
    def add_cities(self):
        try:
            input_value = self.random_gen_entry.get()
            if not input_value:
                print("Pole jest puste.")
                return

            ile = int(input_value)
            if ile > 2000:
                ile = 2000
                self.random_gen_entry.delete(0, tk.END) # wyczysczamy entry
                self.random_gen_entry.insert(0, "2000")

            self.cities = self.graph_manager.cities_random(ile)


        except ValueError:
            from tkinter import messagebox
            messagebox.showwarning("Błąd. Wpisz liczbę całkowitą!")

    def add_cities_file(self):
        cities = load_cities_from_csv() # tu są zwracane miasta z funkcji
        if cities:
            self.cities = self.graph_manager.cities_doc(cities) # przesyłamy do klasy wykresów

            self.random_gen_entry.delete(0, tk.END) # wyczysczamy entry
            self.random_gen_entry.insert(0, str(len(cities)))

    def manual(self):
        new_window = Toplevel(self)
        new_window.title("Manual")
        new_window.geometry("300x200")

        tk.Label(new_window, text="Jedyny akceptowalny typ pliku jest '*.csv'!"
                 , font=("Arial", 11, "bold")).pack()
        tk.Label(new_window, text="Najpierw jest koordynata x, potem y, a na koniec priorytet (od 1 do 10)\n"
                                  "Przykład:\n"
                                  "x,y,priority\n"
                                  "10,20, 1\n"
                                  "50,80, 5\n"
                                  "30,40, 10\n"
                                  "90,10, 3\n"
                                  "75,60, 7\n"
                                  "30,90, 2\n"
                 , font=("Arial", 10)).pack(padx=5, pady=5)

    # parametres for genetic
    def show_gen_param(self):
        for widget in self.params_container.winfo_children():
            widget.destroy()

        self.Population_L = tk.Label(self.params_container, text="Rozmiar populacji: ")
        self.Population_L.pack()
        self.Population_Entry = tk.Entry(self.params_container, width=25)
        self.Population_Entry.pack()
        self.Generation_L = tk.Label(self.params_container, text="Ilość generacji: ")
        self.Generation_L.pack()
        self.Generation_Entry = tk.Entry(self.params_container, width=25)
        self.Generation_Entry.pack()
        self.Mutation_L = tk.Label(self.params_container, text="Prawdopodobieństwo mutacji: ")
        self.Mutation_L.pack()
        self.Mutation_Entry = tk.Entry(self.params_container, width=25)
        self.Mutation_Entry.pack()
        self.Tournament_L = tk.Label(self.params_container, text="Wielkość turnieju: ")
        self.Tournament_L.pack()
        self.Tournament_Entry = tk.Entry(self.params_container, width=25)
        self.Tournament_Entry.pack()
        self.elitism_var = tk.BooleanVar(value=True)
        self.Elitism_Checkbox = tk.Checkbutton(self.params_container, text="Elityzm", variable=self.elitism_var,
                                               bg="#f0f0f0")
        self.Elitism_Checkbox.pack()

    # parametres for ant colony
    def show_ant_param(self):
        for widget in self.params_container.winfo_children():
            widget.destroy()
        tk.Label(self.params_container, text="(Tu się pojawią parametry)", fg="gray", bg="#f0f0f0").pack()

    # parametres for firefly
    def show_firefly_param(self):
        for widget in self.params_container.winfo_children():
            widget.destroy()
        tk.Label(self.params_container, text="(Tu się pojawią parametry)", fg="gray", bg="#f0f0f0").pack()
    #metoda do przełączania parametrów
    def parameters_chooser(self, event):
        chosen = self.algorithm_dropdown.get()

        if chosen == 'Genetyczny':
            self.show_gen_param()
        elif chosen == 'Mrówkowy':
            self.show_ant_param()
        elif chosen == 'Świetlika':
            self.show_firefly_param()
        else:
            print('Błąd')
#------------------------włączenie algorytmów-----------------------------------------------------------------
    def start_algorithm(self):
        if not hasattr(self, 'cities') or not self.cities:
            messagebox.showwarning("Błąd", "Najpierw dodaj lub wgraj miasta!")
            return
        # jeżeli algorytm już działa to nie daje go drugi raz zinicjalizować
        if self.running:
            return
        wybrany_algo = self.algorithm_dropdown.get()

        if wybrany_algo == 'Genetyczny':
            self.ga.dystans_miasta(self.cities)
        elif wybrany_algo == 'Mrówkowy':
            pass # tu dystans dla mrówkowego
        elif wybrany_algo == 'Świetlika':
            pass # tu dla świetlika

        self.running = True
        max_iterations = 100 # domyślnie
        start_time = time.time()
        #pobranie danych dla algorytmu
        if wybrany_algo == 'Genetyczny':
            self.ga.population_size = int(self.Population_Entry.get())
            self.ga.generations = int(self.Generation_Entry.get())
            self.ga.mutation = float(self.Mutation_Entry.get())
            self.ga.tournament_size = int(self.Tournament_Entry.get())
            self.ga.elitism = self.elitism_var.get()

            max_iterations = self.ga.generations
            populacja = self.ga.populacja()

        elif wybrany_algo == 'Mrówkowy':
            pass
        elif wybrany_algo == 'Świetlika':
            pass

        current_best = None
        cur_dist = 0.0
        cur_cost = 0.0

        for idx_gen in range(max_iterations):
            # sprawdzamy czy nie zostałą nacisnięty przycisk STOP
            if not self.running:
                print("Algorytm został zatrzymany przez użytkownika.")
                break

            # wybranie rozwiązania według algorytmu
            if wybrany_algo == 'Genetyczny':
                populacja = self.ga.pokolenie(populacja)
                current_best = min(populacja, key=self.ga.koszt)
                cur_dist = self.ga.total_dystans(current_best)
                cur_cost = self.ga.koszt(current_best)

            elif wybrany_algo == 'Mrówkowy':
                pass

            elif wybrany_algo == 'Świetlika':
                pass

            # animowanie wykresów
            if self.anim_var.get() and current_best is not None:
                krok = self.anim_step_scale.get()
                # rysujemy pierwszą, ostatnią i każdą n iterację
                if idx_gen == 0 or idx_gen == max_iterations - 1 or (idx_gen + 1) % krok == 0:
                    self.graph_manager.draw_route_right(self.cities, current_best)
                    self.update()

            # onowienie logów tekstowych
            self.stats_present_label.config(
                text=f"Iteracja: {idx_gen + 1}\nDystans: {cur_dist:.2f}\nKoszt: {cur_cost:.4f}"
            )

            # final
        end_time = time.time()
        duration = end_time - start_time

        # rysowanie wyniku
        if current_best is not None:
            self.graph_manager.draw_route_left(self.cities, current_best)
            self.stats_best_label.config(
                text=f"Najlepszy Dystans: {cur_dist:.2f}\nNajlepszy koszt: {cur_cost:.4f}\nCzas: {duration:.4f} s"
            )

        # aplikacja zwolniona od wykonania
        self.running = False

    def stop_algorithm(self):
        if self.running:
            self.running = False

    def reset_algorithm(self):
        self.cities = []
        self.random_gen_entry.delete(0, tk.END)
        self.stats_best_label.config(text="Najlepszy Dystans: 0.0\nNajlepszy koszt: 0.0\nCzas: 0.0000 s")
        self.stats_present_label.config(text="Iteracja: 0 \nDystans: 0.0\nKoszt: 0.0")

        # wykasowanie wykresów
        self.graph_manager.clear_graphs()

    # ------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.title("Środowisko testowe TSP")
        self.geometry("1500x900")
        self.running = False
        self.ga = Genetyczny_alg()
        self.cities = []
        #----------------------------------Frame division---------------------------------------------
        self.left_panel = tk.Frame(self, width=300, bg="#f0f0f0", padx=10, pady=10)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)
        self.left_panel.pack_propagate(False)

        self.bottom_panel = tk.Frame(self, bg="#D8D7DE", padx=10, pady=10)
        self.bottom_panel.pack(side=tk.BOTTOM, fill=tk.X)
        self.bottom_panel.columnconfigure(0, weight=1)

        self.right_panel = tk.Frame(self, bg="white", padx=10, pady=10)
        self.right_panel.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        # -------------------------------------------------------------------------------

        # ----------------------------------Frame fulfilling---------------------------------------------
        #Left panel
        tk.Label(self.left_panel, text="Ustawienia Wykresów", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=15)
        #-------------------------------------------------------------------------------------------------------------------
        gen_frame = tk.LabelFrame(self.left_panel, text=" Generacja miast ", font=("Arial", 10, "bold"), bg="#f0f0f0",
                                  padx=10, pady=10)
        gen_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(gen_frame, text="Randomna generacja (max 2000):", bg="#f0f0f0").pack(anchor="w")
        self.random_gen_entry = tk.Entry(gen_frame, width=15)
        self.random_gen_entry.pack(pady=5, fill=tk.X)
        tk.Button(gen_frame, text="Dodać miasta", command=self.add_cities).pack(fill=tk.X)

        tk.Label(gen_frame, text="Operacje z plikami:", bg="#f0f0f0").pack(anchor="w", pady=(10, 0))
        self.file_gen_button = tk.Button(gen_frame, text="Nagrać plik (.csv)", command=self.add_cities_file)
        self.file_gen_button.pack(fill=tk.X, pady=2)
        self.manual_button = tk.Button(gen_frame, text="Przeczytać manual", command=self.manual, font=("Arial", 8, "italic"))
        self.manual_button.pack(anchor="e")
        # -------------------------------------------------------------------------------------------------------------------
        self.algo_frame = tk.LabelFrame(self.left_panel, text=" Ustawienia Algoritmów ", font=("Arial", 10, "bold"),
                                   bg="#f0f0f0", padx=10, pady=10)
        self.algo_frame.pack(fill=tk.X, padx=10, pady=5)

        self.anim_var = tk.BooleanVar(value=True)
        self.anim_checkbox = tk.Checkbutton(self.algo_frame, text="Wizualizacja na żywo", variable=self.anim_var,
                                            bg="#f0f0f0")
        self.anim_checkbox.pack(pady=(10, 0), anchor="w")

        tk.Label(self.algo_frame, text="Krok odświeżania (iteracje):", bg="#f0f0f0").pack(anchor="w", pady=(5, 0))
        self.anim_step_scale = tk.Scale(self.algo_frame, from_=1, to=50, orient=tk.HORIZONTAL, bg="#f0f0f0", resolution=1)
        self.anim_step_scale.set(10)  # domyślnie 10
        self.anim_step_scale.pack(fill=tk.X, pady=5)

        tk.Label(self.algo_frame, text="Wybrany Algorytm:", bg="#f0f0f0").pack(anchor="w")
        self.params_container = tk.Frame(self.algo_frame, bg="#f0f0f0")
        self.algorithm_dropdown = ttk.Combobox(self.algo_frame, values=['Genetyczny', 'Mrówkowy', 'Świetlika'],
                                               state="readonly")
        self.algorithm_dropdown.bind("<<ComboboxSelected>>", self.parameters_chooser)
        self.algorithm_dropdown.pack(pady=5, fill=tk.X)
        self.algorithm_dropdown.current(0)
        self.show_gen_param()


        self.params_container.pack(fill=tk.X, pady=5)

        ctrl_frame = tk.Frame(self.left_panel, bg="#f0f0f0")
        ctrl_frame.pack(fill=tk.X, padx=10, pady=20, side=tk.BOTTOM)  # Przyciski poniżej

        self.start_btn = tk.Button(ctrl_frame, text="START", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=self.start_algorithm)
        self.start_btn.pack(fill=tk.X, pady=2)

        self.stop_btn = tk.Button(ctrl_frame, text="STOP", bg="#F44336", fg="white", font=("Arial", 11, "bold"), command=self.stop_algorithm)
        self.stop_btn.pack(fill=tk.X, pady=2)

        self.reset_btn = tk.Button(ctrl_frame, text="RESET", bg="#2196F3", fg="white", font=("Arial", 11, "bold"), command=self.reset_algorithm)
        self.reset_btn.pack(fill=tk.X, pady=2)

        # Botoom panel
        tk.Label(self.bottom_panel, text="Statystyki & Logi", font=("Arial", 12, "bold"), bg="#D8D7DE").grid(row=0, column=0, padx=40, sticky="s")

        self.stats_container = tk.Frame(self.bottom_panel, bg="#D8D7DE") #container inside bottom panel for text and statistics
        self.stats_container.grid(row=1, column=0, sticky="n")

        self.stats_best_label = tk.Label(self.stats_container, text="Najlepszy Dystans: 0.0\nNajlepszy koszt: 0.0", bg="#D8D7DE",
                                         font=("Arial", 11), justify="right")
        self.stats_best_label.pack(side=tk.LEFT, padx=50)

        self.stats_present_label = tk.Label(self.stats_container, text="Iteracja: 0 \nDystans: 0.0\nKoszt: 0.0", bg="#D8D7DE", font=("Arial", 11), justify="right")
        self.stats_present_label.pack(side=tk.LEFT, padx=50)

        #-------------------------------Wykresy--------------------------------------------------------------
        tk.Label(self.right_panel, text="Wizualizacja wykresów", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

        self.canvas_container = tk.Frame(self.right_panel, bg="white")
        self.canvas_container.pack(expand=True, fill=tk.BOTH)
        # Left graph (the best result)
        self.canvas_left = tk.Frame(self.canvas_container, bg="white")
        self.canvas_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        # Right graph (search animation)
        self.canvas_right = tk.Frame(self.canvas_container, bg="white")
        self.canvas_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.graph_manager = Graphs(self.canvas_left, self.canvas_right)  # klasa do wykresów
        #-------------------------------------------------------------------------------





app = Window()
app.mainloop()
