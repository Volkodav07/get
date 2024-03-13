import RPi.GPIO as GPIO
from time import sleep

num = []
dac = [8, 11, 7, 1, 0, 5, 12, 6]
dec_num = 255
while dec_num: 
    num.append(dec_num % 2)
    dec_num // 2
num.reverse()

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()