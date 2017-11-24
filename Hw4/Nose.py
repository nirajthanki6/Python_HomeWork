class Nose:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,x,y,z):
        self.__x_side = x
        self.__y_side = y
        self.__z_side = z
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getXSide(self):
        return self.__x_side
    def setXSide(self, x):
        self.__x_side = x
    def getYSide(self):
        return self.__y_side
    def setYSide(self, y):
        self.__y_side = y
    def getZSide(self):
        return self.__z_side
    def setZSide(self, z):
        self.__z_side = z
    def isBig(self):
        if(self.__xside > 10 and self.__yside > 10 and self.__zside > 10):
            print("is Big")
        return 0
    def isImpossible(self):
        possible1 = self.__x_side + self.__y_side > self.__z_side
        possible2 = self.__z_side + self.__x_side > self.__y_side
        possible3 = self.__y_side + self.__z_side > self.__x_side
        
        if(possible1 == true or possible2 == true or possible3 == true):
            print("The Triangle is Possible")
        else:
            print("The Triangle is not Possible")

        
    ############################
    # Implementor function
    ############################
    def toString(self):
        return("XSide= " + str(self.__x_side) + " " +
            "YSide= " + str(self.__y_side) + " " +
            "ZSide= " + str(self.__y_side))
    def break1(self):
        setXSide(0)
        setYSide(0)
        setZSide(0)
        return 0
    