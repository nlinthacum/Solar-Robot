#!/usr/bin/env python3
#this is the main script
import rospy
from time import sleep
import RPi.GPIO as GPIO
from std_msgs.msg import String

in1 = 24
in2 = 23
enA = 25
temp1=1

enB = 27
in3 = 17
in4 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(enA, 2200)
q=GPIO.PWM(enB, 2200)
p.start(25)
q.start(25)



def subscriber():
    
     sub = rospy.Subscriber('keyboard_publish', String, callback_function, queue_size=1)
  #  sub = rospy.Subscriber('keyboard_publish', String, callback_function)
     rospy.spin()

def callback_function(message):
    command = message.data
    
    if command == 'w':
        forward_motor()
        rospy.loginfo("forward")

def forward_motor():
    print("I'm going forward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(.5)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    
    


if __name__ == "__main__":
    rospy.init_node("keyboard_subscriber")
    subscriber()


    
    




