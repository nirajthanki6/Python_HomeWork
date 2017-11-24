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
    def __init__(self, r):
        self._eyeRadius = r
    def __del__(self):
        pass

    ############################
    # Access function
    ############################
    def getEyeRadius(self):
        return self._eyeRadius
    def setEyeRadius(self, r):
        self._eyeRadius = r
    def isSmall(self):
        return self._eyeRadius < 10

    ############################
    # Implementor function
    ############################
    def toString(self):
        return("EyeRadius= " + str(self._eyeRadius))
    def close(self):
        setEyeRadius(0)
        return 0
    
