# Day 1: Calculator App (GUI Version)
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("300x400")
        self.configure(bg="white")
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.display.pack(expand=True, fill='both')

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            frame = tk.Frame(self, bg="white")
            frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(
                    frame, text=btn_text, font=("Arial", 18),
                    bd=5, relief=tk.RAISED, command=lambda text=btn_text: self.on_button_click(text)
                )
                btn.pack(side='left', expand=True, fill='both')

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
