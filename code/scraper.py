#ZOOM 100% SCROLL TOP

from pynput.mouse import Button, Controller
import time
mouse = Controller()

days = 181 # 01 NOV - 01 MAY
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
    time.sleep(0.5)

    #NEXT DAY
    mouse.position = (223,547) #For 00z: 223,547 For 06z: 194, 528
    mouse.click(Button.left, 1)
    time.sleep(0.7)

    x = x+1
