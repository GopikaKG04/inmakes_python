# task 4 uder tkinter
# task  tkinter using dropdown ,then grouping,msg etc..
from tkinter import *

root = Tk()


def project():
    print("this new project")


def copy():
    print("copy the msg")


def tool():
    print("open window tools")


def newfile():
    print("open the file")


def folder():
    print("this new folder")


def msg():
    print("get new msgs")


mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
mymenu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="new project", command=project)
submenu.add_command(label="new")
submenu.add_separator()
submenu.add_command(label="new file")
submenu.add_command(label="open")
submenu.add_command(label="save as")
submenu.add_command(label="exit", command=mymenu.quit)

submenu1 = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=submenu1)
submenu1.add_command(label="undo")
submenu1.add_command(label="cut")
submenu1.add_separator()
submenu1.add_command(label="paste")
submenu1.add_command(label="delete")
submenu1.add_command(label="select all")
submenu1.add_command(label="copy", command=copy)

submenu2 = Menu(mymenu)
mymenu.add_cascade(label="view", menu=submenu2)
submenu2.add_command(label="toolwindow", command=tool)
submenu2.add_command(label="context info")
submenu2.add_separator()
submenu2.add_command(label="quick_definition")
submenu2.add_command(label="parameter info")
submenu2.add_command(label="type_info")
submenu2.add_command(label="recent files")

submenu3 = Menu(mymenu)
mymenu.add_cascade(label="navigate", menu=submenu3)
submenu3.add_command(label="back")
submenu3.add_command(label="class")
submenu3.add_separator()
submenu3.add_command(label="file", command=newfile)
submenu3.add_command(label="symbol")
submenu3.add_command(label="line_column")
submenu3.add_command(label="next highlighted error")

submenu4 = Menu(mymenu)
mymenu.add_cascade(label="code", menu=submenu4)
submenu4.add_command(label="codecompletion")
submenu4.add_command(label="analyazecode")
submenu4.add_separator()
submenu4.add_command(label="folding", command=folder)
submenu4.add_command(label="reformatecode")
submenu4.add_command(label="reformatefile")
submenu4.add_command(label="movelineup")

submenu5 = Menu(mymenu)
mymenu.add_cascade(label="windows", menu=submenu5)
submenu5.add_command(label="storecurrentlayoutdt")
submenu5.add_command(label="activetool")
submenu5.add_separator()
submenu5.add_command(label="editortool")
submenu5.add_command(label="notification", command=msg)
submenu5.add_command(label="tabs")
submenu5.add_command(label="backgroundtask")

root.mainloop()
