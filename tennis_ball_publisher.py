#!/usr/bin/env python

import cv2
import string
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import rospy
#video_capture = cv2.VideoCapture(0)
bridge = CvBridge()

def image_conversion(image):
    try:
    	ros_image = bridge.cv2_to_imgmsg(image, "bgr8")
	return ros_image
    except CvBridgeError as e:
        print(e)

def publisher():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/tennis_ball_image', Image, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('tennis_ball_publisher', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(20) # 1hz
    #keep publishing until a Ctrl-C is pressed
    video_capture = cv2.VideoCapture('video/tennis-ball-video.mp4')
    i = 0
    while not rospy.is_shutdown():
        ret, frame = video_capture.read()
	
	#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	
	#cv2.line(frame,(0,0),(511,511),(255,0,0),5)
	cv2.imwrite("images/copy/pranav_tennis_ball_detection"+str(i)+".jpg",frame)
	image_name = "images/copy/pranav_tennis_ball_detection"+str(i)+".jpg" 	
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break
	imageros = image_conversion(frame)
	hello_str = "Sending Image %s" % i
	rospy.loginfo(hello_str)
        pub.publish(imageros)
	i = i + 1
        rate.sleep()
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
