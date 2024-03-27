import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(len(dac))]

def dac_data(data):
    signal = dec2bin(data)
    GPIO.output(dac, signal)
    return signal

try:
    period = float(input("Type a period for sygnal: "))
    while True:
        for i in range(256):
            dac_data(i)
            time.sleep(period / 512)
        for i in range(255, -1, -1):
            dac_data(i)
            time.sleep(period / 512)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
