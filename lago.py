from geopy.distance import geodesic

def is_inside_circle(center_lat, center_lon, point_lat, point_lon, radius_km=5):
    center = (center_lat, center_lon)
    point = (point_lat, point_lon)
    distance = geodesic(center, point).km
    return distance <= radius_km

# Input dall'utente
center_latitude = 42.122797
center_longitude = 12.232452
point_latitude = float(input("Inserisci la latitudine del punto: "))
point_longitude = float(input("Inserisci la longitudine del punto: "))

if is_inside_circle(center_latitude, center_longitude, point_latitude, point_longitude):
    print("Il punto si trova all'interno dell'area circolare.")
else:
    print("Il punto è fuori dall'area circolare.")
