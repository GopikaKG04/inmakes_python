from tkinter import *


class myfun:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()
        self.pbutton = Button(frame, text="click", command=self.msg)
        self.pbutton.pack()
        self.qbutton = Button(frame, text="exit", command=frame.quit)
        self.qbutton.pack(side=LEFT)

    def msg(self):
        print("clicked")


root = Tk()
object = myfun(root)
root.mainloop()
