import sys
import rospy
from ros_assignment.srv import RectangleAreaService
from ros_assignment.srv import RectangleAreaServiceRequest
from ros_assignment.srv import RectangleAreaServiceResponse

def calc_area_client(w,h):
	rospy.wait_for_service("calc_area")
	try:
		calc_area = rospy.ServiceProxy('calc_area', RectangleAreaService)
		resp = calc_area(w,h)
		return resp.area
	except rospy.ServiceException(e):
		print("Some problem with the service")
def usage():
	return

if __name__ == '__main__'
	if len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print ("%s [x y]" %sys.argv[0])
		sys.exit(1)
	print ("Requesting %s * %s",%(x,y))
	s = calc_area_client(x,y)
	print("Area : ",s)
