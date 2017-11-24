#!/usr/bin/python

# TestSpecialChinaCoin.py
import SpecialChinaCoin, Square
import Metal as Metal
import sys, getopt

def usage():
   print ('Usmaterial: TestSpecialChinaCoin.py -h')
   print ('Usmaterial: TestSpecialChinaCoin.py -r <radius> -s <side> -m <material>')
   print ('Usmaterial: TestSpecialChinaCoin.py --radius=<radius> --side=<side> --material=<material>')

def main(argv):
   radius = ''
   side = ''
   material = ''

   try:
      opts, args = getopt.getopt(argv,"hr:s:m:",["radius=", "side=", "material="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-r", "--radius"):
         radius = arg
      elif opt in ("-s", "--side"):
         side = arg
      elif opt in ("-m", "--material"):
         material = arg

   square = Square.Square(int(side))
   coin = SpecialChinaCoin.SpecialChinaCoin(material, float(radius), square)
   print (coin.toString())
   print("-----------")

   coin.changeMaterial("gold");
   print (coin.toString())
   print("-----------")

   coin.enlarge(3)
   print (coin.toString())
   print("-----------")


####################################
# $ TestSpecialChinaCoin.py -h
# Usmaterial: TestSpecialChinaCoin.py -h
# Usmaterial: TestSpecialChinaCoin.py -r <radius> -s <side> -a <material>
# Usmaterial: TestSpecialChinaCoin.py --radius=<radius> --side=<side> --material=<material>
#
# $ TestSpecialChinaCoin.py -r 2 -s 5 -m cupper
# Material= cupper
# Side= 5
# Radius= 2.0
# -----------
# Material= gold
# Side= 5
# Radius= 2.0
# -----------
# Material= gold
# Side= 5
# Radius= 5.0
# -----------
####################################
if __name__ == '__main__':
   main(sys.argv[1:])

