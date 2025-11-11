import tkinter as tk
from tkinter import messagebox

class MadLibsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎉 Mad Libs Game")
        self.geometry("600x500")
        self.configure(bg="#f0f8ff")  # Light pastel background
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(
            self,
            text="🎭 Welcome to Mad Libs!",
            font=("Helvetica", 24, "bold"),
            bg="#f0f8ff",
            fg="#ff5733"
        ).pack(pady=20)

        # Instructions
        tk.Label(
            self,
            text="Enter the following types of words to create your story:",
            font=("Helvetica", 14),
            bg="#f0f8ff"
        ).pack(pady=5)

        # Input Fields
        self.noun_entry = self.create_input("Noun:")
        self.verb_entry = self.create_input("Verb:")
        self.adjective_entry = self.create_input("Adjective:")
        self.adverb_entry = self.create_input("Adverb:")

        # Generate Button
        tk.Button(
            self,
            text="✨ Generate Story",
            font=("Helvetica", 14, "bold"),
            bg="#00c9a7",
            fg="white",
            padx=20,
            pady=5,
            bd=2,
            relief="raised",
            command=self.generate_story
        ).pack(pady=20)

        # Output Story Box
        self.story_frame = tk.Frame(self, bg="white", bd=2, relief="groove")
        self.story_frame.pack(padx=30, pady=10, fill="both", expand=True)

        self.story_label = tk.Label(
            self.story_frame,
            text="",
            font=("Helvetica", 14),
            wraplength=500,
            justify="left",
            bg="white",
            fg="#333"
        )
        self.story_label.pack(padx=10, pady=10, fill="both", expand=True)

    def create_input(self, label_text):
        frame = tk.Frame(self, bg="#f0f8ff")
        frame.pack(pady=5)

        tk.Label(frame, text=label_text, font=("Helvetica", 12), bg="#f0f8ff").pack(side="left", padx=10)
        entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
        entry.pack(side="left")
        return entry

    def generate_story(self):
        noun = self.noun_entry.get().strip()
        verb = self.verb_entry.get().strip()
        adjective = self.adjective_entry.get().strip()
        adverb = self.adverb_entry.get().strip()

        if not all([noun, verb, adjective, adverb]):
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        # Construct Mad Libs story
        story = (
            f"Once upon a time, a {adjective} {noun} decided to {verb} {adverb}. "
            f"Everyone in the village was amazed, and it became the talk of the town!"
        )

        # Display the generated story
        self.story_label.config(text=story)

if __name__ == "__main__":
    app = MadLibsApp()
    app.mainloop()
