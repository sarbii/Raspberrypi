#! /usr/bin/env python

import roslib
import pigpio
import time
import threading
import RPi.GPIO as GPIO
import rospy
from sensor_msgs.msg import LaserScan


def laser_180callback(msg):
    #print (len(msg.ranges))
    if (msg.ranges[359] < 0.3 ):
        print ("stop")
    elif(msg.ranges[359]>12):
        print("trash")
    elif(msg.ranges[359]>0.3):
        print("driving")

def project():
    rospy.init_node('laser_180degree')
    sub = rospy.Subscriber('/scan',LaserScan,laser_180callback)
    rospy.spin()


project()
