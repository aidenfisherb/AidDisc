from nicegui import ui
from Helpers.distance import haversine_meters, convert_distance, average_readings
from Navigation.components.back import back_button
from Helpers.distance import CAPTURE_JS, CAPTURE_SECONDS

async def acquire_location():
    readings = await ui.run_javascript(CAPTURE_JS, timeout=CAPTURE_SECONDS + 7)
    return average_readings(readings)

@ui.page("/measure_distance")
def distance_ui():
    points = {"start": None, "end": None}
    markers = {"start": None, "end": None}

    def place_marker(key, lat_lng):
        if lat_lng is None:
            return
        lat, lon = lat_lng
        if markers[key] is None:
            markers[key] = m.marker(latlng=(lat, lon))
        else:
            markers[key].move(lat, lon)
        markers[key].run_method("bindPopup", f"{key.capitalize()} point")
        m.set_center((lat, lon))
        m.set_zoom(35)

    async def handle_start_measure():
        result.set_text("Measuring... stand still")
        points["start"] = await acquire_location()
        place_marker("start", points["start"])
        start_button.set_visibility(False)
        result.set_text("Start point set. Now set the end point.")
        end_button.set_visibility(True)
        title.set_text("How far did you throw?")

    async def handle_end_measure():
        result.set_text("Measuring... stand still")
        points["end"] = await acquire_location()
        place_marker("end", points["end"])
        result.set_text("End point set.")
        end_button.set_visibility(False)
        calculate_button.set_visibility(True)
        title.set_text("See your distance!")

    def calculate_distance():
        start, end = points["start"], points["end"]
        if not (start and end):
            result.set_text("Set both a start and an end point first.")
            return
        meters = haversine_meters(start[0], start[1], end[0], end[1])
        result.set_text(
            f"{convert_distance(meters, 'feet'):.1f} ft "
            f"({convert_distance(meters, 'yards'):.1f} yds)"
        )
        calculate_button.set_visibility(False)
        reset_button.set_visibility(True)


    def reset():
        points["start"] = None
        points["end"] = None
        if markers["start"]:
            m.remove_layer(markers["start"])
            markers["start"] = None
        if markers["end"]:
            m.remove_layer(markers["end"])
            markers["end"] = None
        result.set_text("")
        start_button.set_visibility(True)
        end_button.set_visibility(False)
        calculate_button.set_visibility(False)
        reset_button.set_visibility(False)

    options = {
    'zoomControl': False,
    'scrollWheelZoom': False,
    'doubleClickZoom': False,
    'boxZoom': False,
    'keyboard': False,
    'dragging': True,
}

    BUTTON_CLASSES = "w-full max-w-xs"

    with ui.header().classes("w-full bg-white shadow-md"):
        back_button()
        m = ui.leaflet(center=(39, -98), zoom=4, options=options).classes("w-full h-[50vh]")

    with ui.footer().classes("bg-slate-800 w-full"):
        with ui.column().classes("items-center gap-3 w-full p-4"):
            title = ui.label("Where are you throwing from?").classes("text-2xl font-semibold text-white text-center")
            start_button = ui.button("Start Measurement", on_click=handle_start_measure).props("color=green rounded").classes(BUTTON_CLASSES)
            end_button = ui.button("End Measurement", on_click=handle_end_measure).props("color=red rounded").classes(BUTTON_CLASSES)
            calculate_button = ui.button("Calculate Distance", on_click=calculate_distance).props("color=blue rounded").classes(BUTTON_CLASSES)
            reset_button = ui.button("Measure Again", on_click=reset).props("color=blue rounded").classes(BUTTON_CLASSES)
            result = ui.label().classes("text-lg text-white text-center")
            ui.label("Distances can be off by ~10ft").classes("text-sm text-slate-400 text-center")
    reset()
