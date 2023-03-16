class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdetails(self):
        self.name = input("enter your name")
        self.mark = int(input("enter your mark"))

    def putdetails(self):
        print(self.name, self.mark)


obj = student("", "")
obj.getdetails()
obj.putdetails()


class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def getdetails(self):
        self.name = "gopika"
        self.subject = "maths"
        print("gopika", "maths")


obj = teacher("gopika", "maths")
obj.getdetails()


class teacher:
    def __init__(self, name, subj):
        self.name = name
        self.subj = subj

    def getdetails(self):
        self.name = input("enter your name")
        self.subj = input("enter your subj")

    def putdetails(self):
        print(self.name, self.subj)


object = teacher("", "")
object.getdetails()
object.putdetails()
