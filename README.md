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

###Algorithms and Data Structure

  A linked list method is what I will begin with in this demonstration. This method would be used for smaller data sets so that the source code can be generated faster. With quick implementation to get the project file up and running when the data structure is not as large. The linked list source code displays good housekeeping variables to keep the list from writing over itself and losing data. Start with the head node and continue to push a new bid into the place of the list. Ability to search for a bid that is wanted to be known. The linked list gives a fast and simple method to get the data up and running for temporary use of the data. 
  
  With vector sorting there is a display of two methods to compare to in the source file. This demonstrates the timing involved with the algorithm used between quicksort and selection sort methods. The vector source code can allow visual troubleshooting to obtain the best possible outcome for the data set on hand. Monitors the output to reflect which is a faster result. With the two methods you can find that selection sort can be better if the data structure is redefined in another manner to simplify the sorting process. The quicksort will find the results much faster than that of selection sort when dealing on a larger scale of data. This source code is a great way to troubleshoot between the two methods to prove the capability to obtain data in a faster manner for the user. 
	
  A great method of organizing large data sets is reflected in the hash tables source code. In the source code you can find that the hash table is also utilizing the chaining method to store data. The code reflects on how the good housekeeping can find the proper data node when searching a bucket with multiple data nodes due to the hashing function. The hash function creates a structure to simplify the data on hand. Another good advantage of hashing is that a node with a large data set within itself can be simplified into a designation of a hash which can reduce the memory usage when accessing the node. The hash function can be utilized to have the data set be organized in a system that can be easily accessible.
	
  With the binary search tree, you can optimize the search ability on a list of data. The tree structure has a root node, internal nodes, and leaf nodes. Root node being the top node in tier zero. From the root node you have your smaller nodes to the left and the larger nodes to the right branching down until the leaf node is made. This source code shows the structure on how to access the search tree and find the node that is wanted without conflict. Always maintaining good housekeeping with having the node set to nullptr for each search. If no node is found being able to add the node in the proper location in the tree. Breaking down a which path to take the search lessens the process that the computer needs to go through. Instead of having a list to go through the binary search method cuts that down. A list of seven nodes in a normal array will have to go search all nodes until the correct one is found. The same list in a binary tree the search will find the node in three search points. Nodes 1-7 and wanting to find seven all points are not needed to search for the seven. You would hit 4, 6 then 7.
	
  The source codes available in the portfolio are all good examples on how to troubleshoot a data set that is given. There are some standards that need to be implemented when using this code. The standard “-std=c++11” will give functionality to the source codes attached. The hash table usage in the source code can be vital to a large database and can be implemented as shown in the source code. Use of a hashing algorithm can have an impact on performance with a data set. Incorporate code for collisions that may occur can make sure the proper data can be read. The chaining method or the linear probing which uses unused spaces. 
	
  The source codes available are reusable with minor changes to the source. They are based of extracting information from an excel database and can change the parameters that are needed for the desired result. Some of the codes provided can correlate to other codes already established. The structure of these codes can show the placement in the original code structure. There are multiple comments added to the code to help in that aspect. They are modular in that concept to be able to use them elsewhere. 
	
  In computer science it is vital to know algorithms and how to define data structures. Most work environments want to lean towards going digital in that means to create better flow and environmentally helpful. No need to continually print page after page if you have a database that is accessible and the means to access it whenever from a computer. I can use the source code on hand to generate data that I would normally take around a half hour to compose. Instead, I can organize the data by shipment dates and even incorporate timelines that are needed to meet. This attacks a processing problem to cut back on work hours to focus on other issues at hand. The only obstacle I have is the schedule changes constantly and I cannot change the information at that exact moment. 


Linked List Data Structure. (n.d.). Retrieved February 22, 2020, from https://www.geeksforgeeks.org/data-structures/linked-list/

Fundamentals of data structures: Hashing. (n.d.). Retrieved February 22, 2020, from https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_1/Fundamentals_of_data_structures/Hash_tables_and_hashing

Parlante, N. (n.d.). Retrieved February 22, 2020, from http://cslibrary.stanford.edu/110/BinaryTrees.html





