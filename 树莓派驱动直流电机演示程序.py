import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup（7,GPIO.OUT,initial=GPIO.LOW）//7号口用来控制驱动板

print("start!")
GPIO.output(7,GPIO.HIGH)
time.slee(60)//延时一分钟
GPIO.output(7,GPIO.LOW)
print("stop!")

GPIO.cleanup()