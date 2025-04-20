import json
import os
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "shopping_list.json"

# Load & Save
def load_list():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_list(shopping_list):
    with open(FILE_NAME, "w") as f:
        json.dump(shopping_list, f, indent=4)

# GUI Functions
def update_listbox():
    listbox.delete(0, tk.END)
    for item in shopping_list:
        status = "✅" if item["bought"] else "❌"
        listbox.insert(tk.END, f"{item['name']} x{item['quantity']} {status}")

def add_item():
    name = name_entry.get()
    quantity = quantity_entry.get()
    if name and quantity:
        shopping_list.append({"name": name, "quantity": quantity, "bought": False})
        save_list(shopping_list)
        update_listbox()
        name_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing data", "Please enter both name and quantity.")

def mark_as_bought():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        shopping_list[index]["bought"] = True
        save_list(shopping_list)
        update_listbox()
    else:
        messagebox.showinfo("Select item", "Please select an item to mark as bought.")

def delete_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        item = shopping_list.pop(index)
        save_list(shopping_list)
        update_listbox()
        messagebox.showinfo("Deleted", f"Deleted item: {item['name']}")
    else:
        messagebox.showinfo("Select item", "Please select an item to delete.")

# Load data
shopping_list = load_list()

# GUI Setup
root = tk.Tk()
root.title("Shopping List")
root.geometry("400x400")

tk.Label(root, text="Item Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Quantity:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)
tk.Button(root, text="Mark as Bought", command=mark_as_bought).pack()
tk.Button(root, text="Delete Item", command=delete_item).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

update_listbox()

root.mainloop()
