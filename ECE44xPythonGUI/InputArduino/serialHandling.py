#Author:    Aleksi Hieta
#Reference: https://www.youtube.com/watch?v=AHr94RtMj1A&ab_channel=Von
#Date:      12/29/2022
#Purpose:   Identify and read from serial port. Error handling for choosing invalid port

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

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

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n')) # .rstrip('\n') to remove extra endline