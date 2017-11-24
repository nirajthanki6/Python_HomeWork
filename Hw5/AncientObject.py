import Metal
import sys, getopt
class AncientObject:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,a,metal):
        self._age = a
        self._metal = metal
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getAge(self):
        return self._age
    def setAge(self, a):
        self._age = a
    def getMetal(self):
        return self._metal
    def setMetal(self, metal):
        self._metal = metal
    def isOld(self):
        return self._age > 1000

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("Age= " + str(self._age) + "\n" +
            self._metal.toString())
    def destroy(self):
        AncientObject.setAge(self,-1)
        return  0
