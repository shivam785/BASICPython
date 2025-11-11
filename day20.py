# Markdown to HTML Converter GUI
#pip install markdown 
import tkinter as tk
from tkinter import filedialog
import markdown

def convert_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    if file_path:
        with open(file_path, "r") as f:
            text = f.read()
        html = markdown.markdown(text)
        with open(file_path.replace(".md", ".html"), "w") as f:
            f.write(html)
        label.config(text="Converted to HTML!")

app = tk.Tk()
app.title("Markdown to HTML")

tk.Button(app, text="Choose .md file", command=convert_file).pack(pady=20)
label = tk.Label(app, text="")
label.pack()

app.mainloop()
