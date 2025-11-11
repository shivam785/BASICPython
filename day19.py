import os
from pytube import YouTube, exceptions
from time import time
from customtkinter import *

set_appearance_mode("System")
set_default_color_theme("blue")

# Create download directory if not exists
if "youtube_downloads" not in os.listdir():
    os.mkdir("youtube_downloads")

yt = None  # Global to store the YouTube object

# Fetch available qualities from URL
def fetch_qualities():
    global yt
    url = entry.get().strip()
    quality_combo.set("")  # Reset dropdown
    if not url:
        status_label.configure(text="❌ Enter a YouTube URL", text_color="red")
        return
    try:
        yt = YouTube(url)
        resolutions = list({
            stream.resolution for stream in yt.streams.filter(progressive=True).order_by('resolution').desc()
        })
        if resolutions:
            quality_combo.configure(values=resolutions)
            quality_combo.set(resolutions[0])
            status_label.configure(text="✅ Qualities loaded", text_color="green")
        else:
            status_label.configure(text="⚠️ No downloadable resolutions", text_color="orange")
    except exceptions.RegexMatchError:
        status_label.configure(text="❌ Invalid YouTube URL", text_color="red")
    except Exception as e:
        status_label.configure(text=f"⚠️ Error: {str(e)}", text_color="red")

# Download selected quality
def download_video():
    if not yt:
        status_label.configure(text="❌ Load a valid URL first", text_color="red")
        return
    selected_quality = quality_combo.get()
    if not selected_quality:
        status_label.configure(text="❌ Please select a video quality", text_color="red")
        return

    try:
        status_label.configure(text="⏳ Downloading...", text_color="orange")
        master.update()

        stream = yt.streams.filter(res=selected_quality, progressive=True).first()
        if not stream:
            status_label.configure(text="⚠️ Selected quality not available", text_color="red")
            return

        start_time = time()
        stream.download("youtube_downloads")
        end_time = time()
        status_label.configure(
            text=f"✅ Downloaded {selected_quality} in {round(end_time - start_time, 2)}s",
            text_color="green"
        )
    except Exception as e:
        status_label.configure(text=f"❌ Download error: {str(e)}", text_color="red")

# GUI Setup
master = CTk()
master.title("🎬 YouTube Downloader with Quality Selector")
master.geometry("550x350")
master.resizable(False, False)

frame = CTkFrame(master, corner_radius=15)
frame.pack(padx=30, pady=30, fill="both", expand=True)

title = CTkLabel(frame, text="YouTube Video Downloader", font=("Helvetica", 20, "bold"))
title.pack(pady=(10, 20))

entry = CTkEntry(frame, placeholder_text="Paste YouTube video link here...", width=400)
entry.pack(pady=10)

load_btn = CTkButton(frame, text="🔍 Load Qualities", command=fetch_qualities)
load_btn.pack(pady=5)

quality_combo = CTkOptionMenu(frame, values=[""], width=200)
quality_combo.pack(pady=10)

download_btn = CTkButton(frame, text="⬇️ Download Video", command=download_video, width=200)
download_btn.pack(pady=10)

status_label = CTkLabel(frame, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

footer = CTkLabel(master, text="Made with ❤️ using customtkinter & pytube", font=("Helvetica", 10), text_color="gray")
footer.pack(side="bottom", pady=5)

master.mainloop()
