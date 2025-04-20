import tkinter as tk
import random

words = ["python", "programming", "hangman", "developer", "algorithm"]
selected_word = random.choice(words)
guessed_letters = set()
wrong_letters = set()
MAX_TRIES = 6

def update_display():
    display = " ".join([letter if letter in guessed_letters else "_" for letter in selected_word])
    word_label.config(text=display)
    wrong_label.config(text="Wrong guesses: " + ", ".join(sorted(wrong_letters)))

    if "_" not in display.replace(" ", ""):
        result_label.config(text="🎉 You win!")
        guess_button.config(state="disabled")
    elif len(wrong_letters) >= MAX_TRIES:
        result_label.config(text=f"💀 You lose! Word was: {selected_word}")
        guess_button.config(state="disabled")

def guess_letter():
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        result_label.config(text="Enter a single letter.")
        return

    if guess in guessed_letters or guess in wrong_letters:
        result_label.config(text="Already guessed.")
        return

    if guess in selected_word:
        guessed_letters.add(guess)
    else:
        wrong_letters.add(guess)

    update_display()

# GUI setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

tk.Label(root, text="Guess a letter:").pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

word_label = tk.Label(root, font=("Arial", 24))
word_label.pack(pady=10)

wrong_label = tk.Label(root, text="Wrong guesses:")
wrong_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

update_display()
root.mainloop()
