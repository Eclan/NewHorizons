# **** Eric Clancy's use for port scanning****
import socket, sys
remoteServer    = input('Enter a remote host to scan (press Ctrl-C to stop): ')
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

