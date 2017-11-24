#!/usr/bin/python

# TestException.py
from ExceptionClass import Date
from ExceptionClass import ErrorYear
from ExceptionClass import ErrorMonth
from ExceptionClass import ErrorDay
from ExceptionClass import Error
import sys, getopt

def usage():
   print ('Usmaterial: TestException.py -h')
   print ('Usmaterial: TestException.py -y <year> -m <month> -d <day>')
   print ('Usmaterial: TestException.py --year=<year> --month=<month> --day=<day>')

def main(argv):
   year = ''
   month = ''
   day = ''

   try:
      opts, args = getopt.getopt(argv,"hy:m:d:",["year=", "month=", "day="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-y", "--year"):
         year = arg
      elif opt in ("-m", "--month"):
         month = arg
      elif opt in ("-d", "--day"):
         day = arg
   
   try:
    t1 = Date(int(year),int(month),int(day))
   except ErrorYear as obj:
      print("Error", obj.getCode(),": The Year", obj.getNum(), "or negative.")
   except ErrorMonth as obj:
      print("Error", obj.getCode(),": The Month", obj.getNum(), "is more than 12.")
   except ErrorDay as obj:
      print("Error", obj.getCode(),": The Day", obj.getNum(), "is more than 31.")
   except:
      print("Error: Unknwon exception.")
   else:
      print("No exception.")
   finally:
      print("End")

if __name__ == '__main__':
   main(sys.argv[1:])

