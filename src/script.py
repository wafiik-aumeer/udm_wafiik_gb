#!/bin/python

import sys
import rospy
from std_srvs.srv import Empty


rospy.init_node('node_name')
rospy.wait_for_service("global_localization")
rospy.wait_for_service("request_nomotion_update")
r = rospy.Rate(10)

global_localise = rospy.ServiceProxy("/global_localization", Empty)
global_localise()
nomotion = rospy.ServiceProxy("/request_nomotion_update",Empty)


x = int(sys.argv[1])

for i in range(x):
    nomotion()
    r.sleep()
