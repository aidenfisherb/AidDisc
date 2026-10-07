from nicegui import ui
import json

from Classes.Greeter import Greeter
from Navigation.components.navbar import navbar
from Navigation.components.menu import menu


@ui.page("/courses")
def course_catalog():
    navbar()
    menu()
    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("Select Course").classes("text-3xl font-semibold")

    with open("tests/fake_courses.json", "r") as file:
            courses = json.load(file)

    with ui.row().classes("w-full flex-wrap justify-center items-stretch gap-6"):
        for course in courses:
            name = course["name"]
            location = course["location"]
            difficulty = course["difficulty"]

            #Dont map these to scorecard map them to more information page
            with ui.card().classes("w-full md:flex-1 md:max-w-md").on('click', lambda course_id=course["id"]: ui.navigate.to(f"/scorecard/{course_id}")):
                ui.image('https://picsum.photos/id/684/640/360')
                with ui.card_section().classes("flex flex-col"):
                    ui.label(name).classes('text-lg text-slate-700')
                    ui.label(location).classes('text-xs text-slate-500')
                    ui.label(difficulty).classes('text-xs text-slate-500')

    #Delete
    #with ui.row().classes("w-full flex-wrap justify-center items-stretch gap-6"):
        #with ui.card().classes("w-full md:flex-1 md:max-w-md"):
            #ui.image('https://picsum.photos/id/684/640/360')
            #with ui.card_section().classes("flex flex-col"):
                #ui.label('Course Title').classes('text-lg text-slate-700')
                #ui.label('Course Location').classes('text-xs text-slate-500')
                #ui.label('Course Difficulty').classes('text-xs text-slate-500')
        #with ui.card().classes("w-full md:flex-1 md:max-w-md"):
            #ui.image('https://picsum.photos/id/684/640/360')
            #with ui.card_section():
                  #ui.label('Course Title').classes('text-lg text-slate-700')
                  #ui.label('Course Location').classes('text-xs text-slate-500')
                  #ui.label('Course Difficulty').classes('text-xs text-slate-500')

