# 1 draw a line
from tkinter import *

root = Tk()
canvas = Canvas(root, width=100, height=200)
canvas.pack()
line = canvas.create_line(0, 0, 8, 90)
root.mainloop()

# 2. 2lines
from tkinter import *

root = Tk()
canvas = Canvas(root, width=100, height=200)
canvas.pack()

line = canvas.create_line(10, 10, 10, 90, fill="green")
newline = canvas.create_line(0, 0, 8, 90)
root.mainloop()
# 3.rectangle
from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=500)
canvas.pack()

new = canvas.create_rectangle(100, 100, 200, 200, fill="green")

root.mainloop()
# 4
from tkinter import *

root = Tk()
canvas = Canvas(root, width=100, height=200)
canvas.pack()
newline1 = canvas.create_line(15, 25, 30, 35, 40, 45, 50, 55, dash=(4, 3))
newline2 = canvas.create_line(300, 35, 300, 200, 35, 200, 35, 300, dash=(4, 4))

newline = canvas.create_line(55, 85, 155, 85, 105, 180, 25, 85, dash=(4, 3))
root.mainloop()
# 5 arc
from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

new = canvas.create_arc(100, 100, 200, 200, fill="green")

root.mainloop()
# 6.oval
from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

new = canvas.create_oval(100, 100, 200, 200, fill="green")

root.mainloop()
# 7line
from tkinter import *

root = Tk()
canvas = Canvas(root, width=100, height=200)
newline = canvas.create_line(0, 0, 89, 90)
root.mainloop()
