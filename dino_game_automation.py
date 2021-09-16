import pyautogui
import time
from PIL import ImageGrab
import numpy

#some of these values may vary based on your device
relativeToActualScreenDimensionsRatio = 2
x = 488 * relativeToActualScreenDimensionsRatio
y = 294 * relativeToActualScreenDimensionsRatio
a = 200 * relativeToActualScreenDimensionsRatio
defaultColorValue = 647

def CheckImage(screenshot):
    array = numpy.array(screenshot.getcolors())
    if array.sum() != defaultColorValue:
        return True
    else:
        return False

time.sleep(2)

while True:
    screenshot = ImageGrab.grab((x, y, x + a, y + 1)).convert("L")
    if CheckImage(screenshot) == True:
        pyautogui.press("space")
