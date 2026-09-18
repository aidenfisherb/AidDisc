from nicegui import ui
from Helpers.distance import haversine_meters, convert_distance

async def acquire_location():
    return await ui.run_javascript(
        "new Promise((resolve, reject) => { navigator.geolocation.getCurrentPosition("
        "pos => resolve([pos.coords.latitude, pos.coords.longitude]), err => reject(err)); })",
        timeout=10,
    )

async def handle_start_measure():
    start = await acquire_location()
    return start

async def handle_end_measure():
    end = await acquire_location()
    return end

def distance_in_meters():
    start = handle_start_measure()
    end = handle_end_measure()
    if start and end:
        distance = haversine_meters(start[0], start[1], end[0], end[1])
        ui.notify(f"Distance: {distance:.2f} meters")
    else:
        ui.notify("Unable to calculate distance.", color="negative")
        return None


@ui.page("/measure_distance")
def distance_ui():
    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("Distance Measurement Page").classes("text-3xl font-semibold")
        ui.label("This page will allow users to measure distances.").classes("text-lg text-slate-700")
        ui.button("Start Measurement", on_click=handle_start_measure).classes("bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded")
        ui.button("End Measurement", on_click=handle_end_measure).classes("bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded")
        ui.button("Calculate Distance", on_click=distance_in_meters).classes("bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded")

      