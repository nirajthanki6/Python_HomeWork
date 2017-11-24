#!/usr/bin/python

# TestMetal.py
import Metal
import sys, getopt

def usage():
   print ('Usage: TestMetal.py -h')
   print ('Usage: TestMetal.py -m <material>')
   print ('Usage: TestMetal.py --material=<material>')

def main(argv):
   material = ''

   try:
      opts, args = getopt.getopt(argv,"hm:",["material="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-m", "--material"):
         material = arg

   coin = Metal.Metal(material)
   print (coin.toString())
   coin.setMaterial("gold")
   print (coin.toString())
   coin.changeMaterial("plastic")
   print (coin.toString())


####################################
# $ TestMetal.py -h
# Usage: TestMetal.py -h
# Usage: TestMetal.py -r <material>
# Usage: TestMetal.py --material=<material>
#
# $ TestMetal.py -m cupper
# material= 2
# Coin is large
# material= 103
# The area is 33329.2344
# The circumference is 647.1696
#
# $ TestMetal.py --material=2
# material= 2
# Coin is large
# material= 103
# The area is 33329.2344
# The circumference is 647.1696
####################################
if __name__ == '__main__':
   main(sys.argv[1:])
