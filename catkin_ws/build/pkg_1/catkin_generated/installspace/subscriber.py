#!/usr/bin/env python2

import rospy
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo(msg.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Chatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
