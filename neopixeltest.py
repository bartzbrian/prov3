import random
from neopixel import *
import time

LED_COUNT = 24
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 150
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
state = 0

def set_neopixel(strip, state):
    if state == 0:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(25,150),0,255))
    if state == 1:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(50,175),0,random.randint(75,255)))
    if state == 2:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(75,255),0,random.randint(25,150)))
    if state == 3:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(255,0,random.randint(25,125)))
    if state == 4:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(255,random.randint(75,200),0))
    if state == 5:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(75,175),random.randint(125,225),0))
    if state == 6:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(25,150),255,0))
    if state == 7:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(25,75),255,0))
    if state == 8:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(random.randint(0,25),255,0))
    strip.show()


while True:
    if state == 9:
       state = 0
    print state
    set_neopixel(strip,state)
    state += 1
    time.sleep(5)

