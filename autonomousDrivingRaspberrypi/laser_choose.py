#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_180callback(msg):
    #print (len(msg.ranges))
    print (msg.ranges[359])
rospy.init_node('laser_180degree')
sub = rospy.Subscriber('/scan',LaserScan,laser_180callback)
rospy.spin()
