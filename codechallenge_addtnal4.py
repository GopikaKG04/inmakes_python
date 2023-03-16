# inheritances -  additional questions 1.multiple inheritances
class hospital:
    def __init__(self, adminname, drname, sistername, department):
        self.adminname = adminname
        self.drname = drname
        self.sistername = sistername
        self.department = department

    def details(self):
        self.adminname = input("enter your adminname")
        self.drname = input("enter your drname")
        self.sistername = input("enter your sistername")
        self.department = input("enter your department")


class department(hospital):
    def show(self):
        print(self.adminname, self.drname, self.sistername, self.department)


class patientward(department):
    def __init__(self, name, age, number, disease):
        self.name = name
        self.age = age
        self.number = number
        self.disease = disease

    def getdetails(self):
        self.name = input("enter your name")
        self.age = int(input("enter your age"))
        self.number = int(input("enter your number"))
        self.disease = input("enter your disease")

    def putdetails(self):
        print(self.name, self.age, self.number, self.disease)


obj = patientward('', '', '', '')
obj.details()
obj.show()
obj.getdetails()
obj.putdetails()
