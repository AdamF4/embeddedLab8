from sense_hat import SenseHat
import time
sense = SenseHat()

flashTime = 0
flashState = False

green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

state = "none"  # what the current state is

lastDetect = 0  # time the last detection was made

raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))
accl = max(max(raw["x"], raw["y"]), raw["z"])

thres = {
    "mild": 2,
    "XTREME": 3
}
timeOut = {
    "mild": 3,
    "XTREME": 10,
}

if accl > thres["XTRREME"]:
    state = "XTREME"
    lastDetect = time.time()

elif state != "XTREME" and accl > thres["mild"]:
    state = "mild"
    lastDetect = time.time()

if lastDetect + timeOut[state] > time.time():
    state = "none"


def flash(colour):
    global flashTime
    global flashState
    if time.time() > flashTime:
        if flashState:
            sense.clear()
            flashState = False
        else:
            sense.clear(colour)
            flashState = True
        flashTime = time.time()


if state == "none":
    sense.clear(green)
elif state == "mild":
    flash(yellow)
elif state == "XTREME":
    flash(red)
