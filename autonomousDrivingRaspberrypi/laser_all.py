#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(msg):
    print (len(msg.ranges))

rospy.init_node('laser_readings')
sub = rospy.Subscriber('/scan',LaserScan,laser_callback)
rospy.spin()
