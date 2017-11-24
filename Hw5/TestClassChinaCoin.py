#!/usr/bin/python

# TestClassChinaCoin.py

import ClassicalChinaCoin 
import Square
import AncientObject
import Metal
import sys, getopt

def usage():
   print ('Usmaterial: TestClassChinaCoin.py -h')
   print ('Usmaterial: TestClassChinaCoin.py -r <radius> -s <side> -m <material>')
   print ('Usmaterial: TestClassChinaCoin.py --age=<age> --radius=<radius> --side=<side> --material=<material>')

def main(argv):
   age = ''
   radius = ''
   side = ''
   material = ''

   try:
      opts, args = getopt.getopt(argv,"ha:r:s:m:",["age=","radius=", "side=", "material="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-a", "--age"):
         age = arg
      elif opt in ("-r", "--radius"):
         radius = arg
      elif opt in ("-s", "--side"):
         side = arg
      elif opt in ("-m", "--material"):
         material = arg
      

   square = Square.Square(int(side))
   metal = Metal.Metal(material)
   mycoin = ClassicalChinaCoin.ClassicalChinaCoin(age,metal,float(radius),square)
   print(mycoin.toString() + "\n")
   mycoin.setAge(700)
   mycoin.getSquare().setSide(2)
   mycoin.setRadius(float(5.0))
   metal1 = Metal.Metal("Gold")
   mycoin.setMetal(metal1)
   print(mycoin.toString() + "\n")
   mycoin.destroy()
   print(mycoin.toString())

if __name__ == '__main__':
   main(sys.argv[1:])

