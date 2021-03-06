import RPi.GPIO as GPIO
import LEDRGB as LED
import time 
import random 

from getpass import getpass
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin=32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
frequencies = [220, 440, 880, 1760]

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def validate_guess(color_string_seq, guess):
    if guess != color_string_seq:
        print "Gameover"
        print "The correct sequence was: ", color_string_seq
        LED.noColor()
        LED.destroy()
        exit()
    else:
        pass     

def loop():
    n = random.randint(0,3) 
    color_string = [colors[n]]
    freq_string = [frequencies[n]]
    while True:
        for i in range(len(color_string)):
            Buzz.ChangeFrequency(freq_string[i])
            Buzz.start(50)
            LED.setColor(color_string[i])
            time.sleep(0.5)
            Buzz.stop()
            LED.noColor()
            time.sleep(0.5)
        guess = getpass("What was the color sequence") 
        color_string_seq = ''.join(color_string)
        validate_guess(color_string_seq, guess.upper())
        n = random.randint(0,3)
        color_string.append(colors[n])
        freq_string.append(frequencies[n])
        time.sleep(0.5)   
            





if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        LED.destroy()
        print 'Good Bye'
