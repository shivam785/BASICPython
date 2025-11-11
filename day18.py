import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import threading

def download_video():
    url = entry.get().strip()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube video URL.")
        return

    def download():
        try:
            label.config(text="Downloading...", fg="blue")
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            label.config(text="Download complete!", fg="green")
        except Exception as e:
            label.config(text="Download failed.", fg="red")
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    # Run download in a thread to prevent freezing UI
    threading.Thread(target=download).start()

# --- GUI Setup ---
app = tk.Tk()
app.title("🎬 YouTube Video Downloader")
app.geometry("500x250")
app.configure(bg="#f4f6f7")

# --- Title ---
tk.Label(app, text="YouTube Downloader", font=("Helvetica", 18, "bold"), bg="#f4f6f7", fg="#333").pack(pady=15)

# --- URL Input ---
tk.Label(app, text="Enter YouTube Video URL:", font=("Helvetica", 12), bg="#f4f6f7").pack()
entry = tk.Entry(app, font=("Helvetica", 12), width=45, bd=2)
entry.pack(pady=10)

# --- Download Button ---
tk.Button(app, text="⬇️ Download Video", font=("Helvetica", 12, "bold"),
          bg="#28a745", fg="white", padx=10, pady=5, command=download_video).pack(pady=10)

# --- Status Label ---
label = tk.Label(app, text="", font=("Helvetica", 11), bg="#f4f6f7", fg="black")
label.pack(pady=5)

# --- Run App ---
app.mainloop()
