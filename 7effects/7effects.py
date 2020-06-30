
//For More Info : https://albtronics.wordpress.com/

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def effect_1():
    for i in range(2,10):
        GPIO.setup(i,GPIO.OUT)

    for i in range(2,10):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.02)

def effect_2():
    for i in range(2,10):
        GPIO.setup(i,GPIO.OUT)

    for i in range(2,10):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
    
    for i in range(2,10):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.02)

def effect_3():
    for i in range(2,10):
        GPIO.setup(i,GPIO.OUT)

    for i in range(2,10):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
        
    for i in range(2,10):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.1)

def effect_4():
    for i in range(2,10):
        GPIO.setup(i,GPIO.OUT)

    for i in range(2,10):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.2)
    
    for i in range(2,10):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.2)
         
def effect_5():#10 to 2 backwards....
    for i in range(2,11):
        GPIO.setup(i,GPIO.OUT)

    for i in range(10,1,-1):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.02)
    
    for i in range(10,1,-1):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.02)

def effect_6():
    for i in range(2,11):
        GPIO.setup(i,GPIO.OUT)

    for i in range(10,1,-1):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.08)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.05)
        
    for i in range(10,1,-1):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.08)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.05)
 
def effect_7():
    for i in range(2,11):
        GPIO.setup(i,GPIO.OUT)

    for i in range(2,10):
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.08)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.05)
        
    for i in range(2,10):
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.08)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.05)
 
while True:
    effect_1()
    effect_1()
    effect_1()
    effect_1()
    effect_1()
    
    effect_2()
    effect_2()
    effect_2()
    
    effect_3()
    effect_3()
    
    effect_4()
    effect_4()
    
    effect_5()
    effect_5()
    
    effect_6()
    effect_6()
    
    effect_7()
    effect_7()
 
 #Combined effects
    effect_1()
    effect_5()
    effect_1()
    effect_5()
    effect_4()
    effect_5()
    effect_6()
    effect_7()
    effect_1()

