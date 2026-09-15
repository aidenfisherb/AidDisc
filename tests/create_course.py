# Interactive scenario for creating a course.
# (Moved here from tests/test_course.py, which is now an automated test.)4
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from Classes.Course import Course
from dataclasses import fields
import random

phrases = [
    "Tell me about the ",
    "Give me the ",
    "What is the ",
    "You're starting to bore me, but I will still ask about the ",
    "Please provide the ",
    "I need the "
]

fields = [
    "name of the course",
    "par of the course",
    "rating of the course",
    "difficulty of the course",
    "location of the course"
]

    #method that lists the fields of the Course class fix later
def list_fields():
    return [field.name for field in fields(Course)]

def main():
    print("====================================")
    print("Welcome to AidDisc!")
    print("====================================")
    print("If you wish to quit at any time during this process, please type 'quit' and press enter.")
    print("=====================================")

    print("To create a course, please fill out the following fields.")

    responses = []
    user_input = ""
    for field in fields:
        if user_input.lower() == "quit":
            break
        print(random.choice(phrases) + field + ": ")
        user_input = input()
        responses.append(user_input)

    print("====================================")
    print("Great, would you like to continue creating the course with the following information?")
    print("Name: " + responses[0])
    print("Par: " + responses[1])
    print("Rating: " + responses[2])
    print("Difficulty: " + responses[3])
    print("Location: " + responses[4])
    print("====================================")

    user_input = input("Type 'yes' to continue, or 'no' to edit: ")

    if user_input.lower() == "yes":
        course = Course(responses[0], int(responses[1]), float(responses[2]), responses[3], responses[4])
        course.print_course()

if __name__ == "__main__":
    main()
