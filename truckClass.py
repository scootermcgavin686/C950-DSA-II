# The truck class is initialized with a truck ID and a start time with the start
# time being in minutes from midnight. The packages list will eventually be
# filled with package objects. There is also a total miles variable that will
# hold the amount of miles that the truck travels.

class Truck:
    def __init__(self, truckID, timeStart):
        self.truckID = truckID
        self.packages = []
        self.speed = 18
        self.timeStart = timeStart
        self.totalMiles = 0
