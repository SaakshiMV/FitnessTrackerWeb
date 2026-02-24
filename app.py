from flask import Flask, render_template, Response, request, jsonify
import cv2
from pose_modules.pose_tracker import PoseTracker
from utils.angles import calculate_angle
from utils.exercise_logic import ExerciseCounter
from utils.session_manager import SessionManager

app = Flask(__name__)
cap = cv2.VideoCapture(0)
tracker = PoseTracker()

exercise_type = "squat"
counter_obj = ExerciseCounter(exercise_type=exercise_type)
session_manager = SessionManager("session_stats.csv")

# Store live stats for AJAX
live_stats = {"count": 0, "feedback": ""}

def generate_frames():
    global counter_obj, exercise_type, live_stats
    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        tracker.find_pose(frame)
        tracker.draw_pose(frame)
        landmarks = tracker.get_landmarks(frame)
        feedback = ""
        color = (0, 255, 0)

        if landmarks:
            if exercise_type == "squat" or exercise_type == "lunge":
                hip = landmarks[24][1:]
                knee = landmarks[26][1:]
                ankle = landmarks[28][1:]
                angle = calculate_angle(hip, knee, ankle)
            elif exercise_type == "pushup":
                shoulder = landmarks[12][1:]
                elbow = landmarks[14][1:]
                wrist = landmarks[16][1:]
                angle = calculate_angle(shoulder, elbow, wrist)

            counter_obj.counter, feedback, color = counter_obj.update(angle)

            # Save session entry for CSV if good rep
            if feedback.startswith("Good"):
                session_manager.add_entry(exercise_type, counter_obj.counter, feedback)

            live_stats["count"] = counter_obj.counter
            live_stats["feedback"] = feedback

            # Overlay on video
            cv2.putText(frame, f"Angle: {int(angle)}", (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.putText(frame, f"{exercise_type.capitalize()}s: {counter_obj.counter}",
                    (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
        cv2.putText(frame, f"{feedback}", (20, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', exercise=exercise_type)

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_exercise', methods=['POST'])
def set_exercise():
    """
    Called when user clicks a button to switch exercises
    """
    global exercise_type, counter_obj, live_stats
    data = request.json
    exercise_type = data['exercise']
    counter_obj = ExerciseCounter(exercise_type=exercise_type)
    live_stats = {"count": 0, "feedback": ""}
    return {"success": True}

@app.route('/get_live_stats')
def get_live_stats():
    return jsonify(live_stats)

@app.route('/save_session', methods=['POST'])
def save_session():
    session_manager.save_csv()
    return {"success": True}

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)