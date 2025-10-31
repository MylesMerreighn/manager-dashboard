import tkinter as tk
from tkinter import messagebox
from dashboard_ui import Dashboard

def login(self):
    user = self.username_entry.get()
    pw = self.password_entry.get()

    if user == "admin" and pw == "1234":
        self.root.withdraw()  # hide login
        Dashboard().run()
    else:
        messagebox.showerror("Error", "Invalid credentials")

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Manager Dashboard Login")
        self.root.geometry("350x250")

        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=15)

    def login(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()

        if user == "admin" and pw == "1234":
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def run(self):
        self.root.mainloop()
