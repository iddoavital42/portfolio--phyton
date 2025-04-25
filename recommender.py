import tkinter as tk
from tkinter import messagebox
import json

# בסיס נתונים של המלצות
database = {
    "movies": ["Inception", "The Matrix", "Interstellar"],
    "books": ["Atomic Habits", "Deep Work", "The Alchemist"],
    "recipes": ["Spaghetti Bolognese", "Chicken Curry", "Avocado Toast"]
}

# פונקציית המלצה
def get_recommendations(interests):
    recommendations = {}
    for interest in interests:
        interest = interest.lower()
        if interest in database:
            recommendations[interest] = database[interest]
        else:
            recommendations[interest] = ["No results found."]
    return recommendations

# פונקציה להצגת תוצאות
def show_results():
    raw_input = entry.get().strip()
    if not raw_input:
        messagebox.showwarning("Missing input", "Please enter at least one interest.")
        return

    interests = [i.strip().lower() for i in raw_input.split(",")]
    results = get_recommendations(interests)

    result_text.delete("1.0", tk.END)
    for category, items in results.items():
        result_text.insert(tk.END, f"\n📚 {category.capitalize()}:\n")
        for item in items:
            result_text.insert(tk.END, f"  - {item}\n")

    save_to_file(results)

# פונקציית שמירה לקובץ
def save_to_file(data):
    with open("recommendations.json", "w") as f:
        json.dump(data, f, indent=4)

# GUI
root = tk.Tk()
root.title("🎯 Personal Recommender")
root.geometry("500x450")

tk.Label(root, text="Enter interests (e.g., movies, books):").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Get Recommendations", command=show_results, bg="#4CAF50", fg="white").pack(pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()
