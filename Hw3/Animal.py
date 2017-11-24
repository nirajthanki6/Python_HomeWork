#!/usr/bin/python
# Animal.py

class Animal:
    ############################
    # Helping function
    ############################
    def __pi(self,s):
        return (s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,legs):
        self.__legs = legs
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getName(self):
        return self.__legs
    def setName(self, legs):
        self.__legs = legs
    def isDisable(self):

    	if(self.__legs == 0):
    		print("Po is Disable")
	############################
    # Implementor function
    ############################
    def toString(self):
    	return ("Legs=" + str(self.__legs))
    def removeLegs(self,num):
        self.__legs = (int(self.__legs) - num)
        if(int(self.__legs) < 0):
        	print("The Value of Legs Can't be less than 0")
        return 0

