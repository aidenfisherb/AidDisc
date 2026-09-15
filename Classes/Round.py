class Round:
    def __init__(self,course, timestamp, round_number, score, difficulty):
        self.course = course
        self.timestamp = timestamp
        self.round_number = round_number
        self.score = score
        self.difficulty = difficulty

    def print_round(self):
        """Print the information of the round."""
        print("Round created successfully!")
        print("====================================")
        print("Course Information:")
        print("Name: " + self.get_name())
        print("Par: " + str(self.get_par()))
        print("Rating: " + str(self.get_rating()))
        print("Difficulty: " + self.get_difficulty())
        print("Location: " + self.get_location())
        print("====================================")

    def alter_round(self, new_course=None, new_timestamp=None, new_round_number=None, new_score=None, new_difficulty=None):
        """Alter the properties of the round."""
        if hasattr(self, self.course):
            setattr(self, self.course, new_course)
        if hasattr(self, self.timestamp):
            setattr(self, self.timestamp, new_timestamp)
        if hasattr(self, self.round_number):
            setattr(self, self.round_number, new_round_number)
        if hasattr(self, self.score):
            setattr(self, self.score, new_score)
        if hasattr(self, self.difficulty):
            setattr(self, self.difficulty, new_difficulty)

    # Setters
    def set_course(self, course):
        self.course = course

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def set_round_number(self, round_number):
        self.round_number = round_number

    def set_score(self, score):
        self.score = score

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    # Getters
    def get_course(self):
        return self.course  

    def get_timestamp(self):
        return self.timestamp

    def get_round_number(self):
        return self.round_number

    def get_score(self):
        return self.score

    def get_difficulty(self):
        return self.difficulty