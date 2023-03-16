class father:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def getdetails(self):
        self.name = input("entr your name")
        self.character = input("entr your charcter")

    def putdetails(self):
        print(self.name, self.character)


class mother:
    def display(self):
        print("am mother class")


class child(father, mother):
    def child(self):
        print("am derived class")


obj = child('', '')
obj.getdetails()
obj.putdetails()
obj.display()
obj.child()
