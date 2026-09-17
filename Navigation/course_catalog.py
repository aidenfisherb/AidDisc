from nicegui import ui

from Classes.Greeter import Greeter
from Navigation.navbar import navbar

@ui.page("/courses")
def course_catalog():
    navbar()

    with ui.row().classes("w-full flex-wrap justify-center items-stretch gap-6"):
        with ui.card().classes("w-full md:flex-1 md:max-w-md"):
            ui.image('https://picsum.photos/id/684/640/360')
            with ui.card_section().classes("flex flex-col"):
                ui.label('Course Title').classes('text-lg text-slate-700')
                ui.label('Course Location').classes('text-xs text-slate-500')
                ui.label('Course Difficulty').classes('text-xs text-slate-500')

        with ui.card().classes("w-full md:flex-1 md:max-w-md"):
            ui.image('https://picsum.photos/id/684/640/360')
            with ui.card_section():
                  ui.label('Course Title').classes('text-lg text-slate-700')
                  ui.label('Course Location').classes('text-xs text-slate-500')
                  ui.label('Course Difficulty').classes('text-xs text-slate-500')

