import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TSP Metaheuristic Solver")
        self.geometry("1500x900")
        #----------------------------------Frame division---------------------------------------------
        self.left_panel = tk.Frame(self, width=250, bg="#f0f0f0", padx=100, pady=10)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.bottom_panel = tk.Frame(self, width=1500, height=250, bg="#D8D7DE", padx=100, pady=800)
        self.bottom_panel.pack(side=tk.BOTTOM, fill=tk.Y)

        self.right_panel = tk.Frame(self, width=1250, height=650, bg="white", padx=10, pady=10)
        self.right_panel.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        # -------------------------------------------------------------------------------

        # ----------------------------------Frame fulfilling---------------------------------------------
        #Left panel
        tk.Label(self.left_panel, text="Canvas Settings", font=("Arial", 12, "bold")).pack(pady=5)





        # Botoom panel
        #tk.Label(self.bottom_panel, text="Statistics", font=("Arial", 12, "bold")).pack()





        # Right panel
        tk.Label(self.right_panel, text="Graphs", font=("Arial", 12, "bold")).pack(pady=5)
        #tk.Label(self.bottom_panel, text="The best", font=("Arial", 10, "bold")).pack(pady=5)
        # tk.Label(self.bottom_panel, text="Present", font=("Arial", 10, "bold")).pack(pady=5)



app = Window()
app.mainloop()
