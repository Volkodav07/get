import RPi.GPIO as GPIO
from time import sleep

num = [0, 0, 0, 0, 0, 0, 0, 0]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
dec_num = 255
for i in range(7, -1, -1):
    if dec_num >= 2**i:
        num[7-i] = 1
        dec_num -= 2**i

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()