import tkinter as tk
from tkinter import filedialog, messagebox
import random
import json
import pyperclip

# Generate a random substitution key
def generate_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# Encrypt text with a given key
def encrypt(text, key):
    text = text.upper()
    return ''.join(key.get(char, char) for char in text)

# Reverse key for decryption
def invert_key(key):
    return {v: k for k, v in key.items()}

# GUI Application
class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Encryption Tool")

        self.key = generate_key()
        self.decryption_mode = tk.BooleanVar(value=False)

        self.build_gui()

    def build_gui(self):
        tk.Label(self.root, text="Enter Text:").pack()
        self.input_text = tk.Text(self.root, height=5)
        self.input_text.pack()
        self.input_text.bind("<KeyRelease>", self.update_output)

        tk.Checkbutton(self.root, text="Decryption Mode", variable=self.decryption_mode,
                       command=self.update_output).pack()

        tk.Label(self.root, text="Encrypted Output:").pack()
        self.output_text = tk.Text(self.root, height=5, state='disabled')
        self.output_text.pack()

        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_output).pack(pady=2)
        tk.Button(self.root, text="Save Key", command=self.save_key).pack(pady=2)
        tk.Button(self.root, text="Load Key", command=self.load_key).pack(pady=2)

        self.key_map_label = tk.Label(self.root, text=f"Key Map: {self.key}")
        self.key_map_label.pack(pady=5)

    def update_output(self, event=None):
        text = self.input_text.get("1.0", tk.END).strip()
        if self.decryption_mode.get():
            output = encrypt(text, invert_key(self.key))
        else:
            output = encrypt(text, self.key)

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output)
        self.output_text.config(state='disabled')

    def copy_output(self):
        result = self.output_text.get("1.0", tk.END).strip()
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Encrypted text copied to clipboard!")

    def save_key(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.key, f)
            messagebox.showinfo("Saved", "Encryption key saved.")

    def load_key(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, "r") as f:
                self.key = json.load(f)
            self.key_map_label.config(text=f"Key Map: {self.key}")
            self.update_output()
            messagebox.showinfo("Loaded", "Encryption key loaded.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
