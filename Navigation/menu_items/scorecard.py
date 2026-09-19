from nicegui import ui

from Classes.Greeter import Greeter
from Navigation.components.navbar import navbar
from Navigation.components.menu import menu
import json
import time

@ui.page("/scorecard/{course_id}")
def scorecard(course_id: str):
    navbar()
    menu()

    score_labels = []
    current_hole = 0
    score_total = 0

    with open("tests/fake_courses.json", "r") as file:
          courses = json.load(file)

    for course in courses:
        if course["id"] == course_id:
            name = course["name"]
            par = course["par"]
            hole_count = int(course["hole_count"]) + 1
            rating = course["rating"]
            difficulty = course["difficulty"]
            location =  course["location"]
            break

    def change_score(label, num, reset):
        if reset == True: #Checks to see if assign score was used therefore reset current par to 0
            new_score = 0
            label.set_text(str(new_score))
        else:
            new_score = int(label.text) + num
            label.set_text(str(new_score))

    def assign_score():
        nonlocal current_hole
        if current_hole < len(score_labels):
            if int(scratch_label.text) <= 0:
                throw_error()
            else:    
                score_labels[current_hole].set_text(scratch_label.text)
                if int(scratch_label.text) == 3: #Value needs to be changed from 3 to whatever par is for hole
                    score_labels[current_hole].style(f"background-color: lightblue")
                elif int(scratch_label.text) > 3:
                    score_labels[current_hole].style(f"background-color: red")
                else:
                    score_labels[current_hole].style(f"background-color: lightgreen")
                current_hole += 1
                update_total()
                change_score(scratch_label, 0, True)

    def update_total():
        nonlocal score_total
        score_total += int(scratch_label.text)
        score_total_label.set_text(str(score_total))

    def throw_error():
        ui.notify("Score cannot be negative, please try again.")

    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label(name).classes("text-3xl font-semibold")

    with ui.row():
        with ui.column():
            ui.label("Hole").classes("text-3xl font-semibold")
            ui.label("Par").classes("text-3xl font-semibold")
            ui.label("Dist").classes("text-3xl font-semibold")
            ui.label("Player").classes("text-3xl font-semibold") #Make username instead of hardcoded name

        for index in range(1, hole_count ):
            with ui.column():
                ui.label(str(index)).classes("text-3xl font-semibold")
                ui.label("3").classes("text-3xl font-semibold")
                ui.label(".").classes("text-3xl font-semibold")
                score_label = ui.label("").classes("text-3xl font-semibold")
                score_labels.append(score_label)

        with ui.column():
            ui.label("TOTAL").classes("text-3xl font-semibold")
            ui.label(str(3 * hole_count)).classes("text-3xl font-semibold") #Write a function that makes adds each hole par to a total
            ui.label("N/A").classes("text-3xl font-semibold")
            score_total_label = ui.label("").classes("text-3xl font-semibold")

    with ui.column().classes("items-center gap-4 w-full mt-24"):
        with ui.row():
            scratch_label = ui.label("0").classes("text-3xl font-semibold")
        with ui.row():
            ui.button("-", on_click=lambda: change_score(scratch_label, -1, False)).classes("text-3xl font-semibold")
            ui.button("+", on_click=lambda: change_score(scratch_label, 1, False)).classes("text-3xl font-semibold")
        with ui.row():
            ui.button("Add", on_click = assign_score)