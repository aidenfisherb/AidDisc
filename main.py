from nicegui import ui

import Navigation.home 
import Navigation.course_catalog 
import Navigation.rounds

@ui.page("/")
def index():
    ui.navigate.to("/home")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="AidDisc")
