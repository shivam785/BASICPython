import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import schedule
import time
import os
import threading
import tkinter as tk
from tkinter import messagebox

# Step 1: Email configuration using environment variables
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

# Step 2: Define function to send plain text email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Step 3: Schedule the email
def schedule_email(to_email, subject, body, schedule_time):
    def job():
        send_email(to_email, subject, body)

    schedule.every().day.at(schedule_time).do(job)

# Step 4: Run the scheduler in a separate thread to keep the GUI responsive
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Step 5: Define GUI functionality
def on_submit():
    to_email = email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    schedule_time = time_entry.get()

    if not to_email or not subject or not body or not schedule_time:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    schedule_email(to_email, subject, body, schedule_time)
    messagebox.showinfo("Scheduled", f"Email scheduled at {schedule_time} daily.")
    print("Scheduled email job added.")

# Step 6: Create GUI using Tkinter
app = tk.Tk()
app.title("Daily Email Scheduler")
app.geometry("400x400")

tk.Label(app, text="Recipient Email").pack()
email_entry = tk.Entry(app, width=40)
email_entry.pack()

tk.Label(app, text="Subject").pack()
subject_entry = tk.Entry(app, width=40)
subject_entry.pack()

tk.Label(app, text="Body").pack()
body_text = tk.Text(app, height=5, width=30)
body_text.pack()

tk.Label(app, text="Schedule Time (HH:MM)").pack()
time_entry = tk.Entry(app, width=20)
time_entry.pack()

submit_btn = tk.Button(app, text="Schedule Email", command=on_submit)
submit_btn.pack(pady=10)

# Start scheduler thread
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# Step 7: Run the app
app.mainloop()
