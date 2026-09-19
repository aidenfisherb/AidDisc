from nicegui import ui
from Helpers.distance import haversine_meters, convert_distance, average_readings

CAPTURE_SECONDS = 5

CAPTURE_JS = f"""
new Promise((resolve, reject) => {{
    const readings = [];
    const watchId = navigator.geolocation.watchPosition(
        pos => readings.push([pos.coords.latitude, pos.coords.longitude, pos.coords.accuracy]),
        err => {{ navigator.geolocation.clearWatch(watchId); reject(err); }},
        {{ enableHighAccuracy: true, maximumAge: 0, timeout: 10000 }}
    );
    setTimeout(() => {{
        navigator.geolocation.clearWatch(watchId);
        resolve(readings);
    }}, {CAPTURE_SECONDS * 1000});
}})
"""


async def acquire_location():
    readings = await ui.run_javascript(CAPTURE_JS, timeout=CAPTURE_SECONDS + 7)
    return average_readings(readings)


@ui.page("/measure_distance")
def distance_ui():
    points = {"start": None, "end": None}

    async def handle_start_measure():
        result.set_text("Measuring... stand still")
        points["start"] = await acquire_location()
        result.set_text(f"Start set: {points['start']}")

    async def handle_end_measure():
        result.set_text("Measuring... stand still")
        points["end"] = await acquire_location()
        result.set_text(f"End set: {points['end']}")

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

    with ui.column().classes("items-center gap-4 w-full mt-24"):
        ui.label("Distance Measurement Page").classes("text-3xl font-semibold")
        ui.label("This page will allow users to measure distances.").classes("text-lg text-slate-700")
        ui.button("Start Measurement", on_click=handle_start_measure).classes("bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded")
        ui.button("End Measurement", on_click=handle_end_measure).classes("bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded")
        ui.button("Calculate Distance", on_click=calculate_distance).classes("bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded")
        result = ui.label().classes("text-lg text-slate-700")
