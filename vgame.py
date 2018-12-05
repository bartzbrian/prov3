import RPi.GPIO as GPIO
import pygame, sys
import os
import random
from neopixel import *

LED_COUNT = 24
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_CHANNEL = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN) #blue
GPIO.setup(27,GPIO.IN) #green
GPIO.setup(22,GPIO.IN) #white


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path).convert()
                _image_library[path] = image
        return image

def set_neopixel(strip,state):
    if state == 0:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,0,255))
    elif state == 1:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(50,0,255))
    elif state == 2:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(100,0,200))
    elif state == 3:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(200,0,100))
    elif state == 4:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(255,0,0))
    elif state == 5:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(255,50,0))
    elif state == 6:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(200,150,0))
    elif state == 7:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(75,225,0))
    elif state == 8:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,255,0))
    elif state == 9:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,0,0))
    strip.show()

def check_buttons():
    blue = GPIO.input(17)
    green = GPIO.input(27)
    white = GPIO.input(22)
    if (blue == 1):
        return 'blue'
    if (green == 1):
        return 'green'
    if (white == 1):
        return 'white'
    if (blue == 0 and green == 0 and white == 0):
        return 'none'

def load_imgs():
    get_image('/home/pi/Desktop/vgame/startup.jpg')
    get_image('/home/pi/Desktop/vgame/decision_one_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_one.jpg')
    get_image('/home/pi/Desktop/vgame/decision_one_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_one_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_one_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_two_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_two.jpg')
    get_image('/home/pi/Desktop/vgame/decision_two_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_two_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_two_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_three_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_three.jpg')
    get_image('/home/pi/Desktop/vgame/decision_three_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_three_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_three_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_four_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_four.jpg')
    get_image('/home/pi/Desktop/vgame/decision_four_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_four_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_four_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_five_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_five.jpg')
    get_image('/home/pi/Desktop/vgame/decision_five_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_five_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_five_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_six_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_six.jpg')
    get_image('/home/pi/Desktop/vgame/decision_six_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_six_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_six_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_seven_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_seven.jpg')
    get_image('/home/pi/Desktop/vgame/decision_seven_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_seven_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_seven_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_eight_intro.jpg')
    get_image('/home/pi/Desktop/vgame/decision_eight.jpg')
    get_image('/home/pi/Desktop/vgame/decision_eight_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_nine.jpg')
    get_image('/home/pi/Desktop/vgame/decision_nine_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_nine_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_nine_green.jpg')
    get_image('/home/pi/Desktop/vgame/decision_ten.jpg')
    get_image('/home/pi/Desktop/vgame/decision_ten_blue.jpg')
    get_image('/home/pi/Desktop/vgame/decision_ten_white.jpg')
    get_image('/home/pi/Desktop/vgame/decision_ten_green.jpg')
    get_image('/home/pi/Desktop/vgame/afterwards_slide_one.jpg')
    get_image('/home/pi/Desktop/vgame/afterwards_slide_two.jpg')

if __name__ == '__main__':

    pygame.init()
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    load_imgs()

    done = False
    clock = pygame.time.Clock()
    current_image = '/home/pi/Desktop/vgame/startup.jpg'
    current_logo = '/home/pi/Desktop/vgame/logo0.png'
    changed_this_loop = True
    button_press_current = 'none'
    button_press_previous = 'none'
    changed_this_loop = False
    state = 9
    set_neopixel(strip,state)

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            
            screen.fill((255, 255, 255))
            button_press_current = check_buttons()
            
            if (current_image == '/home/pi/Desktop/vgame/startup.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_one_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo1.png'
                state = 0
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_one_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_one.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo1.png'
                state = 1
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_one.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_one_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_one.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_one_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_one.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_one_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_one_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_one_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_one_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_two_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo2.png'
                state = 1
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_two_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_two.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_two.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_two_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_two.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_two_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_two.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_two_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_two_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_two_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_two_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_three_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo3.png'
                state = 2
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_three_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_three.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_three.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_three_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_three.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_three_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_three.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_three_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_three_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_three_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_three_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_four_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo4.png'
                state = 3
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_four_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_four.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_four.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_four_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_four.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_four_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_four.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_four_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_four_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_four_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_four_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_five_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo5.png'
                state = 4
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_five_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_five.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_five.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_five_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_five.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_five_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_five.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_five_white.jpg'
                changed_this_loop = True   

            if ((current_image == '/home/pi/Desktop/vgame/decision_five_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_five_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_five_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_six_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo6.png'
                state = 5
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_six_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_six.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_six.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_six_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_six.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_six_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_six.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_six_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_six_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_six_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_six_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_seven_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo7.png'
                state = 6
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_seven_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_seven.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_seven.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_seven_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_seven.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_seven_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_seven.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_seven_white.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_seven_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_seven_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_seven_white.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_eight_intro.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo8.png'
                state = 7
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_eight_intro.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_eight.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_eight.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_eight_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_eight.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_ten.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_eight.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_nine.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_nine.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_nine_white.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_nine.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_nine_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_nine.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_nine_blue.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_ten.jpg' and button_press_current == 'white' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_ten_white.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_ten.jpg' and button_press_current == 'green' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_ten_green.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/decision_ten.jpg' and button_press_current == 'blue' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/decision_ten_blue.jpg'
                changed_this_loop = True

            if ((current_image == '/home/pi/Desktop/vgame/decision_eight_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_nine_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_nine_white.jpg' or current_image == '/home/pi/Desktop/vgame/decision_nine_blue.jpg' or current_image == '/home/pi/Desktop/vgame/decision_ten_white.jpg' or current_image == '/home/pi/Desktop/vgame/decision_ten_green.jpg' or current_image == '/home/pi/Desktop/vgame/decision_ten_blue.jpg') and button_press_current != 'none' and button_press_previous == 'none'  and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/afterwards_slide_one.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo9.png'
                state = 8
                set_neopixel(strip,state)
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/afterwards_slide_one.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/afterwards_slide_two.jpg'
                changed_this_loop = True

            if (current_image == '/home/pi/Desktop/vgame/afterwards_slide_two.jpg' and button_press_current != 'none' and button_press_previous == 'none' and not changed_this_loop):
                current_image = '/home/pi/Desktop/vgame/startup.jpg'
                current_logo = '/home/pi/Desktop/vgame/logo0.png'
                changed_this_loop = True
                state = 9
                set_neopixel(strip,state)


            button_press_previous = button_press_current
            screen.blit(get_image(current_image),(0,0))
            # screen.blit(get_image(current_logo),(910,25))
            changed_this_loop = False

            pygame.display.flip()
            clock.tick(20)
