#!/usr/bin/env python


from udm_gb.srv import *
import rospy
import rosservice
from std_srvs.srv import Empty
import time

"""
def handle_req(req):
    c=int(req.a.data)

    #rosservice.call_service('/global_localization',True)
    #for x in range(c):	
    #	rosservice.call_service('/request_nomotion_update',True)
    rospy.wait_for_service('global_localization') 
    rospy.wait_for_service('request_nomotion_update')
    try:
        #global_localization = rospy.ServiceProxy('global_localization', Empty) 
        #response = global_localization()
        #print(response)
	request = rospy.ServiceProxy('request_nomotion_update', Empty)
        for x in range(c):
            request()
            print(resp)
	    print("index" + str(x))		
	rep=udm_serviceResponse()
    	rep.res.data=True
    	return rep      
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

    
def simple_server():
    rospy.init_node('global_localization_Service')
    s = rospy.Service('global_localization_Service', udm_service, handle_req)
    rospy.spin()
"""

if __name__ == "__main__":
    rospy.init_node('global_localization_Service')
    rospy.wait_for_service('global_localization') 
    rospy.wait_for_service('request_nomotion_update')
    global_localization = rospy.ServiceProxy('global_localization', Empty) 
    global_localization()
    print("global_localization done !")
    time.sleep(1)
    request = rospy.ServiceProxy('request_nomotion_update', Empty)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()
    time.sleep(0.5)
    request()    
    print("request_nomotion_update done !") 
