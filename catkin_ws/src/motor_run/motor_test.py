#!/usr/bin/env python3
import rospy
from time import sleep
import RPi.GPIO as GPIO
from std_msgs.msg import Char

def subscriber():
	sub = rospy.Subscriber('keyboard_publish', Char, callback_function)
	
	rospy.spin()

def callback_function(message):
	rospy.loginfo("I received: %s"%message.data)

if __name__ == "__main__":
	rospy.init_node("keyboard_subscriber")
	subscriber()

# DIR = 20
# STEP = 21
# CW = 1
# CCW = 0
# SPR = 200
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(STEP, GPIO.OUT)
# GPIO.output(DIR, CW)
# 
# step_count = SPR
# delay = 0.005
# 
# # for x in range(step_count):
# #     GPIO.output(STEP, GPIO.HIGH)
# #     sleep(delay)
# #     GPIO.output(STEP, GPIO.LOW)
# #     sleep(delay)
#     
# sleep(.5)
# GPIO.output(DIR,CCW)
# 
# for x in range(step_count):
#     GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)
#     
# # GPIO.cleanup()
# 
