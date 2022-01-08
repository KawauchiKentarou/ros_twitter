#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import requests



key = "トークン"


def callback(msg):
    rospy.loginfo("Received a string")
    print(msg)

    message = msg.data
    tweetdata = "_t=%s&msg=%s" % (key,message)
    response = requests.post('http://stewgate-u.appspot.com/api/post/', data=tweetdata)
    print(response)

def listener():

    rospy.init_node('without_oauth', anonymous=True)

    rospy.Subscriber("tweeter", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
