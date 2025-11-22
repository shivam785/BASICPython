# Smart Face Attendance using face_recognition (dlib-based)

import streamlit as st
import cv2
import numpy as np
import face_recognition
import os
import pickle
import csv
from datetime import datetime

st.set_page_config(page_title="Smart Face Attendance", layout="centered")

# Ensure folders exist
os.makedirs("data", exist_ok=True)
os.makedirs("Attendance", exist_ok=True)

st.title("📸 Smart Face Attendance System")

mode = st.sidebar.selectbox("Select Mode", ["Add Face", "Mark Attendance", "Upload Photo & Mark Attendance", "View Attendance"])
threshold = st.sidebar.slider("Face Match Threshold", 0.3, 0.6, 0.5)

# ------------------ ADD FACE ------------------
if mode == "Add Face":
    name = st.text_input("Enter Your Name")
    if st.button("Capture Face") and name:
        encodings_list = []
        count = 0
        st.info("Collecting face encodings... Please look at the camera.")

        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while count < 100:
            ret, frame = cap.read()
            if not ret:
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb)

            for face in faces:
                top, right, bottom, left = face
                encoding = face_recognition.face_encodings(rgb, [face])[0]
                encodings_list.append(encoding)
                count += 1
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.putText(frame, f"Collected: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

            stframe.image(frame, channels="BGR")

        cap.release()
        st.success("✅ Face encodings collected!")

        # Save encodings
        if os.path.exists("data/face_encodings.pkl"):
            with open("data/face_encodings.pkl", "rb") as f:
                all_encodings = pickle.load(f)
        else:
            all_encodings = []

        all_encodings.extend(encodings_list)
        with open("data/face_encodings.pkl", "wb") as f:
            pickle.dump(all_encodings, f)

        names = [name] * len(encodings_list)
        if os.path.exists("data/names.pkl"):
            with open("data/names.pkl", "rb") as f:
                all_names = pickle.load(f)
            all_names += names
        else:
            all_names = names

        with open("data/names.pkl", "wb") as f:
            pickle.dump(all_names, f)

# ------------------ MARK ATTENDANCE ------------------
elif mode == "Mark Attendance":
    if not os.path.exists("data/face_encodings.pkl"):
        st.error("❌ No face data found. Please add faces first.")
    elif st.button("Start Attendance"):
        with open("data/face_encodings.pkl", "rb") as f:
            known_encodings = pickle.load(f)
        with open("data/names.pkl", "rb") as f:
            known_names = pickle.load(f)

        cap = cv2.VideoCapture(0)
        present = set()
        stframe = st.empty()
        stop_btn = st.button("🛑 Stop Attendance")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or stop_btn:
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb)
            encodings = face_recognition.face_encodings(rgb, faces)

            timestamp = datetime.now()
            date = timestamp.strftime("%d-%m-%Y")
            time_str = timestamp.strftime("%H:%M:%S")

            for encoding, (top, right, bottom, left) in zip(encodings, faces):
                distances = face_recognition.face_distance(known_encodings, encoding)
                min_dist = np.min(distances) if len(distances) else 1.0
                match_index = np.argmin(distances)

                if min_dist < threshold:
                    name = known_names[match_index]
                else:
                    name = "Unknown"

                if name != "Unknown" and name not in present:
                    present.add(name)
                    filename = f"Attendance/Attendance_{date}.csv"
                    file_exists = os.path.isfile(filename)
                    with open(filename, "a", newline='') as f:
                        writer = csv.writer(f)
                        if not file_exists:
                            writer.writerow(["NAME", "DATE", "TIME"])
                        writer.writerow([name, date, time_str])
                    st.success(f"📌 Marked: {name}")

                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)

            stframe.image(frame, channels="BGR")

        cap.release()
        st.subheader("🟢 Attendance Summary")
        st.write("### Present:", present)

# ------------------ UPLOAD PHOTO ------------------
elif mode == "Upload Photo & Mark Attendance":
    st.info("Upload a group photo to mark attendance.")
    image_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
    if image_file:
        with open("data/face_encodings.pkl", "rb") as f:
            known_encodings = pickle.load(f)
        with open("data/names.pkl", "rb") as f:
            known_names = pickle.load(f)

        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        present = set()
        timestamp = datetime.now()
        date = timestamp.strftime("%d-%m-%Y")
        time_str = timestamp.strftime("%H:%M:%S")

        for encoding, (top, right, bottom, left) in zip(encodings, faces):
            distances = face_recognition.face_distance(known_encodings, encoding)
            min_dist = np.min(distances)
            match_index = np.argmin(distances)

            if min_dist < threshold:
                name = known_names[match_index]
            else:
                name = "Unknown"

            if name != "Unknown" and name not in present:
                present.add(name)
                filename = f"Attendance/Attendance_{date}.csv"
                file_exists = os.path.isfile(filename)
                with open(filename, "a", newline='') as f:
                    writer = csv.writer(f)
                    if not file_exists:
                        writer.writerow(["NAME", "DATE", "TIME"])
                    writer.writerow([name, date, time_str])

            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

        st.image(frame, channels="BGR")
        st.success("✅ Attendance marked from image.")
        st.write("### Present:", present)

# ------------------ VIEW ATTENDANCE ------------------
elif mode == "View Attendance":
    files = os.listdir("Attendance")
    if files:
        selected = st.selectbox("Select Date", sorted(files, reverse=True))
        with open(f"Attendance/{selected}", newline='') as f:
            csv_content = f.read()
            st.download_button("📥 Download Attendance CSV", data=csv_content, file_name=selected, mime="text/csv")
            f.seek(0)
            data = list(csv.reader(f))
        st.table(data)
    else:
        st.info("No attendance records found.")
