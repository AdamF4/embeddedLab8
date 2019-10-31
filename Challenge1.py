from sense_hat import SenseHat
from time import sleep


def clear_leds(sense):
    sense.clear()
    # Reset the values of the sensehat to 0


sense = SenseHat()
clear_leds(sense)
# Insert code HERE ##
# Commands for image
R = [255, 255, 0]  # Red
G = [0, 255, 0]  # green
B = [0, 0, 255]  # blue
O = [0, 0, 0]  # black

smile = [
    O, O, O, O, O, O, O, O,
    O, O, R, O, O, G, O, O,
    O, O, R, O, O, G, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, B, O, O, O, O, B, O,
    O, O, B, B, B, B, O, O,
    O, O, O, O, O, O, O, O
]

sense.set_pixels(smile)
# Added code ends HERE ##

# sense.flip_v()

angle = 0

while True:
    if angle > 270:
        angle = 0
    sense.set_rotation(angle)
    sleep(1)
    angle += 90
