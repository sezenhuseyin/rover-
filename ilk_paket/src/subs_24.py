#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import fonx_file

def kontrolEt(data):    #verinin başındaki ve sonundaki harfleri kontrol ediyor bu harfler sırasıyla A ve B değilse veriyi almıyor 
    rospy.loginfo(data.data)
    if data.data[0]=="A":
        if data.data[len(data.data)-1]=="B":

            pub = rospy.Publisher('serial/execute24',String,queue_size=10)  
           
            rate = rospy.Rate(10)  
		
            pub.publish(data.data)
            rate.sleep()
            
y=fonx_file.Yap()
if __name__=='__main__':
    y.listener('subs_24','/serial/robotic_arm',kontrolEt)
