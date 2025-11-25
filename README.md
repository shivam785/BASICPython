# 📸 Smart Face Attendance System

Smart Face Attendance is a **Streamlit-based website** that uses **face recognition** to automatically mark attendance from a webcam , any camera setup connected to the system or a group photo.  
This project was developed as part of an **NIT internship** in a group of two people with **Harsh Vishwakarma**.

---

## 🚀 Features.

- Add new faces using a **webcam**.
- Automatically **mark attendance in real-time** from the webcam.
- **Upload group photos** and mark attendance for all detected known faces.
- Store attendance records as **CSV files (per day)**.
- Simple **web UI built with Streamlit** – runs in the browser.
- Two implementations:
  - `Sa.py` → uses **MTCNN + face_recognition** for face detection & recognition. :contentReference[oaicite:0]{index=0}  
  - `try2.py` → uses only **face_recognition (dlib-based)** for a simpler pipeline. :contentReference[oaicite:1]{index=1}  

---

## 🧰 Tech Stack

- **Python**
- **Streamlit** – web UI
- **OpenCV (cv2)** – image & video handling
- **NumPy** – numerical operations
- **face_recognition** – face encoding & matching
- **MTCNN** (in `Sa.py`) – face detection
- **pickle** – storing face encodings & names
- **CSV** – attendance logs
- **Datetime** – date & time stamps

---

## 📁 Project Structure

```bash
smart-attendance/
├── Sa.py                  # Smart Face Attendance (MTCNN + face_recognition)
├── try2.py                # Smart Face Attendance (face_recognition only)
├── data/                  # Stored face encodings & names (auto-created)
│   ├── face_encodings.pkl
│   └── names.pkl
├── Attendance/            # Daily attendance CSV files (auto-created)
│   ├── Attendance_DD-MM-YYYY.csv
└── README.md              # Project documentation
