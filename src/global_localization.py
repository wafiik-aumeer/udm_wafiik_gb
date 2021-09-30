#!/usr/bin/env python


from udm_group2_gb.srv import *
import rospy
import rosservice
from std_srvs.srv import Empty

def handle_req(req):
    c=int(req.a.data)

    #rosservice.call_service('/global_localization',True)
    #for x in range(c):	
    #	rosservice.call_service('/request_nomotion_update',True)
    rospy.wait_for_service('global_localization') 
    rospy.wait_for_service('request_nomotion_update')
    try:
	
        global_localization = rospy.ServiceProxy('global_localization', Empty) 
	resp = global_localization()
	print(resp)
	for x in range(c):
	   rospy.ServiceProxy('request_nomotion_update', Empty)
	   print("index" + str(x))		
	rep=udm_serviceResponse()
    	rep.res.data=True
    	return rep      
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

    
def simple_server():
    rospy.init_node('global_localization_service')
    s = rospy.Service('global_localization_Service', udm_service, handle_req)
    rospy.spin()

if __name__ == "__main__":
    simple_server() 
