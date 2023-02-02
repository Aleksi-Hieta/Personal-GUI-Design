#Author: Aleksi Hieta
#Viewer.py: image viewer for multiple pics
#Date: 10/15/22

from tkinter import *
from PIL import ImageTk,Image

#Python image library

root = Tk()
root.title('Testrun of Image Viewer')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico') #import images tough way

frame = LabelFrame(root, padx=150, pady=150) #padding inside the frame
frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #Padding outside the frame

my_img1 = ImageTk.PhotoImage(Image.open("ImageLib/GoosePipe.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("ImageLib/DangerGoose.png"))
my_img3 = ImageTk.PhotoImage(Image.open("ImageLib/GooseBell.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("ImageLib/GooseCouple.jpg"))
#images can be added to any widget

image_list = [my_img1, my_img2, my_img3, my_img4]
#image_list[index]

status = Label(frame, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #E is East/rightside

myLabel = Label(image=image_list[0])
myLabel.grid(row=0, column=0, columnspan=3)

def forward(img_index):
    global myLabel
    global button_forward
    global button_back
    
    myLabel.grid_forget()

    myLabel = Label(image=image_list[img_index-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_index+1))
    button_back = Button(root, text="<<", command=lambda: back(img_index-1))

    if img_index == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image "+str(img_index)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #West to East
    

def back(img_index):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=image_list[img_index-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_index+1))
    button_back = Button(root, text="<<", command=lambda: back(img_index-1))

    if img_index == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image "+str(img_index)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #West to East
    


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit) #example of quit button
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E) #West to East

root.mainloop()