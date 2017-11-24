#!/usr/bin/python
# Face.py

import sys, getopt

class Face:
    ############################
    # Helping function
    ############################
    def __pi(self,s):
        return (s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,name,left_eye,right_eye,nose,mouth):
        self.__name = name
        self.__left_eye = left_eye
        self.__right_eye = right_eye
        self.__nose = nose
        self.__mouth = mouth
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getLeftEye(self):
        return self.__left_eye
    def setLeftEye(self, left_eye):
        self.__left_eye = left_eye
    def getRightEye(self):
        return self.__right_eye
    def setRightEye(self, right_eye):
        self.__left_eye = right_eye
    def getNose(self):
        return self.__nose
    def setNose(self, nose):
        self.__nose = nose
    def getMouth(self):
        return self.__mouth
    def setMouth(self, mouth):
        self.__mouth = mouth    
    def isBigMouth(self):
        return self.__mouth > 30
    def isEyesUnbalanced(self):
        if(self.__left_eye != self.__right_eye):
        	return 0
    def isOneEye(self):
    	if(self.__right_eye == 0 or self.__left_eye == 0):
    		return 0


    ############################
    # Implementor function
    ############################
    def toString(self):
    	return ("Name=" + str(self.__name) + "\n" +
    			"left_eye=" +str(self.__left_eye) + "\n" +
    			"right_eye=" +str(self.__right_eye) + "\n" +
    			"nose=" +str(self.__nose) + "\n" +
    			"mouth=" +str(self.__mouth))
    def blind(self):
        self.__left_eye = 0 
        self.__right_eye = 0
    def removeMouth(self):
        remove(self.__mouth)
        return  0