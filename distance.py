import csv

# This function will open the distance table csv file and pull that information into
# the distList variable. This will create a matrix that will be used to find the
# distances in the getDistance function.

# Run time complexity O(n)
with open("WGUPS Distance Table.csv") as distanceTable:
    reader = csv.reader(distanceTable)
    distList = []
    for row in reader:
        distList.append(row)

# This will open my location table so that an address can be entered and a
# integer will be returned.

# Run time complexity O(n)
with open("WGUPS Location Table.csv") as locationName:
    reader = csv.reader(locationName)
    locationList = []
    for row in reader:
        locationList.append(row)

# This function will find the distance of a row, col pair in distList

# Run time complexity of O(1)
def getDistance(row,col):
    distance = distList[row][col]
    if distance == '':
        distance = distList[col][row]
    return float(distance)

# This function is passed an address and then will pass back an integer. The
# integer will correspond to the row/column of the address in the distList
# matrix.

# Run time complexity of O(n)
def GetLocationPos(address):
    address = address
    number = 0
    for location in locationList:
        if location[1] == address:
            number = int(location[0])
    return number

# This function is passed a distance which is a float, truckleavetime which is an
# integer which is the minutes after midnight that the truck is currently at
# and the final variable that the function is passed is the truck object that
# the truckleavetime is associated with. The distance is divided by the truck
# speed which will return a float of the amount of hours that have passed.
# To find the minutes, you multiply the minutes by 60 and convert it to an int
# The totalMinutes variable is then added to the truckleavetime to ensure
# that the truck is updated with the right time. The function will return
# a string in the format of HH:MM

# Run time complexity O(1)
def getTime(distance,truckleavetime,truck):
    hours = distance / truck.speed
    totalMinutes = int(hours * 60)
    truckleavemin = truckleavetime + totalMinutes
    newHours = int(truckleavemin / 60)
    minutes = int(truckleavemin - (newHours * 60))
    if minutes < 10:
        newMinutes = '0' + str(minutes)
        minutes = newMinutes
    strTime = str(newHours) + ':' + str(minutes)
    truck.timeStart += totalMinutes

    return strTime

