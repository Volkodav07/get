import RPi.GPIO as GP
GP.setmode(GP.BCM)  

GP.setup(24, GP.OUT)
GP.setup(23, GP.IN)

a = GP.input(23)
GP.output(24, a)
