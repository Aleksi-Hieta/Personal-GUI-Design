from tkinter import *
from PIL import ImageTk,Image
#Python image library

root = Tk()
root.title('Framing')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xJupyterGUI/BeaverLogo.ico')

frame = LabelFrame(root, padx=50, pady=50) #padding inside the frame
#Title on the border -> text="This is the frame"
frame.pack(padx=10, pady=10) #Padding outside the frame
#Note- can usually only do pack and pack or grid and grid, but there can be a grid inside a packed frame
b = Button(frame, text="Example")
b2 = Button(frame, text="Example2")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

status = Label(frame, text="Image 1 of 4", bd=1, relief=SUNKEN, anchor=E) #E is East/rightside

root.mainloop()