#ZOOM 100% SCROLL TOP

from pynput.mouse import Button, Controller
import time
mouse = Controller()

days = 120 # 01 NOV - 20 APR
x = 0

time.sleep(5)
while x < days:
    #SAVE AS
    mouse.position = (678, 706)
    mouse.click(Button.left, 1)
    time.sleep(1.5)

    #MODEL RUN
    mouse.position = (339, 718)
    mouse.click(Button.left, 1)
    time.sleep(0.7)

    #NEXT DAY
    mouse.position = (194, 528) #For 00z: 223, 547 For 06z: 194, 528
    mouse.click(Button.left, 1)
    time.sleep(1.0)

    x = x+1
