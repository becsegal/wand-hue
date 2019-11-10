import time
from hue import Hue
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pressed = False
hue = Hue()

while True: # Run forever
  if GPIO.input(10) == GPIO.HIGH and not(pressed) :
    pressed = True
    print("Pressed -- toggle")
    hue.toggle()
  elif GPIO.input(10) == GPIO.LOW and pressed :
    pressed = False
    print("Released")
  time.sleep(0.1)