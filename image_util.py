import numpy as np


def overlay_layers(background, image, alfa=0.2):
    if background.shape[:2] != image.shape[:2]:
        raise ValueError("Sizes of layers are not the same")

    image_colors = image[:, :, :3]
    image_mask = alfa * image[:, :, 3] / 255.0

    out = np.zeros(background.shape[:], dtype=background.dtype)
    for c in range(0, 3):
        out[:, :, c] = background[:, :, c] * (1 - image_mask) + image_colors[:, :, c] * image_mask

    return out
