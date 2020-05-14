import serial
import csv
import time
from serial import Serial
from datetime import datetime

directory = 'C:/Users/hatoufi/Desktop'
port = 'COM5'
baudrate = 9600
timeout = 1
ts = 1

#Open serial port
ser = serial.Serial(port, baudrate, timeout, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS
)
ser.isOpen()

#Naming file by date
filename = datetime.now().strftime('{}/RS232_%Y-%m-%d-%H-%M.csv'.format(directory))

#Create a CSV file and record the data in it
with open(filename,'w',
          newline='') as f:
    csv_writer = csv.writer(f)

    #Read data in bytes type from serial port
    while True:
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        time.sleep(ts)

        #Remove first and last whitespace
        bytesValue = data.strip()
	
        #Convert bytes to string
        stringValue = bytesValue.decode('utf-8')
		
        #Save the string data in the CSV file
        writer = csv.writer(f,delimiter=',')
        writer.writerow([stringValue])
