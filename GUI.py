import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TSP Metaheuristic Solver")
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
        tk.Label(self.left_panel, text="Canvas Settings", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)




        # Botoom panel
        tk.Label(self.bottom_panel, text="Statistics & Logs", font=("Arial", 12, "bold"), bg="#D8D7DE").grid(row=0, column=0, padx=40, sticky="s")
        self.stats_container = tk.Frame(self.bottom_panel, bg="#D8D7DE") #container inside bottom panel for text and statistics
        self.stats_container.grid(row=1, column=0, sticky="n")
        self.stats_best_label = tk.Label(self.stats_container, text="Best Distance: 0.0\nBest cost: 0.0", bg="#D8D7DE",
                                         font=("Arial", 11), justify="right")
        self.stats_best_label.pack(side=tk.LEFT, padx=50)

        self.stats_present_label = tk.Label(self.stats_container, text="Iteration: 0 \nDistance: 0.0\nCost: 0.0", bg="#D8D7DE", font=("Arial", 11), justify="right")
        self.stats_present_label.pack(side=tk.LEFT, padx=50)

        # Right panel
        tk.Label(self.right_panel, text="Graphs Visualization", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

        self.canvas_container = tk.Frame(self.right_panel, bg="white")
        self.canvas_container.pack(expand=True, fill=tk.BOTH)

        # Left graph (the best result)
        self.canvas_left = tk.Canvas(self.canvas_container, bg="#FAFAFA", highlightthickness=1,
                                     highlightbackground="#CCCCCC")
        self.canvas_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Right graph (search animation)
        self.canvas_right = tk.Canvas(self.canvas_container, bg="#FAFAFA", highlightthickness=1,
                                      highlightbackground="#CCCCCC")
        self.canvas_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        # -------------------------------------------------------------------------------





app = Window()
app.mainloop()
