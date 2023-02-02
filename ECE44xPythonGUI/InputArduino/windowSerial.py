#Author:    Aleksi Hieta
#Reference: https://www.youtube.com/watch?v=AHr94RtMj1A&ab_channel=Von
#Date:      12/29/2022
#Purpose:   Identify and read from serial port. Error handling for choosing invalid port
#           Open output in window similar to what will be incorporated in final GUI

from tkinter import *
from PIL import Image, ImageTk

import serial.tools.list_ports

#Root def for Windows
root = Tk()
root.title('Testrun of Window Menu')
root.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/InputArduino/OSLogo.ico') #import images tough way
frame = LabelFrame(root, padx=150, pady=150) #padding inside the frame
frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Port def
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

xval = 0
yval = 0
zval = 0
#Button Definition to open a new window
def openknobs():
   top = Toplevel()
   top.title('Input Controls')
   top.iconbitmap('C:/Users/ahiet/OneDrive/Desktop/ECE44xPythonGUI/InputArduino/OSLogo.ico')

   x_label = Label(top, text="x: "+ str(xval)).pack()
   y_label = Label(top, text="y: "+ str(yval)).pack()
   z_label = Label(top, text="z: "+ str(zval)).pack()
   btn2 = Button(top, text="Close Window", command=top.destroy).pack() 

btn = Button(frame, text="Input Controls", command=openknobs).pack()

def portRead():
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n')) # .rstrip('\n') to remove extra endline
        #Parse the line to determine which values to adjust
        #First Knob: X, Second Knob: Y, Third Knob: Z

#Port Declaration
portlist = []

for onePort in ports:
        portlist.append(str(onePort))
        print(str(onePort))

val = input("Select Port: COM")

found = 0
for x in range(0, len(portlist)):
    if portlist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portlist[x])
        found = 1

if found == 1:
    print("Port Found")
else:
    print("Port Not Found")
    quit()

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

mainloop()
portRead()
#while True:
#    if serialInst.in_waiting:
#        packet = serialInst.readline()
#        print(packet.decode('utf').rstrip('\n')) # .rstrip('\n') to remove extra endline
        #Parse the line to determine which values to adjust
        #First Knob: X, Second Knob: Y, Third Knob: Z