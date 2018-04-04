import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
for bin in [16,18,22,29]:
    GPIO.setup(bin,GPIO.OUT,initial=GPIO.LOW)
for bi in [31,32,33,35,36,37,38,40]:
    GPIO.setup(bi,GPIO.OUT,initial=GPIO.HIGH)

D_zero=[31,32,33,35,36,37]
D_one=[32,33]
D_two=[31,32,35,36,38]
D_three=[31,32,33,35,38]
D_four=[32,33,37,38]
D_five=[31,33,35,37,38]
D_six=[31,33,35,36,37,38,40]
D_seven=[31,32,33]
D_eight=[31,32,33,35,36,37,38]
D_nine=[31,32,33,35,37,38]

D_list=[D_zero,D_one,D_two,D_three,D_four,D_five,D_six,D_seven,D_eight,D_nine]

def display(wei,num):
    GPIO.output(wei,GPIO.HIGH)
    num_n=D_list[num]
    for i in num_n:
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.0001)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.0001)
    GPIO.output(wei,GPIO.LOW)

def xianshi(shi,feng):
    shi_o=shi//10
    shi_t=shi%10
    feng_o=feng//10
    feng_t=feng%10
    display(16,shi_o)
    display(18,shi_t)
    display(22,feng_o)
    display(29,feng_t)
    
while True:
    now_h=datetime.datetime.now().strftime('%H')
    now_m=datetime.datetime.now().strftime('%M')
    nowh=int(now_h)
    nowm=int(now_m)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(40,GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(40,GPIO.HIGH)
    xianshi(nowh,nowm)

GPIO.cleanup()