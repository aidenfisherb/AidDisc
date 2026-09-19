from nicegui import ui

import Navigation.navbar_items.home 
import Navigation.navbar_items.course_catalog 
import Navigation.navbar_items.rounds
import Navigation.menu_items.scorecard
import Navigation.menu_items.play_round
import Navigation.menu_items.measure_distance

@ui.page("/")
def index():
    ui.navigate.to("/home")

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="AidDisc")
