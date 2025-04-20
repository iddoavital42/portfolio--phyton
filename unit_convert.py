import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        value = float(entry.get()) 
        from_unit = from_unit_box.get()
        to_unit = to_unit_box.get()

        if from_unit == to_unit:
            result = value
        elif from_unit == 'Meter' and to_unit == 'Kilometer':
            result = value / 1000
        elif from_unit == 'Kilometer' and to_unit == 'Meter':
            result = value * 1000
        else:
            result = value

        result_label.config(text=f'{result:.2f} {to_unit}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid number')

# GUI setup
root = tk.Tk()
root.title('Unit Converter')

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

entry = ttk.Entry(frame, width=10)
entry.grid(row=0, column=0, padx=5, pady=5)

from_unit_box = ttk.Combobox(frame, values=['Meter', 'Kilometer'], width=10)
from_unit_box.grid(row=0, column=1, padx=5, pady=5)
from_unit_box.set('Meter')

to_unit_box = ttk.Combobox(frame, values=['Meter', 'Kilometer'], width=10)
to_unit_box.grid(row=0, column=2, padx=5, pady=5)
to_unit_box.set('Kilometer')

convert_button = ttk.Button(frame, text='Convert', command=convert)
convert_button.grid(row=0, column=3, padx=5, pady=5)

result_label = ttk.Label(frame, font=('Arial', 16))
result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
