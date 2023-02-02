from tkinter import *
from PIL import ImageTk,Image

#Python image library

root = Tk()
root.title('Testrun of Icons')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico') #import images tough way

my_img = ImageTk.PhotoImage(Image.open('GoosePipe.jpg'))
#images can be added to any widget
myLabel = Label(image=my_img)
myLabel.pack()


button_quit = Button(root, text="Exit Program", command=root.quit) #example of quit button
button_quit.pack()

root.mainloop()