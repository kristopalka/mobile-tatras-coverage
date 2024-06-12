from api.api import *
from api.url_generators import *
from image_util import overlay_layers, create_map
from wmts_util import geo_to_wmts_coords


# lat lng zakopane
zakopane_coords = {
    'lat': 49.29114989248627,
    'lng': 19.948794440987104
}
zoom = 11

tile_coords = geo_to_wmts_coords(zakopane_coords, zoom)


image = create_map(tile_coords, generate_google_maps_url)
image = overlay_layers(image, create_map(tile_coords, generate_play_url))
image = overlay_layers(image, create_map(tile_coords, generate_tmobile_url))
image = overlay_layers(image, create_map(tile_coords, generate_o2_slovakia_url), alfa=0.5)


cv2.imshow('Fetched Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
