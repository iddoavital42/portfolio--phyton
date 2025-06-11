import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "budget_data.json"

class BudgetPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Planner")
        self.root.geometry("500x300")

        self.amount_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.category_var = tk.StringVar(value="Income")

        self.create_widgets()
        self.load_data()
        self.update_summary()

    def create_widgets(self):
        tk.Label(self.root, text="Amount:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1)

        tk.Label(self.root, text="Description:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.desc_var).grid(row=1, column=1)

        tk.Label(self.root, text="Category:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.category_var).grid(row=2, column=1)

        tk.Button(self.root, text="Add Entry", command=self.add_entry).grid(row=3, column=0, columnspan=2, pady=10)

        self.summary_label = tk.Label(self.root, text="", fg="blue")
        self.summary_label.grid(row=4, column=0, columnspan=2)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_entry(self):
        try:
            amount = float(self.amount_var.get())
            desc = self.desc_var.get()
            category = self.category_var.get()

            entry = {"amount": amount, "description": desc, "category": category}
            self.data.append(entry)
            self.save_data()

            self.amount_var.set("")
            self.desc_var.set("")
            self.category_var.set("Income")

            self.update_summary()
            messagebox.showinfo("Success", "Entry added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_summary(self):
        income = sum(e["amount"] for e in self.data if e["category"].lower() == "income")
        expense = sum(e["amount"] for e in self.data if e["category"].lower() != "income")
        balance = income - expense

        self.summary_label.config(text=f"Income: ₪{income:.2f} | Expenses: ₪{expense:.2f} | Balance: ₪{balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPlannerApp(root)
    root.mainloop()
