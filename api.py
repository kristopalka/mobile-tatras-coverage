def generate_play_url(coord):
    return f"https://internet.play.pl/maps-resources/tiles/cell_all/{coord['z']}/{coord['x']}/{1023 - coord['y']}.png"

def generate_google_maps_url(coord):
    return f"https://mt1.google.com/vt/x={coord['x']}&y={coord['y']}&z={coord['z']}"
