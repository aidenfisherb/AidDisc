from nicegui import ui

def menu():
    with ui.row().classes('w-full items-center'):
        result = ui.label().classes('mr-auto')
        with ui.button(icon='menu'):
            with ui.menu() as menu:
                ui.menu_item('Play a Round', lambda: ui.navigate.to('/play_round'))
                ui.menu_item('My Profile', lambda: ui.navigate.to('/profile'))
                ui.menu_item('Create a Course', lambda: ui.navigate.to('/create_course'))
                ui.menu_item('Measure Distance', lambda: ui.navigate.to('/measure_distance'))
                ui.separator()
                ui.menu_item('Close', menu.close)