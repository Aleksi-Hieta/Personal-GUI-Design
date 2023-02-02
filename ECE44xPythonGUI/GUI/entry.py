from tkinter import * #import GUI tkinter needed

#Input box
root = Tk() #base window widget

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ") #Default text
#e.get()

def myClick():
    hello = "Hello " + e.get() + "!"
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Name: ", command=myClick) #note no () on the command
myButton.pack()


root.mainloop()

 