from nicegui import ui

from Classes.Greeter import Greeter


@ui.page("/")
def greeter_page():
    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("Class Instance Demo").classes("text-3xl font-semibold")

        message = ui.label().classes("text-lg text-slate-700")

        def create_greeter():
            greeter = Greeter("Aiden")
            message.set_text(greeter.greet())

        ui.button("Create Greeter", on_click=create_greeter)
