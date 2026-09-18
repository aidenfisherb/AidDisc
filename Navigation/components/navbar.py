from nicegui import ui

def navbar():
    with ui.footer(fixed=True).props("dense").classes("bg-slate-800 text-white items-center px-3 py-1 gap-2"):
        ui.label("AidDisc").classes("text-lg font-bold")

        with ui.row().classes("gap-2 items-center"):
            ui.button(icon="home", on_click=lambda: ui.navigate.to("/home")) \
                .props("flat round").tooltip("Home")
            ui.button(icon="golf_course", on_click=lambda: ui.navigate.to("/courses")) \
                .props("flat round").tooltip("Courses")
            ui.button(icon="military_tech", on_click=lambda: ui.navigate.to("/rounds")) \
                .props("flat round").tooltip("My Rounds")
            ui.button(icon="scoreboard", on_click=lambda: ui.navigate.to("/scorecard")) \
                .props("flat round").tooltip("Scorecard")