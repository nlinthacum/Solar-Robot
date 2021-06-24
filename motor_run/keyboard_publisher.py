#!/usr/bin/env python3

import rospy
import getch

from std_msgs.msg import Char
from std_msgs.msg import String


def publisher():
    pub	= rospy.Publisher('keyboard_publish', String, queue_size=1)

    rate	= rospy.Rate(50) #should be 1 hz

    msg_to_publish = Char()
    
    

    while not rospy.is_shutdown():
        command = getch.getch()
    
        
        char_to_publish = "Publishing %c"%command

      #  msg_to_publish.data = char_to_publish
        pub.publish(command)

        rospy.loginfo(command)

        rate.sleep()


if __name__== "__main__":
    rospy.init_node("keyboard_publisher")
    publisher()




