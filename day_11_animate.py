import os

import day_11
import display
from PIL import Image

root = os.path.join(os.getcwd(), 'images')


def load_images_starting_with(prefix):
    imgs = []
    root = os.path.join(os.getcwd(), 'images')
    for f in sorted(os.listdir(root)):
        if f.startswith(prefix):
            im = Image.open(os.path.join(root, f))
            imgs.append(im)
    return imgs

imgs = load_images_starting_with("test_")
im_copy = imgs[0].copy()
imgs[0].save("jason.gif", save_all=True, append_images=imgs[1:], duration=5)