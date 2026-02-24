import cv2
import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_pose(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(rgb)

    def draw_pose(self, frame):
        if self.results.pose_landmarks:
            self.mp_draw.draw_landmarks(
                frame,
                self.results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

    def get_landmarks(self, frame):
        landmarks = []

        if self.results.pose_landmarks:
            h, w, _ = frame.shape

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((id, cx, cy))

        return landmarks