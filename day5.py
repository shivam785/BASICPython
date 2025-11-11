import tkinter as tk
import random

class DiceRollerGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎲 Rolling the Dices Game")
        self.geometry("600x400")
        self.configure(bg="#121212")
        self.resizable(False, False)

        self.dice_faces = ['\u2680', '\u2681', '\u2682',
                           '\u2683', '\u2684', '\u2685']
        self.rolling = False

        self.build_ui()

    def build_ui(self):
        # Title Label
        self.title_label = tk.Label(
            self,
            text="🎯 Roll the Dice!",
            font=("Helvetica", 24, "bold"),
            fg="aqua",
            bg="#121212"
        )
        self.title_label.pack(pady=20)

        # Dice Display
        self.dice_label = tk.Label(
            self,
            text="\u2680\u2680",
            font=("Helvetica", 150),
            bg="#121212",
            fg="yellow"
        )
        self.dice_label.pack(pady=10)

        # Roll Button
        self.roll_button = tk.Button(
            self,
            text="Roll 🎲",
            font=("Helvetica", 16, "bold"),
            bg="#00FFFF",
            fg="black",
            activebackground="cyan",
            relief="raised",
            bd=4,
            padx=20,
            pady=10,
            command=self.start_rolling
        )
        self.roll_button.pack(pady=20)

    def start_rolling(self):
        if not self.rolling:
            self.rolling = True
            self.animate_roll(10)

    def animate_roll(self, remaining):
        if remaining > 0:
            roll1 = random.choice(self.dice_faces)
            roll2 = random.choice(self.dice_faces)
            self.dice_label.config(text=f"{roll1}{roll2}")
            self.after(100, lambda: self.animate_roll(remaining - 1))
        else:
            # Final result
            final_roll = f"{random.choice(self.dice_faces)}{random.choice(self.dice_faces)}"
            self.dice_label.config(text=final_roll)
            self.rolling = False

if __name__ == "__main__":
    app = DiceRollerGame()
    app.mainloop()
