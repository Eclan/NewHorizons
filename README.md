### Self review over old code on my PC.

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="">
    <source src="https://Eclan.github.io/NewHorizons/Code Review.mp4" type="video/mp4">
  </video>
</figure>

A self review of older code is conducted by myself above. The original code submission is version 1.0 and the submission to the code review is updated version 1.1. When beginning to code with Python I was very unaware of how in-depth code went. Throughout multiple python courses I am noticing that my old code is not up to par and need to update them. Here is one example of self reviewing your own material and creating better more reformed code and exercise good practice.

```markdown
`Version 1.0`

import socket, sys
remoteServer    = input('Enter a remote host to scan: ')
remoteServerIP  = socket.gethostbyname(remoteServer)
print('*' * 60)
print('Please wait, scanning remote host', remoteServerIP)
print('*' * 60)
try: 
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex((remoteServerIP, port)) 
        if result == 0: 
            print('Port {}: 	 Open' .format(port)) 
        sock.close() 
except socket.gaierror: 
    print('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error: 
    print('Couldn''t connect to server')
    sys.exit()
input('press Enter to exit')

```

```markdown
`Version 1.1`

# to access ports from remote host that you choose
import socket 
# uses the sys.exit for errors when reading ports
import sys 
# to keep track of time to accomplish port scan
from datetime import datetime 

# Ask for input of ip you are wanting to scan
remoteServer = input('Enter a remote host to scan (press Ctrl-C to stop): ')
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print('*' * 60)
print('Please wait, scanning remote host', remoteServerIP)
print('*' * 60)

# Check what time the scan started
t1 = datetime.now()

# using the try will run all ports in range first then except applies
try: 
    for port in range(441,447):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0: 
            print('Port {}: 	 Open' .format(port)) 
            sock.close() 

# user function to exit program
except KeyboardInterrupt: 
    print('You pressed Ctrl+C exiting program')
    sys.exit()

# having errors with ip chosen
except socket.gaierror: 
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# having errors with sockets
except socket.error: 
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

```
[version1.1](https.Eclan.github.io/NewHorizons/PortScanV1.0.py)

