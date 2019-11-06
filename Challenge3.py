from sense_hat import SenseHat
import numpy as np
from time import sleep
import random.py


def add_dangerous_pixels(sense, nr_dang_pix):
    dangerous_coord = []  # list where all the x,y coordinates are stored
    for i in range(0, nr_dang_pix):
        candidate_pixel = (random.randint(0, 7), random.randint(0, 7))
        dangerous_coord.append(candidate_pixel)
    return dangerous_coord


def check_boundary(x, y):
    
    if x<0:
        x = 0
    elif x > 7:
        x = 7
    elif y < 0:
        y = 0
    elif y > 7:
        y = 7
    return x, y


sense = SenseHat()
sense.clear()
number_of_dangerous_pixels = 4
dangerous_coord = add_dangerous_pixels(sense, number_of_dangerous_pixels)
r = (255, 0, 0)

# Adding dangerous pixels to the LED matrix:
for set in dangerous_coord:
    print(set)
    sense.set_pixel(set[0], set[1], r)

white = (255, 255, 255)
x, y = 6, 6  # location where the moving pixel is being ‘spawned’
sense.set_pixel(x, y, white)
# Set wining pixel
#
# Added code to generate “objective pixel”
goal_pixel = (random.randint(0, 7), random.randint(0, 7))

sense.set_pixel(goal_pixel[0], goal_pixel[1], 0, 255, 0)

alive = True  # flag to check where the moving pixel is located
while alive:
    for event in sense.stick.get_events():

        if event.direction == 'up':
            sense.set_pixel(x, y, 0, 0, 0)
        y -= 1
        x, y = check_boundary(x, y)
        sense.set_pixel(x, y, white)

        if event.direction == 'down':
            sense.set_pixel(x, y, 0, 0, 0)
        y += 1
        x, y = check_boundary(x, y)
        sense.set_pixel(x, y, white)

        if event.direction == 'left':
            sense.set_pixel(x, y, 0, 0, 0)
        x -= 1
        x, y = check_boundary(x, y)
        sense.set_pixel(x, y, white)

        if event.direction == 'right':
            sense.set_pixel(x, y, 0, 0, 0)
        x += 1
        x, y = check_boundary(x, y)
        sense.set_pixel(x, y, white)

        if (x, y) in dangerous_coord:
            sense.show_message('Game over')
        print('Game Over')
        alive = False  # Game is over, because you lost

        if (x, y) == (goal_pixel[0], goal_pixel[1]):
            sense.show_message('Victory')
        alive = False  # Game is over, because you won.
