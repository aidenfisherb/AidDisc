from math import radians, sin, cos, sqrt, atan2
conversions = {
    "feet": 0.3048,
    "meters": 1.0,
    "yards": 0.9144,
}

    #converts latitude and longitude to meters
def haversine_meters(start_lat, start_lon, end_lat, end_lon):

    #convertion to radians for formula
    lat1 = radians(start_lat)
    lon1 = radians(start_lon)
    lat2 = radians(end_lat)
    lon2 = radians(end_lon)


    difference_lat = lat2 - lat1
    difference_lon = lon2 - lon1

    a = sin(difference_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(difference_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371000  # Radius of Earth in meters
    distance = r * c
    return distance

def convert_distance(distance_meters, unit):
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    return distance_meters / conversions[unit]
