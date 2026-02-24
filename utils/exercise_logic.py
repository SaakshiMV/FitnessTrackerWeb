class ExerciseCounter:
    def __init__(self, exercise_type="squat"):
        self.counter = 0
        self.stage = None
        self.exercise = exercise_type

    def update(self, angle):
        feedback = ""
        color = (0, 255, 0)  # default green

        if self.exercise == "squat":
            if angle > 160:
                self.stage = "UP"
                color = (0, 255, 0)
            if angle < 90 and self.stage == "UP":
                self.stage = "DOWN"
                self.counter += 1
                feedback = "Good Squat!"
                color = (0, 255, 0)
            elif angle < 90:
                feedback = "Bend More"
                color = (0, 0, 255)  # red for bad form

        elif self.exercise == "pushup":
            if angle > 160:
                self.stage = "UP"
            if angle < 90 and self.stage == "UP":
                self.stage = "DOWN"
                self.counter += 1
                feedback = "Good Pushup!"
                color = (0, 255, 0)
            elif angle < 90:
                feedback = "Go Lower"
                color = (0, 0, 255)

        elif self.exercise == "lunge":
            if angle > 160:
                self.stage = "UP"
            if angle < 90 and self.stage == "UP":
                self.stage = "DOWN"
                self.counter += 1
                feedback = "Good Lunge!"
                color = (0, 255, 0)
            elif angle < 90:
                feedback = "Step Lower"
                color = (0, 0, 255)

        return self.counter, feedback, color