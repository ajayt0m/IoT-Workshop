# IoT-Workshop
attempts on IoT
import serial //make the communication serial
import time //To deal with necessary delays 
ser=serial.Serial('COM3',9600) //storing to ser
time.sleep(1) //setting some wait time
if(ser.isOpen()==False): //if ser is low: make it high
    ser.open() 
data=ser.readline() //read from arduino
print data //display

ser.close() //mandatory
