#!/usr/bin/env python
#-*-coding: utf-* -*-

import rospy
from std_msgs.msg import String
import fonx_file


def yazdir(data):   #veriler doğru publishlenmiş mi diye kontrol ettiğim yer.
	rospy.loginfo(data.data)


y=fonx_file.Yap()
y.listener('deneme_robotic_arm','/position/robotic_arm',yazdir)
 
