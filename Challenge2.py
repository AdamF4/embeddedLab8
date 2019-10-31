from sense_hat import SenseHat
from time import sleep
from PIL import Image
import numpy as np


def load_image(values,sense):
    # sense.set_pixels(values)
    sense.load_image(path_to_file)


def clear_leds(sense):
    sense.clear()


path_to_file = "Pokeball.jpg"
im = Image.open(path_to_file)
rgb_im = im.convert('RGB')
values = np.array(rgb_im)
sense = SenseHat()
clear_leds(sense)
load_image(values, sense)
sense.flip_v()
sense.set_rotation(270)
