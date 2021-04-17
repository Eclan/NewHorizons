# **** Clancy's internal use only for port scanning Revised 2/13/2021 ****

import socket # to access ports from remote host that you choose
import sys # uses the sys.exit for errors when reading ports
from datetime import datetime # to keep track of time to accomplish port scan

# Ask for input of ip you are wanting to scan
remoteServer = input('Enter a remote host to scan (press Ctrl-C to stop): ')
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print('*' * 60)
print('Please wait, scanning remote host', remoteServerIP)
print('*' * 60)

# Check what time the scan started
t1 = datetime.now()

try: # using the try will run all ports in range first then except applies
    for port in range(441,447):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0: 
            print('Port {}: 	 Open' .format(port)) 
            sock.close() 

except KeyboardInterrupt: # user function to exit program
    print('You pressed Ctrl+C exiting program')
    sys.exit()

except socket.gaierror: # having errors with ip chosen
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error: # having errors with sockets
    print('Couldn''t connect to server')
    sys.exit()

# Checking the time again on stop scan
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print('Scanning Completed in: (H:M:S)', total)
input('press Enter to exit')

del port
del t1
del t2
