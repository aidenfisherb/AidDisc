from nicegui import ui

import Navigation.greeter_page  # noqa: F401  (registers the "/" page)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="AidDisc")
