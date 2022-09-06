#!/usr/bin/env python
"""
Assignments from ROS for Beginners:
Author: Anis Koubaa
Modifications: Pranav.S (spranav1911@gmail.com)
Date of modification: 05-06-2022

"""
import numpy as np
import cv2

def filter_color(rgb_image, lower_bound_color, upper_bound_color):
    #convert the image into the HSV color space
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv image",hsv_image)

    #find the upper and lower bounds of the yellow color (tennis ball)
    yellowLower =(30, 150, 100)
    yellowUpper = (50, 255, 255)

    #define a mask using the lower and upper bounds of the yellow color 
    mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)

    return mask

def getContours(binary_image):      
    #_, contours, hierarchy = cv2.findContours(binary_image, 
    #                                          cv2.RETR_TREE, 
    #                                           cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_ball_contour(binary_image, rgb_image, contours):
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],'uint8')
    
    for c in contours:
        area = cv2.contourArea(c)
        perimeter= cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if (area>100):
            cv2.drawContours(rgb_image, [c], -1, (150,250,150), 1)
            cv2.drawContours(black_image, [c], -1, (150,250,150), 1)
            cx, cy = get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),5,(150,150,255),-1)
            print ("Area: {}, Perimeter: {}".format(area, perimeter))
    print ("number of contours: {}".format(len(contours)))
    #cv2.imshow("RGB Image Contours",rgb_image)
    cv2.imshow("Black Image Contours",black_image)
    return black_image

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx= int(M['m10']/M['m00'])
        cy= int(M['m01']/M['m00'])
    return cx, cy

def main(image):
    #read_video.capture()
    #image_name = "images/copy/tennis_ball_detection"+str(i)+".jpg"
    yellowLower =(30, 150, 100)
    yellowUpper = (50, 255, 255)
    #rgb_image = read_rgb_image(image_name, False)
    binary_image_mask = filter_color(image, yellowLower, yellowUpper)
    contours = getContours(binary_image_mask)
    b_image = draw_ball_contour(binary_image_mask, image,contours)
    #cv2.imwrite("images/black/tennis_ball_detection"+str(i)+".jpg",b_image)
    cv2.waitKey()
    cv2.destroyAllWindows()



