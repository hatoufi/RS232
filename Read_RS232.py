import serial, csv, time
from datetime import datetime

directory = 'C:/Users/hatoufi/Desktop' #Directory for output

filename = None			#Output file name

port = 'COM5'			#Serial port COM#
baudrate = 9600			#Serial port baudrate 
timeout = 1				#Serial port timeout

area = 0.0042			#Membrane area in m^2

start = datetime.now()  #Save running code's start time

log_rate = 1			#Time in seconds between readings

#Open serial port
with serial.Serial(port, baudrate, timeout=timeout, parity=serial.PARITY_ODD,
                       stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS) as ser:

    #Naming file by date
    if filename is None:
        filename = datetime.now().strftime('{}/RS232_%Y-%m-%d-%H-%M.csv'.format(directory))

    #Create a CSV file and record the data in it
    with open(filename,'w', newline='') as f:
        writer = csv.writer(f)
    
        #Save the string data in the CSV file
        writer.writerow(['Date', 'Time', 'Mass (g)', 'Flux (Kg/m2/s)'])

        #Read data in bytes type from serial port
        while True:
            bytesToRead = ser.inWaiting()
            data = ser.read(bytesToRead)
            time.sleep(log_rate)

            #Remove first and last whitespace
            bytesValue = data.strip()
        
            #Convert bytes to list
            lists = bytesValue.decode('utf-8').split('\n')
        
            #Skip empty rows
            if len(lists) > 1:

                #Split the data into two lists ([date] and [time])
                d,t = lists[0].split()		          
                
                #Convert date string to date format
                d = datetime.strptime(d, '%m.%d.%Y').date()
                
                #Convert time string to time format
                t = datetime.strptime(t, '%H:%M').time()
                
                #Edit mass data
                mass = float(lists[1].split()[1])
                
                #Calculate elapsed time in seconds
                elapsed_time = datetime.now() - start
                etm = int(elapsed_time.total_seconds())
                
                #Calculate flux
                flux = float(mass/1000/area/etm)
                            
                #Write the modified data on the CSV file
                writer.writerow([d,t,mass,flux])
