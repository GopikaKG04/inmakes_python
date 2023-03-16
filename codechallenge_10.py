# obj class inheritances used super class vehicles sub class car and bike
class vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def getspecs(self):
        self.make = input("enter your make")
        self.model = input("enter your model")
        self.year = int(input("enter your  year"))

    def displayspecs(self):
        print(self.make, self.model, self.year)


class car(vehicles):
    def __init__(self, models, make, year, door, color):
        self.models = models
        self.make = make
        self.year = year
        self.color = color
        self.door = door

    def details(self):
        self.models = input("enter your models")
        self.make = input("enter your make")
        self.year = int(input("enter your year"))
        self.color = input("enter your color")
        self.door = int(input("enter no of door"))

    def shows(self):
        print(self.make, self.models, self.year, self.color, self.door)


class bike(car):
    def __init__(self, model, color, make, wheels):
        self.model = model
        self.color = color
        self.make = make
        self.wheels = wheels

    def bikedetails(self):
        self.model = input("enter your on model")
        self.color = input("enter your on color")
        self.make = input("enter the make")
        self.wheels = int(input("enter no of wheels"))

    def result(self):
        print(self.model, self.color, self.make, self.wheels)


obj = bike('', '', '', '')
obj.getspecs()
obj.displayspecs()
obj.details()
obj.shows()
obj.bikedetails()
obj.result()
