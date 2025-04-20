import tkinter as tk
from tkinter import messagebox

clients = []

 
def update_list():
    listbox.delete(0, tk.END)
    for c in clients:
        listbox.insert(tk.END, f"{c['name']} | {c['phone']} | {c['email']}")

 
def add_client():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not phone or not email:
        messagebox.showwarning("Missing info", "Please fill all fields.")
        return

    clients.append({"name": name, "phone": phone, "email": email})
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    update_list()
 
def delete_selected():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        del clients[index]
        update_list()

 
root = tk.Tk()
root.title("Client Manager")
root.geometry("450x500")

tk.Label(root, text="📋 Client Management", font=("Arial", 18)).pack(pady=10)

 
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="e")
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

 
tk.Button(root, text="➕ Add Client", command=add_client, bg="#4CAF50", fg="white").pack(pady=10)

 
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

 
tk.Button(root, text="❌ Delete Selected", command=delete_selected, bg="#f44336", fg="white").pack()

 
root.mainloop()
