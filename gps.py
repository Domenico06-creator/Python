from math import radians, sin, cos, sqrt, atan2 #radians per convertire i gradi in radianti, sin e cos seno e coseno,
#sqrt radice quadrata, atan2 arcotangente

def distanza(latitudine1, longitudine1, latitudine2, longitudine2):
    R = 6371  # Raggio della Terra in km
    latitudine1, longitudine1, latitudine2, longitudine2 = map(radians, [latitudine1, longitudine1, latitudine2, longitudine2])
    distanzalat = latitudine2-latitudine1
    distanzalon = longitudine2-longitudine1
    a=sin(distanzalat/2)**2+cos(latitudine1) * cos(latitudine2) * sin(distanzalon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c
#

# Inserimento dati
latitudine1 = float(input("Latitudine1: "))
longitudine1 = float(input("Longitudine1: "))
latitudine2 = float(input("Latitudine2: "))
longitudine2 = float(input("Longitudine2: "))

# Stampa risultato
print("Distanza:", round(distanza(latitudine1, longitudine1, latitudine2, longitudine2), 2), "km")
   
