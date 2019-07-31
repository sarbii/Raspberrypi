from subprocess import call
call("sudo pigpiod", shell=True)
import pygame
import RPi.GPIO as GPIO
import pigpio
import time
import getCh

GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()

ESC_GPIO = 17
Servo_GPIO = 26

center_position = 1500
dc = 1500

center_angle = 1560
stand = 1560

def doAngle(angle):
    pi.set_servo_pulsewidth(Servo_GPIO, (angle))
    print ("Angle: %f" % angle)
    time.sleep(0.1)
    
def doPosition(position):
    pi.set_servo_pulsewidth(ESC_GPIO, (position))
    print ("Position: %f" % position)
    time.sleep(0.1)

try:
    doAngle(stand)
    doPosition(dc)
    while True:
        var = getCh.getch()
        if var == 'D' or var == 'd':
            print ("Right")
            stand = stand+10
            doAngle(stand)
        elif var == 'A' or var == 'a':
            print ("Left")
            stand= stand-10
            doAngle(stand)
        elif var == 'C' or var == 'c':
            print ("Center")
            doAngle(center_angle)
            
        elif var == 'W' or var == 'w':
            print ("Forward")
            dc= dc+5
            doPosition(dc)
        elif var == 'S' or var == 's':
            print ("Stop")
            dc= dc-5
            doPosition(dc)
        elif var == 'V' or var == 'v':
            print ("Center positon")
            doPosition(center_position)
            
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(Servo_GPIO, 0)
    pi.set_servo_pulsewidth(ESC_GPIO, 0)

