import tkinter as tk
from tkinter import messagebox
from collections import Counter

def analyze_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Missing text", "Please enter some text to analyze.")
        return  # חשוב! לעצור אם אין טקסט

    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    num_lines = text.count("\n") + 1
    most_common = Counter(words).most_common(1)[0][0] if words else "N/A"
    avg_word_length = sum(len(w) for w in words) / num_words if num_words > 0 else 0

    result = (
        f"Number of words: {num_words}\n"
        f"Number of characters: {num_chars}\n"
        f"Number of lines: {num_lines}\n"
        f"Most common word: {most_common}\n"
        f"Average word length: {avg_word_length:.2f}"
    )
    result_label.config(text=result)

# ⬇️ יצירת ממשק גרפי (GUI)
root = tk.Tk()
root.title("Text Analyzer")
root.geometry("400x400")

tk.Label(root, text="Enter your text:").pack(pady=5)
text_input = tk.Text(root, height=10, width=40)
text_input.pack()

tk.Button(root, text="Analyze Text", command=analyze_text).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()
