from tkinter import * #import GUI tkinter needed

#Buttons
root = Tk() #base window widget

def myClick():
    myLabel = Label(root, text="Look! Button Clicked")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, bg="blue", fg="white") #note no () on the command
myButton.pack()


#Other Button features
# state=DISABLED
#padx and pady make button larger
#fg and bg can be to change color, color codes like "#ffffff" also work

root.mainloop()

 