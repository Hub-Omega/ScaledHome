import RPi.GPIO as GPIO
from time import sleep
in1=17
in2=27
en1=21
en2=13
in3=5
in4=6
temp1=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(inl,GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enl,GPIO.OUT)
GPIO.output (in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output (in3, GPIO.LOW)
GPIO.output (in4, GPIO.LOW)
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)
p1. start (30)
p2.start (30)
i = 0
while(i < 10):
    if i>0:
        GPIO.output (in3,GPIO.HIGH)
        GPIO.output (in4, GPIO.LOW)
        sleep(1)
    GPIO.output (in3,GPIO. LOW)
    GPIO.output (in4, GPIO.LOW)
    sleep(90)
    GPIO.output (in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    sleep(1.5)
    GPIO.output (in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    i = i+1