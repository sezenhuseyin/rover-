#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import fonx_file



def execute(data):   #kodu alıp anlamlı sayılar haline getirip publishliyor.
    all_result_str=""
    for i in range(1,len(data.data)-1,1):
        if i%4==1:
            result_str=""
        result_str= result_str+data.data[i]
        if i%4==0:
            all_result_str= all_result_str +fonx_file.gercekSayi(result_str)+" "
            
    rospy.loginfo(all_result_str)
    pub = rospy.Publisher('/position/drive',String,queue_size=10)
    rate = rospy.Rate(10)
    pub.publish(all_result_str)
    rate.sleep()    
    
          

y=fonx_file.Yap()
if __name__=='__main__':
    y.listener('subs_16e','/serial/execute16',execute)
