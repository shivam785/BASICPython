# Day 4: Digital Clock (GUI Version)

import tkinter as tk
import time

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x200")
        self.configure(bg="black")

        self.label = tk.Label(
            self,
            font=("Arial", 48, "bold"),
            background="black",
            foreground="lime"
        )
        self.label.pack(anchor="center", expand=True)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    app = DigitalClock()
    app.mainloop()
