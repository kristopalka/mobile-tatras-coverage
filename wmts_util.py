import math

TILE_SIZE = 256


def geo_to_point(geo_coords):
    mercator = -math.log(math.tan((0.25 + geo_coords['lat'] / 360) * math.pi))
    return {
        'x': TILE_SIZE * (geo_coords['lng'] / 360 + 0.5),
        'y': TILE_SIZE / 2 * (1 + mercator / math.pi)
    }


def geo_to_wmts_coords(geo_coords, zoom):
    point = geo_to_point(geo_coords)
    scale = 2 ** zoom

    return {
        'x': int(point['x'] * scale / TILE_SIZE),
        'y': int(point['y'] * scale / TILE_SIZE),
        'z': zoom
    }
