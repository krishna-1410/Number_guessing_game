import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        header_label = tk.Label(self.root, text="Welcome to the Number Guessing Game!", font=("Arial", 14, "bold"))
        header_label.pack(pady=10)

        instruction_label = tk.Label(self.root, text="Guess a number between 1 and 100", font=("Arial", 12))
        instruction_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.root, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        guess_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess, font=("Arial", 12), bg="#3498db", fg="white")
        guess_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", fg="blue")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", fg="blue")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the correct number {self.number_to_guess} in {self.attempts} attempts!")
                self.reset_game()
                
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()