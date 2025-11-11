import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors Game")
        self.geometry("400x400")
        self.configure(bg="lightblue")

        self.choices = ["Rock", "Paper", "Scissors"]
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Rock-Paper-Scissors Game", font=("Arial", 18), bg="lightblue")
        self.label.pack(pady=10)

        self.instructions = tk.Label(self, text="Choose your move!", font=("Arial", 14), bg="lightblue")
        self.instructions.pack(pady=5)

        self.rock_button = tk.Button(self, text="Rock", font=("Arial", 14), width=15, command=lambda: self.play_game("Rock"))
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(self, text="Paper", font=("Arial", 14), width=15, command=lambda: self.play_game("Paper"))
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(self, text="Scissors", font=("Arial", 14), width=15, command=lambda: self.play_game("Scissors"))
        self.scissors_button.pack(pady=10)

        self.result_label = tk.Label(self, text="Result: ", font=("Arial", 14), bg="lightblue")
        self.result_label.pack(pady=20)

    def play_game(self, player_choice):
        # Get the computer's choice
        computer_choice = random.choice(self.choices)

        # Determine the result
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You Win! {player_choice} beats {computer_choice}"
        else:
            result = f"You Lose! {computer_choice} beats {player_choice}"

        # Show the result in a message box
        messagebox.showinfo("Game Over", f"Player: {player_choice}\nComputer: {computer_choice}\n{result}")

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()
