import csv
from datetime import datetime

class SessionManager:
    def __init__(self, filename="session_stats.csv"):
        self.filename = filename
        self.data = []

    def add_entry(self, exercise, count, feedback):
        self.data.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exercise": exercise,
            "count": count,
            "feedback": feedback
        })

    def save_csv(self):
        keys = ["timestamp", "exercise", "count", "feedback"]
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)