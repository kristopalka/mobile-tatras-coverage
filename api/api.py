import cv2
import numpy as np
import requests

from wmts_util import TILE_SIZE


def fetch_image(url):
    try:
        print(f"Fetching {url}...")
        response = requests.get(url)
        response.raise_for_status()

        image_array = np.frombuffer(response.content, dtype=np.uint8)
        return cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)

    except requests.HTTPError:
        return np.zeros((TILE_SIZE, TILE_SIZE, 4), dtype=np.uint8)


