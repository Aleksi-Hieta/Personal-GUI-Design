#Author: Aleksi Hieta
#Viewer.py: image viewer for multiple pics
#Date: 11/15/22

from tkinter import *

from PIL import Image, ImageTk

#Python image library

root = Tk()
root.title('Testrun of Window Menu')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico') #import images tough way
frame = LabelFrame(root, padx=150, pady=150) #padding inside the frame
frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def opengoose():
   global my_img
   top = Toplevel()
   top.title('Goose Window')
   top.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico')
   #lbl = Label(top, text="Test").pack()
   my_img = ImageTk.PhotoImage(Image.open("ImageLib/GoosePipe.jpg")) #Note: variables need to be global
   my_label = Label(top, image=my_img).pack()
   btn2 = Button(top, text="Destroy Goose", command=top.destroy).pack() 

btn = Button(frame, text="Release the Goose!", command=opengoose).pack()

def opendanger():
   global my_img2
   top2 = Toplevel()
   top2.title('Goose Window')
   top2.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico')
   #lbl = Label(top, text="Test").pack()
   my_img2 = ImageTk.PhotoImage(Image.open("ImageLib/DangerGoose.png")) #Note: variables need to be global
   my_label = Label(top2, image=my_img2).pack()
   btn2 = Button(top2, text="Destroy Goose", command=top2.destroy).pack() 

btn2 = Button(frame, text="Face your Doom!", command=opendanger).pack()


mainloop()