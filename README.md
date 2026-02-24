# 🏋️ FitnessTrackerWeb

A real-time **web-based fitness tracking application** built using **Flask**, **OpenCV**, and **MediaPipe Pose**.  
The application uses your webcam to detect body posture, calculate joint angles, count exercise repetitions, and provide live feedback on exercise form.

---

## 🚀 Features

- ✅ Real-time webcam video streaming
- ✅ Pose detection with MediaPipe
- ✅ Exercise repetition counter
- ✅ Live form feedback
- ✅ Multiple exercise support:
  - Squats
  - Pushups
  - Lunges
- ✅ Session logging to CSV
- ✅ Simple dashboard interface

---

## 🧠 How It Works

1. Webcam frames are captured using **OpenCV**
2. **MediaPipe Pose** detects body landmarks
3. Joint angles are calculated from landmark coordinates
4. Angle thresholds determine exercise stages
5. Repetitions are counted when valid movement occurs
6. Feedback is displayed in real time
7. Session data is saved to CSV

---

## 📁 Project Structure
```
FitnessTrackerWeb/

├── app.py                     # Main Flask application  
├── requirements.txt           # Dependencies  

├── pose_modules/  
│   └── pose_tracker.py        # Pose detection logic  

├── utils/  
│   ├── angles.py              # Joint angle calculations  
│   ├── exercise_logic.py      # Rep counting logic  
│   └── session_manager.py     # CSV session management  

├── templates/  
│   ├── index.html             # Main UI  
│   └── dashboard.html         # Dashboard / stats  

└── static/  
    ├── styles.css             # Styling  
    └── charts.js              # Frontend logic  

```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SaakshiMV/FitnessTrackerWeb.git
cd FitnessTrackerWeb
````

---

### 2️⃣ Create Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🏃 Supported Exercises

| Exercise | Detection Method     |
| -------- | -------------------- |
| Squat    | Knee angle tracking  |
| Pushup   | Elbow angle tracking |
| Lunge    | Knee angle tracking  |

Repetitions are counted when joint angles cross predefined thresholds.

---

## 💾 Session Tracking

Workout sessions are stored in:

```
session_stats.csv
```

Each entry includes:

* Timestamp
* Exercise Type
* Repetition Count
* Feedback

Sessions are saved via the `/save_session` route.

---

## 🛠️ Tech Stack

* Python
* Flask
* OpenCV
* MediaPipe Pose
* HTML / CSS / JavaScript

---

## 📌 Future Improvements

* User authentication & profiles
* Database integration (SQLite / PostgreSQL)
* Exercise history dashboard
* Additional exercises
* Improved pose smoothing & accuracy
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, open issues, or submit pull requests.

---

## ❤️ Acknowledgements

Built using:

* MediaPipe by Google
* OpenCV
* Flask Framework

---
Just tell me 👍
```
