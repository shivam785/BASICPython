# GUI Password Generator
import tkinter as tk
import string, random

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=12))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

app = tk.Tk()
app.title("Password Generator")

tk.Button(app, text="Generate Password", command=generate_password).pack(pady=10)
result_entry = tk.Entry(app, width=30)
result_entry.pack(pady=10)

app.mainloop()
