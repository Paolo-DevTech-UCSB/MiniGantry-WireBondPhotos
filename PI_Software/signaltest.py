import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
  
g = 3000; laststate = 1;
for i in range(g):
    
    #print(i)
    state = GPIO.input(26);
    if laststate == 0 & state == 1:
        x = x + 1;
        print(x)
    print(state)
    time.sleep(0.1)
    laststate = state;