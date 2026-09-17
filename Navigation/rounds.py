from nicegui import ui

from Classes.Greeter import Greeter
from Navigation.navbar import navbar

@ui.page("/rounds")
def rounds():
    navbar()
    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("This will have some rounds page stuff").classes("text-3xl font-semibold")

