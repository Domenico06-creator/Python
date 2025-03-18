import random
import math
import time
import winsound  # Importa la libreria winsound per la riproduzione audio

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Raggio della Terra in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Definizione delle zone di interesse con nomi e coordinate
zones = {
    "Trevignano": (42.150, 12.220),
    "Anguillara": (42.080, 12.270),
    "Bracciano": (42.100, 12.180)
}

radius_km = 4.5  # Raggio di 4,5 km

def generate_random_coordinates(center_x, center_y, radius_km):
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, radius_km)
    delta_x = distance * math.cos(angle)
    delta_y = distance * math.sin(angle)
    latitude = center_x + delta_x / 111
    longitude = center_y + delta_y / (111 * math.cos(center_x * math.pi / 180))
    return latitude, longitude

def check_zone(battello_x, battello_y):
    for zone_name, (zone_x, zone_y) in zones.items():
        if haversine(battello_x, battello_y, zone_x, zone_y) <= radius_km:
            return zone_name
    return None

def play_audio(zone_name):
    print(f"Il battello è nei pressi di: {zone_name}")
    audio_files = {
        "Trevignano": "Trevignano.wav",
        "Anguillara": "Anguillara.wav",
        "Bracciano": "Bracciano.wav"
    }
    audio_file = audio_files.get(zone_name)
    if audio_file:
        try:
            winsound.PlaySound(audio_file, winsound.SND_FILENAME)
        except Exception as e:
            print(f"Errore nella riproduzione audio: {e}")

def simulate_boat_journey():
    for _ in range(10):
        battello_x, battello_y = generate_random_coordinates(42.120, 12.230,5)
        print(f"Posizione del battello: ({battello_x}, {battello_y})")
        zone = check_zone(battello_x, battello_y)
        if zone:
            play_audio(zone)
            time.sleep(5)
        else:
            print("Il battello non è in una zona turistica.")
        time.sleep(3)

simulate_boat_journey()
