#Author:    Aleksi Hieta
#Reference: https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
#Date:      2/22/2023
#Purpose:   GUI with Tabs and Arduino reading

#import tkinter as tk                    
#from tkinter import ttk

from tkinter import *
from tkinter.ttk import Notebook

import serial.tools.list_ports
import functools



ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()


root = Tk()
root.title("Test GUI")
tabControl = Notebook(root)
  
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)

tabControl.add(tab1, text ='Initialize')  
tabControl.add(tab2, text ='Control')
tabControl.add(tab3, text ='Video')
tabControl.pack(expand = 1, fill ="both")
  
#Label(tab1, text ="Control Settings").grid(column = 0, row = 0, padx = 30, pady = 30)
Label(tab3, text ="Video Settings").grid(column = 0, row = 0, padx = 30, pady = 30)

Button(tab3, text="Exit Program", command=root.destroy).grid(column = 0, row = 1)

#Initialize Tab1 Elements
stage_frame = LabelFrame(tab1, padx=10, pady=10, text="Stage Initialization")
stage_frame.grid(row=0, column=0, padx=10, pady=10) 
camera_frame = LabelFrame(tab1, padx=10, pady=10, text="Camera Initialization")
camera_frame.grid(row=1, column=0, padx=10, pady=10) 
control_frame = LabelFrame(tab1, padx=10, pady=10, text="Controls Initialization")
control_frame.grid(row=2, column=0, padx=10, pady=10) 

def initComPort1():
    #print(choice.get())
    currentPort = choice1.get()
    comPortVar = str(currentPort.split(' ')[0])

    #currentPort = str(ports[index])
    #comPortVar = str(currentPort.split(' ')[0])
    #print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

def initComPort2():
    #print(choice.get())
    currentPort = choice2.get()
    comPortVar = str(currentPort.split(' ')[0])

    #currentPort = str(ports[index])
    #comPortVar = str(currentPort.split(' ')[0])
    #print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

def initComPort3():
    #print(choice.get())
    currentPort = choice3.get()
    comPortVar = str(currentPort.split(' ')[0])

    #currentPort = str(ports[index])
    #comPortVar = str(currentPort.split(' ')[0])
    #print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

comArray = ["","","","","",""]

for onePort in ports:
    #comButton = Button(tab1, text=onePort, height=1, width=45, command = functools.partial(initComPort, index = ports.index(onePort)))
    #print(ports.index(onePort))
    comArray[ports.index(onePort)+1] = onePort
    #comButton.grid(row=ports.index(onePort)+1, column=0)

#Setting Up drop-down menus for Initialization
choice1 = StringVar()
choice1.set("-")
choice2 = StringVar()
choice2.set("-")
choice3 = StringVar()
choice3.set("-")
drop1 = OptionMenu(stage_frame, choice1, *comArray)
drop1.grid(row = 0, column = 1)
drop1.config(width=50)
drop2 = OptionMenu(camera_frame, choice2, *comArray)
drop2.grid(row = 0, column = 1)
drop2.config(width=50)
drop3 = OptionMenu(control_frame, choice3, *comArray)
drop3.grid(row = 0, column = 1)
drop3.config(width=50)
#print(choice.get())

InitializeButton1 = Button(stage_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort1))
InitializeButton1.grid(row = 1, column = 1)
InitializeButton2 = Button(camera_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort2))
InitializeButton2.grid(row = 1, column = 1)
InitializeButton3 = Button(control_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort3))
InitializeButton3.grid(row = 1, column = 1)



def varUpdate():
    arduinoString = my_label.cget("text")
    
    xyz_val = arduinoString
    xyz_val = xyz_val[8:]
    print(xyz_val)

    #Limit Checks
    if(arduinoString[0] == '1'):
        x_limit.config(text="X Minimum Reached!")
    elif(arduinoString[1] == '1'):
        x_limit.config(text="X Maxmimum Reached!")
    else:
        x_limit.config(text="Gucci X")

    if(arduinoString[2] == '1'):
        y_limit.config(text="Y Minimum Reached!")
    elif(arduinoString[3] == '1'):
        y_limit.config(text="Y Maxmimum Reached!")
    else:
        y_limit.config(text="Gucci Y")

    if(arduinoString[4] == '1'):
        z_limit.config(text="Z Minimum Reached!")
    elif(arduinoString[5] == '1'):
        z_limit.config(text="Z Maxmimum Reached!")
    else:
        z_limit.config(text="Gucci Z")

    if(arduinoString[6] == '1'):
        x_var = xyz_val
        x_name.config(text="X: "+x_var)
    elif(arduinoString[6] == '2'):
        y_var = xyz_val
        y_name.config(text="Y: "+y_var)
    elif(arduinoString[6] == '3'):
        z_var = xyz_val
        z_name.config(text="Z: "+z_var)
    elif(arduinoString[6] == 'B'):
        if(arduinoString[7] == '1'):
            x_button.config(text="pressed!")
            #x button pressed
        elif(arduinoString[7] == '2'):
            y_button.config(text="pressed!")
            #y button pressed
        elif(arduinoString[7] == '3'):
            z_button.config(text="pressed!")
            #z button pressed

def xyz_limit_reset():
    x_limit.config(text="X in valid range")
    y_limit.config(text="Y in valid range")
    z_limit.config(text="Z in valid range")

def xyz_button_reset():
    x_button.config(text="X button")
    y_button.config(text="Y button")
    z_button.config(text="Z button")

my_text = ""
x_var = "0"
y_var = "0"
z_var = "0"

my_label = Label(tab2)
x_name = Label(tab2, text = "X: "+x_var)
y_name = Label(tab2, text = "Y: "+y_var)
z_name = Label(tab2, text = "Z: "+z_var)

limit_label = Label(tab2, text = "Limit messages")
x_limit = Label(tab2, text = "X in valid range")
y_limit = Label(tab2, text = "Y in valid range")
z_limit = Label(tab2, text = "Z in valid range")

limit_reset = Button(tab2, text = "Reset Min & Max", command = xyz_limit_reset)
limit_reset.grid(column = 1, row = 4)

button_reset = Button(tab2, text = "Reset Button Presses", command = xyz_button_reset)
button_reset.grid(column = 2, row = 4)

x_button = Label(tab2, text = "X button")
y_button = Label(tab2, text = "Y button")
z_button = Label(tab2, text = "Z button")

my_label.grid(column = 0, row = 0, padx = 30, pady = 0)
x_name.grid(column = 0, row = 1, padx = 30, pady = 0)
y_name.grid(column = 0, row = 2, padx = 30, pady = 0)
z_name.grid(column = 0, row = 3, padx = 30, pady = 0)

limit_label.grid(column = 1, row = 0, padx = 30, pady = 0)
x_limit.grid(column = 1, row = 1, padx = 30, pady = 0)
y_limit.grid(column = 1, row = 2, padx = 30, pady = 0)
z_limit.grid(column = 1, row = 3, padx = 30, pady = 0)

x_button.grid(column = 2, row = 1, padx = 30, pady = 0)
y_button.grid(column = 2, row = 2, padx = 30, pady = 0)
z_button.grid(column = 2, row = 3, padx = 30, pady = 0)


my_label.config(text=my_text)

def checkSerialPort():
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        my_text = recentPacket.decode('utf').rstrip('\n')
        my_label.config(text=my_text)
        varUpdate()
    root.update()
    root.after(1, checkSerialPort) #Recursive call to allow for root.mainloop()

root.after(1, checkSerialPort)
root.mainloop() 
#while True:
    #root.update()
    #checkSerialPort()