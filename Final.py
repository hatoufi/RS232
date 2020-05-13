import time
import csv
from datetime import datetime


#Open the CSV file created by RS232
with open('C:/Users/hdallal/Desktop/RS232_2020-05-10-16-03.csv') as rf:

#Create a new CSV file
    with open('C:/Users/hdallal/Desktop/RS232edited.csv', 'w', newline='') as wf:
        writer = csv.writer(wf)
		
#Create a header for the new file and start the data modification
        writer.writerow(['Date', 'Time', 'Mass (g)'])
        for data in csv.reader(rf):
            if any(data):
                for line in data:
				
#Split the data into two lists ([date and time] and [mass])
                    lists = line.split('\n')
					
#Edit date and time data
                    for x in lists[0]:
					
#Split the data into two lists ([date] and [time])
                        d = lists[0].split()

#Convert date string to date format
                        date = datetime.strptime(d[0], '%m.%d.%Y').date()
						
#Convert time string to time format
                        time = datetime.strptime(d[1], '%H:%M').time()
						
#Edit mass data
                        m = lists[1].split()
                        mass = float(m[1])

#Write the modified data on the CSV file
                    writer.writerow([date,time,mass])
