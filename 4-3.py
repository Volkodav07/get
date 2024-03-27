import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwm_pin = 24
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 1000) 
pwm.start(0) 

try:
    while True:
        duty_cycle = float(input("Введите коэффициент заполнения (0-100): "))
        pwm.ChangeDutyCycle(duty_cycle)

        voltage = 3.3 * duty_cycle / 100  
        print(f"Предполагаемое значение напряжения: {voltage} В")
finally:
    pwm.stop()
    GPIO.cleanup()