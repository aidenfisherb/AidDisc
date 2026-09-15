
from dataclasses import dataclass

@dataclass
class Course:
    def __init__(self, name, par, rating, difficulty, location):
        self.name = name
        self.par = par
        self.rating = rating
        self.difficulty = difficulty
        self.location = location

    def print_course(self):
        """Print the information of the course."""
        print("Course created successfully!")
        print("====================================")
        print("Course Information:")
        print("Name: " + self.get_name())
        print("Par: " + str(self.get_par()))
        print("Rating: " + str(self.get_rating()))
        print("Difficulty: " + self.get_difficulty())
        print("Location: " + self.get_location())
        print("====================================")
    # Setters

    def alter_course(self, new_name=None, new_par=None, new_rating=None, new_difficulty=None, new_location=None):
        """Alter the properties of the course."""
        if hasattr(self, self.name):
            setattr(self, self.name, new_name)
        if hasattr(self, self.par):
            setattr(self, self.par, new_par)
        if hasattr(self, self.rating):
            setattr(self, self.rating, new_rating)
        if hasattr(self, self.difficulty):
            setattr(self, self.difficulty, new_difficulty)
        if hasattr(self, self.location):
            setattr(self, self.location, new_location)

    # Setters
    def set_name(self, name):
        self.name = name

    def set_par(self, par):
        self.par = par

    def set_rating(self, rating):
        self.rating = rating

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_location(self, location):
        self.location = location

    # Getters
    def get_name(self):
        return self.name

    def get_par(self):
        return self.par

    def get_rating(self):
        return self.rating

    def get_difficulty(self):
        return self.difficulty

    def get_location(self):
        return self.location