import tkinter as tk
from tkinter import ttk, Button
from core.graphs import Graphs

class Window(tk.Tk):
    def add_cities(self):
        try:
            input_value = self.random_gen_entry.get()
            if not input_value:
                print("Pole jest puste.")
                return

            ile = int(input_value)
            if ile > 2000:
                ile = 2000
                self.random_gen_entry.delete(0, tk.END)
                self.random_gen_entry.insert(0, "2000")

            self.graph_manager.cities_random(ile)

        except ValueError:
            from tkinter import messagebox
            messagebox.showwarning("Błąd. Wpisz liczbę całkowitą!")

    def __init__(self):
        super().__init__()
        self.title("Środowisko testowe TSP")
        self.geometry("1500x900")
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
        self.file_gen_button = tk.Button(gen_frame, text="Nagrać plik (.csv/.txt)")
        self.file_gen_button.pack(fill=tk.X, pady=2)
        self.manual_button = tk.Button(gen_frame, text="Przeczytać manual", font=("Arial", 8, "italic"))
        self.manual_button.pack(anchor="e")
        # -------------------------------------------------------------------------------------------------------------------
        algo_frame = tk.LabelFrame(self.left_panel, text=" Ustawienia Algoritmów ", font=("Arial", 10, "bold"),
                                   bg="#f0f0f0", padx=10, pady=10)
        algo_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(algo_frame, text="Wybrany Algorytm:", bg="#f0f0f0").pack(anchor="w")
        self.algorithm_dropdown = ttk.Combobox(algo_frame, values=['Genetyczny', 'Mrówkowy', 'Świetlika'],
                                               state="readonly")
        self.algorithm_dropdown.pack(pady=5, fill=tk.X)
        self.algorithm_dropdown.current(0)

        self.params_container = tk.Frame(algo_frame, bg="#f0f0f0")
        self.params_container.pack(fill=tk.X, pady=5)
        tk.Label(self.params_container, text="(Tu się pojawią parametry)", fg="gray", bg="#f0f0f0").pack()
        # -------------------------------------------------------------------------------------------------------------------
        #tk.Label(self.left_panel, text="Parameters: ", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(pady=5)
        #parametres for genetec
        # -------------------------------------------------------------------------------------------------------------------
        # parametres for ant colony
        # -------------------------------------------------------------------------------------------------------------------
        # parametres for firefly
        # -------------------------------------------------------------------------------------------------------------------
        ctrl_frame = tk.Frame(self.left_panel, bg="#f0f0f0")
        ctrl_frame.pack(fill=tk.X, padx=10, pady=20, side=tk.BOTTOM)  # Кнопки внизу

        self.start_btn = tk.Button(ctrl_frame, text="START", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        self.start_btn.pack(fill=tk.X, pady=2)

        self.stop_btn = tk.Button(ctrl_frame, text="STOP", bg="#F44336", fg="white", font=("Arial", 11, "bold"))
        self.stop_btn.pack(fill=tk.X, pady=2)

        self.reset_btn = tk.Button(ctrl_frame, text="RESET", bg="#2196F3", fg="white", font=("Arial", 11, "bold"))
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
