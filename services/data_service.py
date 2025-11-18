import pandas as pd
from tkinter import filedialog

def load_data():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        df = pd.read_csv(file_path)
        return df
    else:
        return None
