#!python3
# file: led_clock.py
import LEDarcade as LED
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import random
#Variable declaration section
ScrollSleep   = 0.025
HatHeight = 32
HatWidth  = 64


#--------------------------------------
#  SHOW CLOCKS                       --
#--------------------------------------

while 1==1:

    #This allows you to create a title screen with different size text
    #some scrolling text, an animation and even a nice fade to black


    #Starry Night Clock
    if(LED.HatWidth > 64):
      ZoomFactor = 3

    else:
      ZoomFactor = 2


    LED.DisplayDigitalClock(ClockStyle=3,CenterHoriz=True,v=1, hh=24, ZoomFactor = ZoomFactor, AnimationDelay=10, RunMinutes = 5 )