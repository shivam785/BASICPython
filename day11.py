import tkinter as tk
from tkinter import ttk, messagebox

# Unit conversion logic
conversion_factors = {
    'Length': {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'feet': 3.28084,
        'inches': 39.3701,
    },
    'Weight': {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274,
    },
    'Temperature': {
        'celsius': 'temp',
        'fahrenheit': 'temp',
        'kelvin': 'temp',
    }
}

# Helper for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

# GUI
class UnitConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("600x400")
        self.configure(bg="#fff9c4")  # light yellow

        self.categories = list(conversion_factors.keys())
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Unit Converter", font=("Arial", 22, "bold"), bg="black", fg="yellow").pack(pady=20)

        # Category dropdown
        frame = tk.Frame(self, bg="#fff9c4")
        frame.pack()

        tk.Label(frame, text="Category:", font=("Arial", 14), bg="#fff9c4").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.category_var = tk.StringVar(value="Length")
        self.category_menu = ttk.Combobox(frame, textvariable=self.category_var, values=self.categories, state='readonly')
        self.category_menu.grid(row=0, column=1, pady=5)
        self.category_menu.bind('<<ComboboxSelected>>', self.update_units)

        # From / To unit dropdowns
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()

        tk.Label(frame, text="From:", font=("Arial", 14), bg="#fff9c4").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.from_unit_menu = ttk.Combobox(frame, textvariable=self.from_unit_var)
        self.from_unit_menu.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="To:", font=("Arial", 14), bg="#fff9c4").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.to_unit_menu = ttk.Combobox(frame, textvariable=self.to_unit_var)
        self.to_unit_menu.grid(row=2, column=1, pady=5)

        # Amount entry
        tk.Label(frame, text="Value:", font=("Arial", 14), bg="#fff9c4").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.amount_entry = tk.Entry(frame, font=("Arial", 14))
        self.amount_entry.grid(row=3, column=1, pady=5)

        # Buttons
        tk.Button(self, text="Convert", font=("Arial", 14), bg="black", fg="yellow",
                  command=self.convert).pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 16, "bold"), bg="#fff9c4", fg="black")
        self.result_label.pack(pady=10)

        tk.Button(self, text="Clear", font=("Arial", 12), command=self.clear, bg="black", fg="yellow").pack()

        self.update_units()

    def update_units(self, event=None):
        cat = self.category_var.get()
        units = list(conversion_factors[cat].keys())
        self.from_unit_menu['values'] = units
        self.to_unit_menu['values'] = units
        self.from_unit_var.set(units[0])
        self.to_unit_var.set(units[1])

    def convert(self):
        category = self.category_var.get()
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        try:
            value = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a numeric value.")
            return

        if category == 'Temperature':
            result = convert_temperature(value, from_unit, to_unit)
        else:
            base = value / conversion_factors[category][from_unit]
            result = base * conversion_factors[category][to_unit]

        self.result_label.config(text=f"{value} {from_unit} = {round(result, 4)} {to_unit}")

    def clear(self):
        self.amount_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    app = UnitConverter()
    app.mainloop()
