from tkinter import *  # task1

master = Tk()
label = Label(master, text="hello gopika", fg="blue", bg="yellow")
label.pack()
but = Button(master, text="ok", fg="red", bg="black")
but.pack()
master.mainloop()

from tkinter import *  # exmp2 using frame print name label and ok button

master = Tk()
label = Label(master, text="hello gopika", fg="blue", bg="yellow").pack()
frame2 = Frame(master)
frame2.pack()
but = Button(frame2, text="ok", fg="red", bg="black")
but.pack()
master.mainloop()
