# Day 2: Number Guessing Game (GUI Version)

import tkinter as tk
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.configure(bg="lightblue")

        self.target = random.randint(1, 100)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Guess a number between 1 and 100", font=("Arial", 14), bg="lightblue")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 16), justify='center')
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit Guess", font=("Arial", 14), command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue")
        self.result_label.pack(pady=20)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < self.target:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text="Correct! You guessed it!")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.mainloop()
