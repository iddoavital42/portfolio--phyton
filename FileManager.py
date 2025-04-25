import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_file():
    path = filedialog.askopenfilename()
    if path:
        os.startfile(path)

def delete_file():
    path = filedialog.askopenfilename()
    if path and messagebox.askyesno("Confirm", f"Delete {os.path.basename(path)}?"):
        try:
            os.remove(path)
            messagebox.showinfo("Success", "File deleted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def rename_file():
    path = filedialog.askopenfilename()
    if path:
        new_name = filedialog.asksaveasfilename(initialdir=os.path.dirname(path))
        if new_name:
            try:
                os.rename(path, new_name)
                messagebox.showinfo("Success", "File renamed.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

def create_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        try:
            with open(path, 'w') as f:
                f.write("")  # קובץ ריק
            messagebox.showinfo("Success", "File created.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def read_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        try:
            with open(path, 'r') as f:
                content = f.read()
            top = tk.Toplevel()
            top.title(f"Reading: {os.path.basename(path)}")
            tk.Text(top, wrap='word', height=20, width=60).insert('1.0', content).pack()
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("File Manager")
root.geometry("300x350")

tk.Button(root, text="📂 Open File", command=open_file).pack(pady=8)
tk.Button(root, text="❌ Delete File", command=delete_file).pack(pady=8)
tk.Button(root, text="✏️ Rename File", command=rename_file).pack(pady=8)
tk.Button(root, text="🆕 Create File", command=create_file).pack(pady=8)
tk.Button(root, text="📖 Read Text File", command=read_file).pack(pady=8)

root.mainloop()
