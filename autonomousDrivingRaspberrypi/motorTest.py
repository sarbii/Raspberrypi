#!/usr/bin/env python

from subprocess import call
call("sudo pigpiod", shell=True)
import pigpio
import pygame
import RPi.GPIO as GPIO
import time
import rospy
import roslib
from sensor_msgs.msg import LaserScan
GPIO.setmode(GPIO.BCM)

pi = pigpio.pi()

ESC_GPIO = 17
Servo_GPIO = 26


#GPIO.setup(GPIO_LIGHT,GPIO.OUT)


center_position = 1500
dc = 1545

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
    
def laser_180callback(msg):
    #print (len(msg.ranges))
    if (msg.ranges[359] < 2 ):
        print ("stop")
        pi.set_servo_pulsewidth(ESC_GPIO, 0)
    elif(msg.ranges[359]>12):
        print("trash")
        pi.set_servo_pulsewidth(ESC_GPIO, 0)
    elif(msg.ranges[359]>0.3):
        print("driving")
        pi.set_servo_pulsewidth(ESC_GPIO, dc)

try:
    doAngle(stand)
    doPosition(dc)

 
    rospy.init_node('laser_180degree')
    sub = rospy.Subscriber('/scan',LaserScan,laser_180callback)
    rospy.spin()      
        
       
            
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(Servo_GPIO, 0)
    pi.set_servo_pulsewidth(ESC_GPIO, 0)

