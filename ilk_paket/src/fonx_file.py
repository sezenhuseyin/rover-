#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def gercekSayi(a):
    b= int(a)
    if b <1000:
        if b>=0:
            if b<=255:
                return str(b)
            else:
                return "255"
    if b>1000:
        b= b-1000
        if b>=0:
            if b<=255:
                b= b*(-1)
                return str(b)
            else:
                return "-255"
class Yap():
    
    
    
    def listener(self,a,b,c):
        
            rospy.init_node(a,anonymous=False)
            rospy.Subscriber(b,String,c)
            rospy.spin()
        
        