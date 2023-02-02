from tkinter import * #import GUI tkinter needed

#Everything is a widget, 2 step of create and then define
root = Tk() #base window widget

myLabel = Label(root, text="Hello World!") #Creation of label widget

myLabel.pack() #shoving it onto the screen

root.mainloop()

