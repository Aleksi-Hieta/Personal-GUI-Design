from tkinter import *
from PIL import ImageTk,Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

#Python image and matplot libraries

root = Tk()
root.title('Testrun of Image Viewer')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/GUI/OSLogo.ico') #import images tough way

frame = LabelFrame(root, padx=20, pady=20) #padding inside the frame
frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #Padding outside the frame

e = Entry(root, width=20, borderwidth=5)
e.grid(row=1, column=0, columnspan=3)

fig = Figure(figsize=(5, 5), dpi=100)

y = [i**2 for i in range(101)]
plot1 = fig.add_subplot(111)
plot1.plot(y)

canvas = FigureCanvasTkAgg(fig,master = frame)  
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()