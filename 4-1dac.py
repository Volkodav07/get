import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def int_to_bin(num):
    return [int(i) for i in bin(num)[2:].rjust(8, '0')]

try: 
    num = int_to_bin(int(input()))
    GPIO.output(dac, num)
    print(int("".join([str(i) for i in num]), 2)*(3.3/256))
    time.sleep(20)

except KeyboardInterrupt:
    print()
    pass

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()