from math import prod
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw

import sieves

DIMENSIONS = (400, 400)
WHITE = (0, 0, 255)
BLACK = (0, 0, 0)

RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)


def draw_primes_into_grid():

    MODE = "HSV"

    # def digit_colors(n=10):
    #     step = 255 // n
    #     return [(hue, 255, 200) for hue in range(0, 255, step)]

    image = Image.new(MODE, DIMENSIONS, BLACK)
    draw = ImageDraw.Draw(image)

    print(f"Getting primes up to {prod(DIMENSIONS)}")
    primes = sieves.sundaram(prod(DIMENSIONS))

    for prime in primes:
        row, column = divmod(prime, DIMENSIONS[0])
        last_digit = prime % 10
        draw.point((column, row), fill=WHITE)

    image.convert("RGB").save(RESULTS / "visualization.png")


# via https://scipython.com/blog/the-ulam-spiral/
def make_spiral(arr):
    nrows, ncols = arr.shape
    idx = np.arange(nrows * ncols).reshape(nrows, ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append(idx[0])
        # Remove the first row (the one we've just appended to spiral).
        idx = idx[1:]
        # Rotate the rest of the array anticlockwise
        idx = idx.T[::-1]
    # Make a flat array of indices spiralling into the array.
    spiral_idx = np.hstack(spiral_idx)
    # Index into a flattened version of our target array with spiral indices.
    spiral = np.empty_like(arr)
    spiral.flat[spiral_idx] = arr.flat[::-1]
    return spiral


def draw_test_spiral():
    hue = (np.arange(prod(DIMENSIONS)) / prod(DIMENSIONS)).reshape(DIMENSIONS)
    hues = make_spiral(hue)
    hsv = np.dstack((np.ones_like(hues), np.zeros_like(hues), 1 - hues)) * 255
    print(hsv.shape)
    image = Image.fromarray(hsv.astype("|u1"), mode="HSV")
    print(image)
    image.convert("RGB").save(RESULTS / "test_spiral.png")


def draw_primes_into_spiral():
    print(f"Getting primes up to {prod(DIMENSIONS)}")
    # TODO: we really want prod(DIMENSIONS) many primes
    primes = np.array(sieves.sundaram(prod(DIMENSIONS)))
    # Create an array of boolean values: 1 for prime, 0 for composite
    arr = np.zeros(prod(DIMENSIONS), dtype="u1")
    arr[primes - 1] = 1
    # Spiral the values clockwise out from the centre
    image_array = make_spiral(arr.reshape(DIMENSIONS))
    image = Image.fromarray(image_array * 255)
    image.save(RESULTS / "visualization_ulam_spiral.png")


if __name__ == "__main__":
    draw_primes_into_grid()
    draw_test_spiral()
    draw_primes_into_spiral()
