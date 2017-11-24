#!/usr/bin/python

# Exception.py
class Error(Exception):
   """The base class of erros"""
   # __code=0
    
   # constructor
   def __init__(self, n):
        self.__code = n
   def getCode(self):
        return self.__code

class ErrorYear(Error):
   """Raised when the input value of Year is Negative """
   # __num=0
   # constructor
   def __init__(self, n):
        Error.__init__(self, 1)
        self.__num = n
   def getNum(self):
        return self.__num

class ErrorMonth(Error):
   """Raised when the input value of Month is Less than 1"""
   # __num=0
   # constructor
   def __init__(self, n=0):
      Error.__init__(self, 3)
      self.__num = n
   def getNum(self):
      return self.__num

class ErrorDay(Error):
   """Raised when the input value of Day is Less than 1"""
   # __num=0
   # constructor
   def __init__(self, n=0):
      Error.__init__(self, 2)
      self.__num = n
   def getNum(self):
      return self.__num

class Date:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self, y,m,d):
      if(y <= 0):
        raise ErrorYear(y)
      elif(m < 1 or m > 12):
        raise ErrorMonth(m)
      elif(d < 1 or d > 31):
        raise ErrorDay(d)
      self._year = y
      self._month = m
      self._day = d
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getYear(self):
        return self._year
    def setYear(self, y):
        self._year = y
    def getMonth(self):
        return self._month
    def setMonth(self, m):
        self._month = m
    def getDay(self):
        return self._day
    def setDay(self, d):
        self._day = d
    def isCentennial(self):

      if((self._year % 100) == 0):
        print("A date is Centennial")
        return 0

    ############################
    # Implementor function
    ############################
    def reset(self):
        Date.setDay(1)
        Date.setMonth(1)
        Date.setYear(0)

# if __name__ == '__main__':
#   try:
#     t1 = Date(20111,2,32)
#     # t1.setDay(32)
#     t2 = Date(2010,62,3)
#   except ErrorYear as obj:
#     print("Error", obj.getCode(),": The Year", obj.getNum(), "is negative.")
#   except ErrorMonth as obj:
#     print("Error", obj.getCode(),": The Month", obj.getNum(), "is more than 12.")
#   except ErrorDay as obj:
#     print("Error", obj.getCode(),": The Day", obj.getNum(), "is more than 31.")
#   except:
#     print("Error: Unknwon exception.")
#   else:
#     print("No exception.")
#   finally:
#     print("End")
