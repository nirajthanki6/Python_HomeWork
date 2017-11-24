class Mouth:
    ############################
    # Helping function
    ############################
    def __trace(self, s):
        print(s)

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,w,h):
        self.__width = w
        self.__height = h
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getWidth(self):
        return self.__width
    def setWidth(self, w):
        self.__width = w
    def getHeight(self):
        return self.__height
    def setHeight(self, h):
        self.__height = h
    def isBig(self):
        if(self.__width > 10 or self.__height > 5):
            print("Mouth is Big")
        return 0

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("Width= " + str(self.__width) + " " +
                "Height= " + str(self.__height))
    def close(self):
        self.__height = 0
        self.__width = 0
        return 0
    
