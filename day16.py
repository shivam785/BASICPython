# Typing Speed Tester GUI
import tkinter as tk
import time

def start_test():
    global start_time
    start_time = time.time()
    entry.delete(0, tk.END)

def end_test():
    elapsed = time.time() - start_time
    text = entry.get()
    speed = len(text.split()) / (elapsed / 60)
    result_label.config(text=f"Speed: {speed:.2f} WPM")

app = tk.Tk()
app.title("Typing Speed Tester")

tk.Button(app, text="Start", command=start_test).pack()
entry = tk.Entry(app, width=50)
entry.pack()
tk.Button(app, text="Done", command=end_test).pack()
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
