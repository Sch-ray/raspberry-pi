#!/usr/bin/env python
#!/-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import pygame
import time
import datetime

GPIO.setmode(GPIO.BOARD)

bin_high=[13,15]
GPIO.setup(bin_high,GPIO.OUT,initial=GPIO.HIGH)
#11,12
bin_low=[16,18,22,29,31,32,33,35,36,37,38,40]
GPIO.setup(bin_low,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init()
pygame.mixer.music.load('getup.mp3')

D_zero=[31,32,33,35,36,37]
D_one=[32,33]
D_two=[31,32,35,36,38]
D_three=[31,32,33,35,38]
D_four=[32,33,37,38]
D_five=[31,33,35,37,38]
D_six=[31,33,35,36,37,38]
D_seven=[31,32,33]
D_eight=[31,32,33,35,36,37,38]
D_nine=[31,32,33,35,37,38]

D_list=[D_zero,D_one,D_two,D_three,D_four,D_five,D_six,D_seven,D_eight,D_nine]

def display(wei,num):
    GPIO.output(wei,GPIO.HIGH)
    num_n=D_list[num]
    for i in num_n:
        GPIO.output(i,GPIO.LOW)
        time.sleep(0.0005)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.0005)
    GPIO.output(wei,GPIO.LOW)

def xianshi(shi,feng):
    shi_o=shi//10
    shi_t=shi%10
    feng_o=feng//10
    feng_t=feng%10
    display(16,shi_o)
    display(18,shi_t)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(40,GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(40,GPIO.HIGH)
    display(22,feng_o)
    display(29,feng_t)

#def fan(num):
#    GPIO.output(11,GPIO.HIGH)
#    GPIO.output(12,GPIO.LOW)
#    time.sleep(num)
#    GPIO.output(11,GPIO.LOW)
#    GPIO.output(13,GPIO.LOW)

def light(num):
	GPIO.output(13,GPIO.LOW)
	time.sleep(num)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	time.sleep(num)
	GPIO.output(13,GPIO.LOW)
	time.sleep(num)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)

hour=input('Input alarm clock hour:')
minute=input('Input alarm clock minute:')
print('The program is running...')
while True:
	now_hour= datetime.datetime.now().strftime('%H')
	now_minute= datetime.datetime.now().strftime('%M')
	nowh=int(now_hour)
	nowm=int(now_minute)
	xianshi(nowh,nowm)
	if hour == now_hour and minute == now_minute:
		print('Now time is '+now_hour+':'+now_minute+'!')
		pygame.mixer.music.play()
		sign=0
		while True:
                    if GPIO.input(7)==1:
                        print('The alarm clock closes!')
                        sign=1
                        break
                    else:
                        light(0.3)
		if sign==1:
                    break

time.sleep(1)
while True:
    now_hour= datetime.datetime.now().strftime('%H')
    now_minute= datetime.datetime.now().strftime('%M')
    nowh=int(now_hour)
    nowm=int(now_minute)
    xianshi(nowh,nowm)
    if GPIO.input(7)==1:
        print('End of the program!')
        GPIO.cleanup()
        exit(0)