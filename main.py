import cv2
import numpy as np
import requests

from api import *
from image_util import overlay_layers
from tiles import from_lat_lng_to_wmts_coord


def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()

    image_data = response.content
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    return cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)


# lat lng zakopane
zakopane_coords = {
    'lat': 49.29114989248627,
    'lng': 19.948794440987104
}
zoom = 10

tile_coords = from_lat_lng_to_wmts_coord(zakopane_coords, zoom)

try:
    google_maps_image = fetch_image(generate_google_maps_url(tile_coords))
    play_image = fetch_image(generate_play_url(tile_coords))

    image = overlay_layers(google_maps_image, play_image)

    cv2.imshow('Fetched Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except requests.HTTPError as e:
    print(f"Failed to fetch image: {e}")
