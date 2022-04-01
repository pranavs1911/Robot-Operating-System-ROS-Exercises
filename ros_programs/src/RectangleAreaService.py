from ros_assignment.srv import RectangleAreaService
from ros_assignment.srv import RectangleAreaServiceRequest
from ros_assignment.srv import RectangleAreaServiceResponse

import rospy

def calc_area(req):
	print("Returning area for width :",req.width, "and height", req.height)
	return RectangleAreaServiceResponse(req.width * req.height)

def rectangle_area_service():
	rospy.init_node('calc_area_server')
	sa = rospy.Service('calc_area', RectangleAreaService, calc_area)
	print ("Ready to calc area")
	rospy.spin()

if __name__ == "__main__":
	rectangle_area_service()
