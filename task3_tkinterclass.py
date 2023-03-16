# 1.task using class in tkinter
from tkinter import *


class school:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        self.la1 = Label(frame1, text="hello everyone")
        self.la1.pack()
        self.but1 = Button(frame1, text="click me", command=self.teacher)
        self.but1.pack()
        self.la2 = Label(frame1, text="how are you ?")
        self.la2.pack()
        self.but2 = Button(frame1, text="cancel", command=self.student)
        self.but2.pack()
        self.la3 = Label(frame1, text="i hope you all are fine!")
        self.la3.pack()
        self.but3 = Button(frame1, text="exit", command=frame1.quit)
        self.but3.pack()

    def teacher(self):
        print("clicked")

    def student(self):
        print("canceled")


root = Tk()
object = school(root)
root.mainloop()
