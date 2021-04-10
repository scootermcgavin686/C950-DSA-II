import csv

from hashtable import myHash
from package import Package
from distance import getDistance, GetLocationPos, getTime
from truckClass import Truck

# The loadPackageData function will open up a file that is passed to it, and
# then parse through that data and create a package object. The package object
# is then loaded into the hash table through the insert function.

# Run time complexity of O(n)
def loadPackageData(fileName):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile)
        for package in packageData:
            packageID = int(package[0])
            paddress = package[1]
            pcity = package[2]
            pstate = package[3]
            pzip = package[4]
            pdeadline = package[5]
            pweight = package[6]
            pmessage = package[7]

            packageItem = Package(packageID,paddress,pcity,pstate,pzip,pdeadline,pweight,pmessage)

            myHash.insert(packageID,packageItem)


# DeliverPackage function takes in a truck object that contains a list of
# package objects that are populated through the hash table lookup function. It
# will then iterate through the truck objects package list to deliver the packages.
# This function finds the closest distance from the current location to the other
# package addresses in the list. After all packages are delivered it will then find
# the distance from the last location back to the hub.

# O(n^2)
def DeliverPackage(truck):
    route = []
    totalMiles = 0
    currentLocation = GetLocationPos('4001 South 700 East')
    start = GetLocationPos('4001 South 700 East')

    # Continues loop until all packages are off truck objects package list
    while truck.packages:
        min_dist = 1000
        # Will find closest distance from the current location and the closest address
        for p1 in truck.packages:
            nextLocation = GetLocationPos(p1.address)
            dist = getDistance(currentLocation, nextLocation)
            # If the package's address is already the current one and the current location ID isn't 0 which is the hub
            # it will deliver the package
            if dist == 0 and currentLocation != 0:
                min_dist = dist
                closest = p1
            # If no packages are equal to the current location it will assign the closest package to closest
            elif min_dist > dist:
                min_dist = dist
                closest = p1
        currentLocation = GetLocationPos(closest.address)
        totalMiles += min_dist
        deliverTime = getTime(min_dist, truck.timeStart, truck)
        closest.deliveryTime = deliverTime
        closest.on_truck = str(truck.truckID)
        route.append(closest)
        truck.packages.remove(closest)
    end = GetLocationPos(closest.address)
    totalMiles += getDistance(end,start)
    truck.totalMiles += totalMiles


# The LoadTruck function initializes three truck class objects. After initializing the
# truck objects it will access the hash table through the search function and load those
# package objects onto trucks through a state machine. Certain parameters will have the
# packages going onto specific trucks. Once the trucks have been loaded then the
# DeliverPackage function will be called for each truck. The totalMiles variable is
# initialized with zero and will keep track of the miles of each trucks total miles.

# Run time complexity of O(n)
def LoadTruck():
    truck1 = Truck(1,480)
    truck2 = Truck(2,545)
    truck3 = Truck(3,660)
    totalMiles = 0
    packageList = []
    deliverTogether = [15,19,14,20,13,16]
    for i in range(40):
        package = myHash.search(i+1)
        deadline = package.deadline
        message = package.message
        ID = package.packageID
        if message == "Delayed on flight---will not arrive to depot until 9:05 am" and package not in packageList:
            truck2.packages.append(package)
            packageList.append(package)
        if (deadline == "10:30 AM" and message != "Can only be on truck 2") and package not in packageList:
            truck1.packages.append(package)
            packageList.append(package)
        if ID in deliverTogether and package not in packageList:
            truck1.packages.append(package)
            packageList.append(package)
        if message == "Can only be on truck 2" and package not in packageList:
            truck2.packages.append(package)
            packageList.append(package)
        if message == "Wrong address listed" and package not in packageList:
            truck3.packages.append(package)
            packageList.append(package)
        if len(truck2.packages) < 10 and package not in packageList:
            truck2.packages.append(package)
            packageList.append(package)
        if package not in packageList:
            truck3.packages.append(package)
            packageList.append(package)
    DeliverPackage(truck1)
    DeliverPackage(truck2)
    DeliverPackage(truck3)
    totalMiles += truck1.totalMiles
    totalMiles += truck2.totalMiles
    totalMiles += truck3.totalMiles
    return totalMiles





