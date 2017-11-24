import Eye
import Mouth
class Head():
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,nh,hr,le,re,h):
        self.__noofhair = nh
        self.__radiusofhead = hr
        self._left_eye = le
        self._right_eye = re
        self._height = h
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getNoofhair(self):
        return self.__noofhair
    def setNoofhair(self, nh):
        self.__noofhair = nh
    def getHeadRadius(self):
        return self.__radiusofhead
    def setHeadRadius(self, hr):
        self.__radiusofhead = hr
    def getLeftEye(self):
        return self._left_eye
    def setLeftEye(self, le):
        self._left_eye = le
    def getRightEye(self):
        return self._right_eye
    def setRightEye(self, re):
        self._right_eye = re
    def isNormal(self):
        if(self.__left_eye == self.__right_eye):
            print("Head is Normal")
            return 0

    ############################
    # Implementor function
    ############################
    def toString(self):
        left_eye = Eye.Eye(self)
        right_eye = Eye.Eye(self)
        return("No of Hair= " + str(self.__noofhair) + "\n " +
                "Radius of Head= " + str(self.__radiusofhead) + "\n " +
                "left Eye= " +str(self._left_eye.getEyeRadius()) + "\n "
                "Right Eye= " +str(self._right_eye.getEyeRadius()))
    def headAche(self):
        if(Mouth.Mouth.close(self) == 0 or (self._left_eye == 0 and self._right_eye == 0)):
            print("HeadAche because mouth and Eyes are closed!")
        else:
            print("Head is Normal")
            return 0
    