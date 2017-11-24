#!/usr/bin/python
#TestFace.py
import Face
import sys,getopt

def usage():
	print("Usage: TestFace.py -h")
	print("Usage: TestFace.py -f <face>")
	print("Usage: TestFace.py --face=<face>")

def main(argv):
	name = ''
	left_eye = ''
	right_eye = ''
	nose = ''
	mouth = ''

	try:
		opts,args = getopt.getopt(argv,"hf:",["face="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if(opt == "-h"):
			usage()
			sys.exit()
		elif opt in ("-f","--face"):
			name = argv[1]
			left_eye = argv[2]
			right_eye = argv[3]
			nose = argv[4]
			mouth = argv[5]

	face = Face.Face(name,left_eye,right_eye,nose,mouth)
	print(face.toString())
	if(name == "Mike"):
		mike = Face.Face(name,left_eye,right_eye,nose,mouth)
		if(mike.isOneEye() == 1):
			print("Mike have One Eye")	
	elif(name == "Boo"):
		if(face.isEyesUnbalanced() == 0):
			print(name + " "+ "Eyes are Unequal")
		else:
			print("Eyes are Equal")
	elif(name == "Mike"):
		if(face.isOneEye() == 0):
			print(name + " " + "have only One Eye")
		else:
			print(name + " " + "have both Eyes")
	elif(name == "Hello Kitty"):
		face.setMouth(3)
		print(face.toString())
	

if __name__ == "__main__":
   main(sys.argv[1:])