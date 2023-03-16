from tkinter import *

root = Tk()


def fun():
    print("click me")


button1 = Button(root, text="ok", command=fun)
button1.pack()
root.mainloop()
