#!/usr/bin/python
#TestMovie.py

import Animal
import sys,getopt

def usage():
	print("Usage: TestFace.py -h")
	print("Usage: TestFace.py -m <moviee>")
	print("Usage: TestFace.py --movie=<movie>")

def main(argv):
	legs = ''

	try:
		opts,args = getopt.getopt(argv,"hm:",["movie="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if(opt == "-h"):
			usage()
			sys.exit()
		elif opt in ("-m","--movie"):
			
			legs = argv[1]

	po = Animal.Animal(legs)
	print("Total Number of " + " " + po.toString())
	po.removeLegs(1)
	print("After Fight Number of " + " " + po.toString())
	po.isDisable()

if __name__ == "__main__":
   main(sys.argv[1:])

