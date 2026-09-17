from nicegui import ui

from Classes.Greeter import Greeter
from Navigation.components.navbar import navbar
from Navigation.components.menu import menu

@ui.page("/home")
def home():
    navbar()
    menu()
    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("Class Instance Demo").classes("text-3xl font-semibold")

        message = ui.label().classes("text-lg text-slate-700")

        #testing class instance creation and method call
        def create_home():
            greeter = Greeter("Aiden")
            message.set_text(greeter.greet())

        ui.button("Create Greeter", on_click=create_home)
