from tkinter import *

root = Tk()
label1 = Label(root, text="hello python")
label1.pack()
frame1 = Frame(root)
frame1.pack()
but = Button(frame1, text="login", fg="blue", bg="yellow")
but.pack()
root.mainloop()
# eg2
from tkinter import *

root = Tk()
Label(root, text="hello python").pack()
but = Button(root, text="login")
but.pack()
root.mainloop()
