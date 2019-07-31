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


center_position = 1500
dc = 1555

center_angle = 1560


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
    if (3 < msg.ranges[359] < 4.2 ):
        print ("stop")
        pi.set_servo_pulsewidth(ESC_GPIO, 1500)
        time.sleep(0.1)
        pi.set_servo_pulsewidth(ESC_GPIO, 1440)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(ESC_GPIO, 1500)

    elif (msg.ranges[359] < 3 ):
        print ("stop")
        pi.set_servo_pulsewidth(ESC_GPIO, 1500)
        time.sleep(0.1)


    elif(msg.ranges[359] >4):
        print("driving")
        pi.set_servo_pulsewidth(ESC_GPIO, dc)


        if (msg.ranges[315] < 1 ):
            print ("left_weak")
            pi.set_servo_pulsewidth(Servo_GPIO, 1430)
            time.sleep(0.05)
            pi.set_servo_pulsewidth(Servo_GPIO, center_angle)
            pi.set_servo_pulsewidth(ESC_GPIO, 1540)

            time.sleep(0.03)

        if (msg.ranges[45] < 1 ):
            print ("right_weak")
            pi.set_servo_pulsewidth(Servo_GPIO, 1690)
            time.sleep(0.05)
            pi.set_servo_pulsewidth(Servo_GPIO, center_angle)

            pi.set_servo_pulsewidth(ESC_GPIO, 1540)
 
            time.sleep(0.03)
try:
    doAngle(center_angle)
    doPosition(center_position)
 
    rospy.init_node('laser_180degree')
    sub = rospy.Subscriber('/scan',LaserScan,laser_180callback)
    rospy.spin()      
            
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(Servo_GPIO, 0)
    pi.set_servo_pulsewidth(ESC_GPIO, 0)
