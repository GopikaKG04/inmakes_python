from tkinter import *

root = Tk()
l1 = Label(root, text="hai", fg="red", bg="blue")
l1.pack(fill=X)
l2 = Label(root, text="hello", fg="yellow", bg="black")
l2.pack(side=LEFT, fill=Y)
root.mainloop()
