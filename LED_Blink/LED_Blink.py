print("a l b t r o n i c s . c o m")
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time   
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
while True: # Run forever
 GPIO.output(40, GPIO.HIGH) # Turn on
 time.sleep(0.1) 
 GPIO.output(40, GPIO.LOW) # Turn off
 time.sleep(0.2) 
