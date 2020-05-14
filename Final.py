import serial
import csv
import time as t
from serial import Serial
from datetime import datetime

directory = 'C:/Users/hatoufi/Desktop'


#Open serial port
ser = serial.Serial(port='COM5', baudrate=9600, timeout=1, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS
)
ser.isOpen()

#Naming file by date
filename = datetime.now().strftime('{}/RS232_%Y-%m-%d-%H-%M.csv'.format(directory))

#Create a CSV file and record the data in it
with open(filename,'w',
          newline='') as f:
    writer = csv.writer(f)
    
    #Save the string data in the CSV file
    writer.writerow(['Date', 'Time', 'Mass (g)'])

    #Read data in bytes type from serial port
    while True:
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        t.sleep(ts)

        #Remove first and last whitespace
        bytesValue = data.strip()
        
        #Convert bytes to list
        lists = bytesValue.decode('utf-8').split('\n')
        
        #skip empty rows
        if len(lists) > 1:
            
			#Split the data into two lists ([date] and [time])
            X = lists[0].split()
            
			#Convert date string to date format
            date = datetime.strptime(X[0], '%m.%d.%Y').date()
						
			# #Convert time string to time format
            time = datetime.strptime(X[1], '%H:%M').time()
						
			#Edit mass data
            m = lists[1].split()
            mass = float(m[1])
                        
			#Write the modified data on the CSV file
            writer.writerow([date,time,mass])
