import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_handler import load_data

class Dashboard:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Dashboard")
        self.root.geometry("800x600")

        self.load_button = tk.Button(self.root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

    def load_csv(self):
        df = load_data()
        if df is not None:
            print(df.head())

    def run(self):
        self.root.mainloop()
