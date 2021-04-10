# This is the package class, package data will be passed into this class
# from a csv file and will initialize package objects. the str function of
# of the package class will allow the package object to be passed back as a string

class Package:
    def __init__(self, packageID, address, city, state, zip, deadline, weight, message, status=''):
        self.packageID = packageID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.message = message
        self.deliveryStatus = status
        self.deliveryTime = ''
        self.on_truck = ''

    # Allows Package objects to be returned as string
    def __str__(self):
        return ('{}, {}, {}, {} {}, {}, {}, {},'
                ' Delivery time {}, Status of package: {}'.format(self.packageID, self.address, self.city,
                                 self.state, self.zip, self.weight, self.message, self.deadline,
                                 self.deliveryTime, self.deliveryStatus))
