# messagebox or alert box using tkinter
# 1.showinfo()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.showinfo('title', "this is a information")
root.mainloop()
# 2.showwarning()function
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.showwarning('title', "last warning")
root.mainloop()
# 3.showerror()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.showerror('error', "error in form")
root.mainloop()
# 4.sakquestion()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.askquestion('questionforyou', "are you sure?")
root.mainloop()
# 5. askokcancel()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.askokcancel('title', "are you?")
root.mainloop()
# 6.askyesno()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.askyesno('title', "are you sure?")
root.mainloop()
# 7.askretrycancel()
from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.askretrycancel('title', "are wannted?")
root.mainloop()
