class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdetails(self):
        self.name = input("enter your name")
        self.mark = int(input("enter your mark"))

    def putdetails(self):
        print(self.name, self.mark)


class teacher(student):
    def display(self):
        print("am derived class1")


class parent(teacher):
    def new(self):
        print("am derived class2")


class admin(parent):
    def adminfun(self):
        print("am derived class3")


obj = admin('', '')
obj.getdetails()
obj.putdetails()
obj.display()
obj.new()
obj.adminfun()
