#!/usr/bin/env python3

import rospy
import getch

from std_msgs.msg import Char


def publisher():
    pub	= rospy.Publisher('keyboard_publish', Char, queue_size=10)

    rate	= rospy.Rate(1)

    msg_to_publish = Char()
    
    command = getch.getch()

    while not rospy.is_shutdown():
        command = getch.getch()
        
        char_to_publish = "Publishing %c"%command

        msg_to_publish.data = char_to_publish
        pub.publish(msg_to_publish)

        rospy.loginfo(char_to_publish)

        rate.sleep()


if __name__== "__main__":
    rospy.init_node("simple_publisher")
    publisher()




