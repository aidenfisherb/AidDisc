from nicegui import ui

def back_button():
    ui.button(icon="arrow_back", on_click=lambda: ui.navigate.back()) \
        .props("flat round").tooltip("Back")