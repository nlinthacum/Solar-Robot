#!/usr/bin/env python3

import rospy
import getch
import RPi.GPIO as GPIO
import time
from time import sleep

from std_msgs.msg import Char
from std_msgs.msg import String
from std_msgs.msg import Float32

GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER1 = 19
GPIO_ECHO1 = 26

GPIO_TRIGGER2 = 20
GPIO_ECHO2 = 21
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance2():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 


def publisher():
    pub	= rospy.Publisher('ultrasonic_publish1', Float32, queue_size=1)
    pub2	= rospy.Publisher('ultrasonic_publish2', Float32, queue_size=1)

    rate	= rospy.Rate(50) #should be 1 hz

    msg_to_publish = Float32()
    
    

    while not rospy.is_shutdown():
        sens_distance1 = distance1()
        sens_distance2 = distance2()
    
        
       # char_to_publish = sens_distance1
       # char_to_publish = sens_distance2

      #  msg_to_publish.data = char_to_publish
        pub.publish(sens_distance1)
        pub2.publish(sens_distance2)

        rospy.loginfo(sens_distance1)
        rospy.loginfo(sens_distance2)
        
        sleep(.1)

        rate.sleep()


if __name__== "__main__":
    #rospy.init_node("ultrasonic_publish1") #idk if this is right
    rospy.init_node("ultrasonic_publish")
    publisher()





