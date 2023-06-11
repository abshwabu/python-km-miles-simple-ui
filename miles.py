from tkinter import *

windows = Tk()

button = Button(windows,text="change")
button.grid(row=0,column=0)
e1_value=StringVar()
e1 = Entry(windows,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(windows,height=1,width=20)
t1.grid(row=0,column=2)

windows.mainloop()