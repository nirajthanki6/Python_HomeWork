class Eye:
    ############################
    # Helping function
    ############################
    def __pi(self):
        return 3.1416

    ############################
    # Manager function
    ############################
    # Including a default contrutctor
    def __init__(self,r):
        self.__eye_radius = r
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getEyeRadius(self):
        return self.__side
    def setEyeRadius(self, r):
        self.__eye_radius = r
    def isSmall(self):
        return self.__eye_radius < 10

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("EyeRadius= " + str(self.__eye_radius))
    def close(self):
        setEyeRadius(1)
        return 0
    
