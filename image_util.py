import numpy as np

from api.api import fetch_image


def overlay_layers(background, image, alfa=0.2):
    if background.shape[:2] != image.shape[:2]:
        raise ValueError("Sizes of layers are not the same")

    image_colors = image[:, :, :3]
    image_mask = alfa * image[:, :, 3] / 255.0

    out = np.zeros(background.shape[:], dtype=background.dtype)
    for c in range(0, 3):
        out[:, :, c] = background[:, :, c] * (1 - image_mask) + image_colors[:, :, c] * image_mask

    return out


def create_map(center_tile_coords, url_generator, grid_size=(5, 5)):
    rows, cols = grid_size
    tile = fetch_image(url_generator(center_tile_coords))
    size = tile.shape[0]
    depth = tile.shape[2]

    map_image = np.zeros((rows * size, cols * size, depth), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            coords = {
                'x': center_tile_coords['x'] + j - round((cols - 1) / 2),
                'y': center_tile_coords['y'] + i - round((rows - 1) / 2),
                'z': center_tile_coords['z']
            }

            tile = fetch_image(url_generator(coords))
            map_image[i * size:(i + 1) * size, j * size:(j + 1) * size] = tile

    return map_image
