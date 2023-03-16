from tkinter import *

root = Tk()


def newfunction():
    print("hai")


newmenu = Menu(root)
root.config(menu=newmenu)
submenu = Menu(newmenu)
newmenu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="new project")
submenu.add_command(label="new")
submenu.add_separator()
submenu.add_command(label="save as")
submenu1 = Menu(newmenu)
newmenu.add_cascade(label="edit", menu=submenu1)
submenu1.add_command(label="undo", command=newfunction)
submenu1.add_command(label="copy")
submenu1.add_separator()
submenu1.add_command(label="paste")

toolbar = Frame(root, bg="pink")
toolbar.pack(side=TOP, fill=X)
inbutton = Button(toolbar, text="save")
inbutton.pack(side=LEFT, anchor=W, padx=5, pady=25, )
inbutton = Button(toolbar, text="cancel")
inbutton.pack(side=LEFT, anchor=W, padx=5, pady=25, )
statusbar = Label(root, text="this is a statusbar", anchor=W, bd=2)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
