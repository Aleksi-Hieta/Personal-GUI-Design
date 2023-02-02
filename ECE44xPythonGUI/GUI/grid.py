from tkinter import * #import GUI tkinter needed

#Basic widget Label and row/column
root = Tk() #base window widget

myLabel1 = Label(root, text="Hello World!") #Creation of label widget
myLabel2 = Label(root, text="My name is griddy")
myLabel3 = Label(root, text="                 ")

myLabel1.grid(row=0, column=0) #if no column specified, will be centered
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)

myLabel4 = Label(root, text="Test").grid(row=2, column=0) #other form of prior steps

root.mainloop()

 