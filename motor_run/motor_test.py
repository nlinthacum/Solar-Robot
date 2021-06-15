#!/usr/bin/env python3
import rospy
from time import sleep
import RPi.GPIO as GPIO
from std_msgs.msg import String

def subscriber():
    sub = rospy.Subscriber('keyboard_publish', String, callback_function)
    
    rospy.spin()
    
def motor_spin(direction):
    DIR = 20
    STEP = 21
    CW = 1
    CCW = 0
    SPR = 200

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)

    step_count = SPR
    delay = 0.005

    if direction == "positive":
        GPIO.output(DIR, CW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        
    if direction == "negative":
        GPIO.output(DIR,CCW)
        
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        
    GPIO.cleanup()

def callback_function(message):
    rospy.loginfo(message.data)
    command = message.data
    if command == 'w':
        rospy.loginfo("forward")
        motor_spin("positive")
    elif command == 's':
        rospy.loginfo("backward")
        motor_spin("negative")

if __name__ == "__main__":
    rospy.init_node("keyboard_subscriber")
    subscriber()





