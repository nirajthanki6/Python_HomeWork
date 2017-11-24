import sys, getopt
from AncientObject import AncientObject 
class ClassicalChinaCoin(AncientObject):
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,a,metal,r,square):
        self._radius = r
        AncientObject.__init__(self,a,metal)
        self._square = square
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getRadius(self):
        return self._radius
    def setRadius(self, r):
        self._radius = r
    def setSquare(self,square):
        self._square = square
    def getSquare(self):
        return self._square
    

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("Radius=" +str(self._radius) + "\n" +
            self._square.toString() + "\n" +
            AncientObject.toString(self) )
