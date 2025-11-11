import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound
from threading import Thread

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("⏰ Alarm Clock")
        self.geometry("420x300")
        self.configure(bg="#1e1e2e")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self, text="Alarm Clock", font=("Helvetica", 24, "bold"),
                 fg="#00ffff", bg="#1e1e2e").pack(pady=10)

        # Current Time Display
        self.time_label = tk.Label(self, text="", font=("Courier", 18),
                                   fg="#ffffff", bg="#1e1e2e")
        self.time_label.pack(pady=5)
        self.update_clock()

        # Time Setting Frame
        tk.Label(self, text="Set Alarm Time", font=("Helvetica", 16),
                 fg="white", bg="#1e1e2e").pack(pady=10)

        time_frame = tk.Frame(self, bg="#1e1e2e")
        time_frame.pack()

        # Dropdowns for Hour, Minute, Second
        self.hour = tk.StringVar(self)
        self.minute = tk.StringVar(self)
        self.second = tk.StringVar(self)

        hours = [f"{i:02}" for i in range(24)]
        minutes_seconds = [f"{i:02}" for i in range(60)]

        self.hour.set(hours[0])
        self.minute.set(minutes_seconds[0])
        self.second.set(minutes_seconds[0])

        self.create_dropdown(time_frame, self.hour, hours).pack(side="left", padx=5)
        self.create_dropdown(time_frame, self.minute, minutes_seconds).pack(side="left", padx=5)
        self.create_dropdown(time_frame, self.second, minutes_seconds).pack(side="left", padx=5)

        # Set Alarm Button
        tk.Button(
            self,
            text="Set Alarm",
            font=("Helvetica", 14, "bold"),
            bg="#00ffff",
            fg="#000000",
            padx=10,
            pady=5,
            relief="raised",
            bd=3,
            command=self.start_thread
        ).pack(pady=20)

    def create_dropdown(self, parent, variable, options):
        return tk.OptionMenu(parent, variable, *options)

    def update_clock(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"Current Time: {now}")
        self.after(1000, self.update_clock)

    def start_thread(self):
        t = Thread(target=self.alarm)
        t.daemon = True
        t.start()

    def alarm(self):
        alarm_time = f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}"
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Checking:", current_time)
            if current_time == alarm_time:
                print("⏰ Time to Wake up!")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                messagebox.showinfo("Alarm", "Time to Wake Up! ⏰")
                break

if __name__ == "__main__":
    app = AlarmClock()
    app.mainloop()
