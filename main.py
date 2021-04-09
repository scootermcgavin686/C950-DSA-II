from csvreader import LoadTruck, loadPackageData
from hashtable import myHash

loadPackageData("WGUPS Package File.csv")
miles = LoadTruck()

userInput = ''

print('\n\nWGU Delivery Project')
print('Scott Moore Student ID# 0001070276', '\n')


# This loop is the command line interface for my program. A while loop will continue running until
# the user enters the word quit. It will ask the user if they want to see what packages were delivered
# at a certain time by entering the word timestamp. Once a time is entered it will loop through the
# hash table via the search function and the packages num. If the delivery time of the package is before
# the given time it will state that it has been delivered and give the time it was delivered, otherwise
# it will say that it has not been delivered.

# Run time complexity of O(n)
while userInput != 'QUIT':
    # This input will ask the user what they would like to see, delivered or not, All package data at a certain time
    # or a single package's data by ID number
    userInput = input('\nTo only see if a package was delivered or not at a specific time, '
                      'enter Timestamp \nTo see all the package data at a specific time'
                      ' enter AllPACKAGEDATA \nTo see a specific package at a certain time'
                      ' type PACKAGEDATA\nOr enter Quit to end the program: ').upper()

    # Condition to see if a package has been delivered or not by a certain time
    if userInput == 'TIMESTAMP' or userInput == 'TIME STAMP':
        userTimeStamp = input('Please enter a time in the format HH:MM military time: ')
        userTimeStampString = userTimeStamp.split(':')
        userHour = int(userTimeStampString[0])
        userMin = int(userTimeStampString[1])
        while userHour >= 24 or userMin >= 60:
            userTimeStamp = input('Please enter a time in the correct format HH:MM military time: ')
            userTimeStampString = userTimeStamp.split(':')
            userHour = int(userTimeStampString[0])
            userMin = int(userTimeStampString[1])

        # Prints out how many miles it took to deliver the packages
        print('\nPackages were delivered in', miles, 'miles.\n')

        # Loops through the hash table and calls the search function, will compare user timestamp with package
        # timestamp and decided the status of the package
        for i in range(40):
            package = myHash.search(i + 1)
            packageTime = package.deliveryTime
            packageTimeSplit = packageTime.split(':')
            userTime = userTimeStamp.split(':')
            packageHour = int(packageTimeSplit[0])
            packageMin = int(packageTimeSplit[1])
            userHour = int(userTime[0])
            userMin = int(userTime[1])
            if userMin >= 60:
                newUserMin = (userMin % 60)
                newUserHour = int(userMin / 60)
                userHour += newUserHour
                userMin = newUserMin
            if userHour > packageHour:
                package.deliveryStatus = 'Delivered'
            elif userHour == packageHour and userMin >= packageMin:
                package.deliveryStatus = 'Delivered'
            else:
                package.deliveryStatus = 'Not Delivered'

        # Will print out a statement of the amount of miles it took to deliver package.
        print('User entered a time of: {}:{}\n'.format(userHour, userMin))

        # This loop calls the hash table search function to determine the status of the package at the given
        # user timestamp. If the user timestamp is before the package timestamp, then it hasn't been delivered
        # and if it is after than it has been delivered.
        for i in range(40):
            package = myHash.search(i + 1)
            if package.deliveryStatus == 'Delivered':
                print('Package', package.packageID, 'was delivered at', package.deliveryTime)
            elif package.deliveryStatus == 'Not Delivered':
                print('Package', package.packageID, 'is not delivered')

    # Condition to print out all package data at a certain time.
    if userInput == 'ALLPACKAGEDATA' or userInput == 'ALL PACKAGE DATA':
        userTimeStamp = input('Please enter a time in the format HH:MM military time: ')
        userTimeStampString = userTimeStamp.split(':')
        userHour = int(userTimeStampString[0])
        userMin = int(userTimeStampString[1])

        # This will check the user's input. If not formatted correctly, it will ask the user to re-input time.
        # The while loop will check to see that the time is correctly formatted and if it is, will break out.
        while userHour >= 24 or userMin >= 60:
            userTimeStamp = input('Please enter a time in the correct format HH:MM military time: ')
            userTimeStampString = userTimeStamp.split(':')
            userHour = int(userTimeStampString[0])
            userMin = int(userTimeStampString[1])
        print('\nPackages were delivered in', miles, 'miles.\n')

        # Loops through the hash table and calls the search function, will compare user timestamp with package
        # timestamp and decided the status of the package
        for i in range(40):
            package = myHash.search(i + 1)
            packageTime = package.deliveryTime
            packageTimeSplit = packageTime.split(':')
            userTime = userTimeStamp.split(':')
            packageHour = int(packageTimeSplit[0])
            packageMin = int(packageTimeSplit[1])
            userHour = int(userTime[0])
            userMin = int(userTime[1])
            if userMin >= 60:
                newUserMin = (userMin % 60)
                newUserHour = int(userMin / 60)
                userHour += newUserHour
                userMin = newUserMin
            if userHour > packageHour:
                package.deliveryStatus = 'Delivered'
            elif userHour == packageHour and userMin >= packageMin:
                package.deliveryStatus = 'Delivered'
            elif ((userHour * 60) + userMin) >= 480 and package.on_truck == '1':
                package.deliveryStatus = 'En route'
            elif ((userHour * 60) + userMin) >= 545 and package.on_truck == '2':
                package.deliveryStatus = 'En route'
            elif ((userHour * 60) + userMin) >= 660 and package.on_truck == '3':
                package.deliveryStatus = 'En route'
            else:
                package.deliveryStatus = 'At Hub'

        # Will print out the amount of miles it took to deliver packages
        print('\nUser entered a time of: {}:{}\n\n'.format(userHour, userMin))

        # Loops through hash table to print out a statement depending on package status
        for i in range(40):
            package = myHash.search(i + 1)
            if package.deliveryStatus == 'Delivered':
                print('Package:', package, 'was on truck', package.on_truck)
            elif package.deliveryStatus == 'En route':
                print('Package:', package, ', on truck', package.on_truck)
            elif package.deliveryStatus == 'At Hub':
                print('Package:', package, ', loaded on truck', package.on_truck)

    # Condition to see a single package object
    if userInput == 'PACKAGEDATA' or userInput == 'PACKAGE DATA':
        userNum = int(input('Please enter a specific package ID: '))
        userTimeStamp = input('Please enter a time in the format HH:MM military time: ')
        userTimeStampString = userTimeStamp.split(':')
        userHour = int(userTimeStampString[0])
        userMin = int(userTimeStampString[1])

        # Will loop until the user has given a correctly formatted time.
        while userHour >= 24 or userMin >= 60:
            userTimeStamp = input('Please enter a time in the correct format HH:MM military time: ')
            userTimeStampString = userTimeStamp.split(':')
            userHour = int(userTimeStampString[0])
            userMin = int(userTimeStampString[1])

        # Loops through the hash table and calls the search function, will compare user timestamp with package
        # timestamp and decided the status of the package
        for i in range(40):
            package = myHash.search(i + 1)
            packageTime = package.deliveryTime
            packageTimeSplit = packageTime.split(':')
            userTime = userTimeStamp.split(':')
            packageHour = int(packageTimeSplit[0])
            packageMin = int(packageTimeSplit[1])
            userHour = int(userTime[0])
            userMin = int(userTime[1])
            if userHour > packageHour:
                package.deliveryStatus = 'Delivered'
            elif userHour == packageHour and userMin >= packageMin:
                package.deliveryStatus = 'Delivered'
            elif ((userHour * 60) + userMin) >= 480 and package.on_truck == '1':
                package.deliveryStatus = 'En route'
            elif ((userHour * 60) + userMin) >= 545 and package.on_truck == '2':
                package.deliveryStatus = 'En route'
            elif ((userHour * 60) + userMin) >= 660 and package.on_truck == '3':
                package.deliveryStatus = 'En route'
            else:
                package.deliveryStatus = 'At Hub'

        # Will print out the user's timestamp
        print('\nUser entered a time of: {}:{}\n'.format(userHour, userMin))
        # Assigns package to the users specified ID
        package = myHash.search(userNum)

        # Depending on the users time package will either be At hub, En route, or Delivered.
        if package.deliveryStatus == 'Delivered':
            print('\nPackage:', package, 'on truck', package.on_truck, '\n')
        elif package.deliveryStatus == 'En route':
            print('\nPackage:', package, ', on truck', package.on_truck, '\n')
        elif package.deliveryStatus == 'At Hub':
            print('\nPackage:', package, ', Loaded on truck', package.on_truck, '\n')












