#!/usr/bin/python
#TestFace.py
import Head
import Mouth
import Eye
import Nose
import sys,getopt

def usage():
	print("Usage: TestHead.py -h")
	print("Usage: TestHead.py -f <face>")
	print("Usage: TestHead.py --head=<head>")

def main(argv):
	noofhair = ''
	radiusofhead = ''
	left_eye_radius = ''
	right_eye_radius = ''

	try:
		opts,args = getopt.getopt(argv,"hf:",["head="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if(opt == "-h"):
			usage()
			sys.exit()
		elif opt in ("-f","--head"):
			noofhair = argv[1]
			radiusofhead = argv[2]
			left_eye_radius = argv[3]
			right_eye_radius = argv[4]

	
	left_eye = Eye.Eye(left_eye_radius)
	right_eye = Eye.Eye(right_eye_radius)
	left_eye_abnormal = Eye.Eye(0)
	right_eye_abnormal = Eye.Eye(0)
	mouth_height_width = Mouth.Mouth(0,0)
	

	normalhead = Head.Head(noofhair,radiusofhead,left_eye,right_eye,mouth_height_width)
	print("Normal Head:" + "\n")
	print(normalhead.toString() + "\n")
	abnormalhead = Head.Head(noofhair,radiusofhead,left_eye_abnormal,right_eye_abnormal,mouth_height_width)
	print("Abnormal Head:" + "\n")
	print(abnormalhead.toString())
		
	normalhead = Head.Head(noofhair,radiusofhead,left_eye_abnormal,right_eye_abnormal,mouth_height_width)
	# Mouth.Mouth.setHeight(1)
	print("\n")
	print("After Closing Eyes and Mouth for Normal Head" + "\n")
	print(normalhead.toString() + "\n")
	normalhead.headAche()

	
if __name__ == "__main__":
   main(sys.argv[1:])