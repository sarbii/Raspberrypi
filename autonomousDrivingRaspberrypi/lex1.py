#! /usr/bin/env python

import threading
import time
import RPi.GPIO as GPIO
import roslib
import rospy
from sensor_msgs.msg import LaserScan

GPIO.setmode(GPIO.BCM)

def ultra1():

    GPIO_TRIGGER1 = 23
    GPIO_ECH01 = 24

    print("Ultrasonic Distance Measurement")

    GPIO.setup(GPIO_TRIGGER1,GPIO.OUT)
    GPIO.setup(GPIO_ECHO1,GPIO.IN)
    try:
        while True:
            stop1 = 0
            start1 = 0
            GPIO.output(GPIO_TRIGGER1, False)
            time.sleep(0.1)

            GPIO.output(GPIO_TRIGGER1, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER1, False)

            while GPIO.input(GPIO_ECHO1)==0:
                start1 = time.time()
            while GPIO.input(GPIO_ECHO1)==1:
                stop1 = time.time()

            elapsed1 = stop1-start1

            if(stop1 and start1):
                distance1 = (elapsed*34000.0) / 2
                print("Sonic 1 Distance : %.1f cm" % distance1)

def callback(msg):
    print (len(msg.ranges))

def outing():
    rospy.init_node('laser_readings',anonymous=True)
    sub = rospy.Subscriber('/scan',LaserScan,callback)
    rospy.spin()

if __name__ == '__main__':
    outing():
        
GPIO.cleanup()
