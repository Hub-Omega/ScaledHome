import RPi.GPIO as GPIO          
from time import sleep

in1 = 17
in2 = 27
en1 = 20
en2 = 13
in3 = 5
in4 = 6
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(en1,1000)
p2 = GPIO.PWM(en2,1000)
 
##
p1.start(30)
##p2.start(30)
##GPIO.output(in3,GPIO.HIGH)
##GPIO.output(in4,GPIO.LOW)
##sleep(4)
##GPIO.output(in3,GPIO.LOW)
##GPIO.output(in4,GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while(1):
    x=input()
    if x=='r':
        print("run")
        if(temp1==1):
         p1.ChangeDutyCycle(25)
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         p1.ChangeDutyCycle(30)
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'

    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='b':
        print("backward")
        p1.ChangeDutyCycle(30)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'
    elif x=='f':
        print("forward")
        p1.ChangeDutyCycle(25)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(5)
        x='z'

    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(75)
        x='z'
        
    elif x == 'd':
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        sleep(3)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
