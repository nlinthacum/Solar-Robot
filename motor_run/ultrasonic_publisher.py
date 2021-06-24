#!/usr/bin/env python3

import rospy
import getch
import RPi.GPIO as GPIO
import time

from std_msgs.msg import Char
from std_msgs.msg import String
from std_msgs.msg import Float32

GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 19
GPIO_ECHO = 26
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 


def publisher():
    pub	= rospy.Publisher('ultrasonic_publish1', Float32, queue_size=1)

    rate	= rospy.Rate(50) #should be 1 hz

    msg_to_publish = Float32()
    
    

    while not rospy.is_shutdown():
        distance = distance()
    
        
        char_to_publish = "Publishing %c"%distance

      #  msg_to_publish.data = char_to_publish
        pub.publish(distance)

        rospy.loginfo(distance)

        rate.sleep()


if __name__== "__main__":
    rospy.init_node("ultrasonic_publish1")
    publisher()





