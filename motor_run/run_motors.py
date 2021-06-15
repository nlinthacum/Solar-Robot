#!/usr/bin/env python3

import rospy
from time import sleep
import RPi.GPIO as GPIO
from std_msgs.msg import String



def subscriber():
	sub = rospy.Subscriber('keyboard_publish', String, callback_function)
	rospy.spin()

def callback_function(message):
	command = message.data
	
	if command == 'w':
		forward_motor()
		rospy.loginfo("forward")

def forward_motor():
	print("I'm going forward")


if __name__ == "__main__":
	rospy.init_node("keyboard_subscriber")
	subscriber()


	
	

