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


def flash(colour):
        global flashTime
        global flashState
        if time.time() > 0.25 + flashTime:
            #print(time.time()-flashTime)
            if flashState:
                sense.clear()
                flashState = False
            else:
                sense.clear(colour)
                flashState = True
            flashTime = time.time()

thres = {
    "mild": 1,
    "XTREME": 1.5
}
timeOut = {
    "mild": 3,
    "XTREME": 10,
}
while True:
    raw = sense.get_accelerometer_raw()

    accl = max(max(abs(raw["x"]), abs(raw["y"])), abs(raw["z"]))
    ##print(accl)
    if accl >= thres["XTREME"]:
        state = "XTREME"
        lastDetect = time.time()

    elif state != "XTREME" and accl >= thres["mild"]:
        state = "mild"
        lastDetect = time.time()
    ##print(state)    
    if state != "none":
        if lastDetect + timeOut[state] < time.time():
            state = "none"
    ##print(state)
    if state == "none":
        sense.clear(green)
    elif state == "mild":
        flash(yellow)
    elif state == "XTREME":
        flash(red)
