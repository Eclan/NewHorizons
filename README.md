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

***************************************** Software Engineering and Design *****************************************

With the implementation of software engineering design, the initial step was to create the idea without coding. This is defining the structure you want to obtain for the final product. The concept is set with the first draft of the student information system as seen in the diagram below.  

![image](https://user-images.githubusercontent.com/75941814/115123923-6cd47480-9f8d-11eb-9a97-ef5024c9b832.png)

This draft lays out the main functions that are needed to cover for the application to be complete. There is not much detail just an overall layout that gets the team or yourself a pathway to the end of the project.  The first example above with this particular diagram is referred to as a use case diagram. The two actors in this use case diagram are the “Student” and the “Campus Staff”. The actors will be the indivudals that interact with the student information system application. Each oval that is displayed are known as a use case. The use cases are the distinct functionality of the system that is wanted in the application. The use case diagram should be as simple as possible with the constuction of the diagram. This should be the most essential properties that are needed to construct. 
	
The next step for the team or yourself is to know that if there are details that need examined you can generate a class diagram of the student information system. This class diagram can break down more detail for the application. The kind of model a class diagram is would be a static model. Which either working with yourself or others will help with the reduction of maintenance that more than likely is going to occur during the projects build. Along side of this diagram you can incorporate CRC (Class, Responsibilites, Collaborators) cards.  

![image](https://user-images.githubusercontent.com/75941814/115123935-7eb61780-9f8d-11eb-929c-430e38c51b2f.png)

With the class digram created the CRC cards should have more detail about each use case that is significant within the project. This is where we can start to establish variable names that is going to be used in the code and will be a quick reference guide if troubleshooting occurs. As an example the numbering on the “Student” box has a numeric value of one. This is to tie the CRC card directly to that information in that box. The CRC card with have the use case name which is “Student” the identification of that box on the diagram which is the value of one. An importance level tied to that use case. The primary actor that is associated with the use case which is the student accessing the student information system. We can see the example of the CRC card below.

![image](https://user-images.githubusercontent.com/75941814/115123940-88d81600-9f8d-11eb-9c7b-d7cfb00c1711.png)
![image](https://user-images.githubusercontent.com/75941814/115123959-9db4a980-9f8d-11eb-85db-8123647efb42.png)

This card ties directly to the class diagram above. 
	
The important thing to keep in mind is the four phases of systems development life cycle. This consists of planning, analysis, design and implementation. While maintaining clarity with the association relationships between the actors and the use cases. This can best describe the communication between them. The extension of the functionality is maintained with the extended relationships between the use cases and the behavior that is wanted. The relationships need that detail to make sure that it is concise with the wanted outcome. Once the planning and anaylsis are incorporated into your design the next push would be to start drafting code for the application. From the use case diagram showing the general layout that is wanted to a more detailed breakdown in the class diagram, you are at a great starting point for the code to begin. Once the code is generated the implementation of that system is going to execute from the team that started this project. 



***************************************** Algorithms and Data Structure *****************************************

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


***************************************** Databases *****************************************

Databases are very useful tools when someone knows how to use the data in them. The first item a analyst should know is what data to collect. With the proper explanations as to why and how that data will be used in their outcome. This can grant a better perspective for the individual that is participating in the study with the data. The databases that will be used are smaller data sets and can simulate larger data sets. First, I will go through the database named, “roller coaster.xlsx”. I will use the program JMP to execute the visuals in the following figures. I am also familiar with the open source program JASP which has been very resourceful for home projects.

![image](https://user-images.githubusercontent.com/75941814/115123420-f6367780-9f8a-11eb-8473-52f17f28202a.png)
```markdown
Bivariate Fit of Duration By Length
 
Bivariate Normal Ellipse P=0.950
Variable	Mean	Std Dev	 Correlation	Signif. Prob	Number
Length	      3754.571	1589.455   0.800886	<.0001*	          78
Duration      139.5128	 42.6985	
```
*********Figure 1









```markdown
Multivariate 
Correlations
	      Duration	Speed	Height	Drop	Length	Inversions
Duration	1.0000	0.3918	0.3413	0.4326	0.8009	-0.1006
Speed	        0.3918	1.0000	0.7640	0.9211	0.5025	-0.2269
Height	        0.3413	0.7640	1.0000	0.7492	0.4209	-0.1781
Drop	        0.4326	0.9211	0.7492	1.0000	0.5328	-0.2277
Length	        0.8009	0.5025	0.4209	0.5328	1.0000	-0.3750
Inv            -0.1006 -0.2269 -0.1781 -0.2277 -0.3750	 1.0000
```
Scatterplot Matrix

 ![image](https://user-images.githubusercontent.com/75941814/115123538-7eb51800-9f8b-11eb-8289-6517413cc457.png)

*********Figure 2

Principal Components: on Correlations
Summary Plots
 
![image](https://user-images.githubusercontent.com/75941814/115123627-f2efbb80-9f8b-11eb-9e3a-7facc09bafff.png)

![image](https://user-images.githubusercontent.com/75941814/115123632-f8e59c80-9f8b-11eb-8bc4-4e279f2237db.png)

![image](https://user-images.githubusercontent.com/75941814/115123646-03079b00-9f8c-11eb-9289-b274c1fefffe.png)

*********Figure 3


With the gathered information from figures 1, 2 and 3 we can see the differences from a data set of roller coasters. Figure 1 is signifying the relationship between the duration in seconds you are on the roller coaster by the length of the roller coaster. As you can see the length of the roller coaster correlates to the duration you are riding the coaster. As the length increases it is seen that the duration of the ride is longer. The correlation shows close to +1 which shows an increase in the duration and length. The mean showing most coasters are around three thousand seven hundred feet and an average ride time of one hundred and forty seconds. This data set is coming from seventy-eight roller coasters.

Figure 2 is showing all the correlations between the variables from the data set. It is comparing duration, speed, height, drop, length and inversions. This matrix can show which points have a higher correlation than others. With the graph you can see that there is a significant correlation between the speed and drop of the seventy-eight roller coasters. When you look at the visual graphs of figure 2 you can see the oval is very tight when looking at the speed and drop. Almost all points are within the data set. Next in line would be that of figure 1, duration and length. Right behind that would be the height and speed of the roller coaster. Overall, the most significant values from the data set are the speed and drop. Which makes sense because the higher the drop of a coaster the more speed is gained from the gravity helping. This matrix also shows that the inversions of the roller coaster are not significant to all the other variables of the data set. As you can see in the matrix most of the ovals you can only see half of the oval trying to grab data from it. 

In figure 3 there are three different graphs to see the data sets. These points are principal components of the data set. With this figure we are eliminating the inversions value because it did not bring much correlation to the data. The values closet to +1 are significant values for using the data on the roller coasters. Which is shown in the eigenvalues in the first graph as a percentage and the correlation. 3.3 range is at 67.3% which is having much data not that significant to use. At the 21.5% for being close to +1 this data can be used with significant relation to a roller coaster. Which shows in figure 2 matrix. The third graph in figure three shows the close correlations to the variables. Duration and length then speed, drop and height. When you look at the figure 2 matrix you can see those ovals are tighter than those distancing themselves. Like duration and height being the farthest apart on figure 3 and showing a larger oval in figure 2. Identification of principal components are beneficial to finding correlating sources in your data set. 

An online retailer would be able to use a vast amount of data collected. With the customer information the retailer can predict what you want to look at or at least interested in. The customer searches can be tracked to steer the guessing of the retailer to what you want to buy. Indirect contact with the customer with customer focused outlook when they utilize the site. With this creating a more personalized experience for the customer. Which can lead to the advertising that the company wants to invest in. Thee spending habits a customer displays can also increase the personalization for the retailer to home in on. An example would be from Netflix, the more movies you watch the more data collected. Then Netflix would be able to categorize movies that the customer would be more likely to watch. Two components of the data system would be searches and habits from the customer. 

Data warehouse would be collecting all the customer and retailer information. The warehouse would act as a library for data analysis to choose what variables they need. The analyst would not need all the data stored just specific data to correlate to the study at hand. That would consist of also what was said above with the searches and habits. That would not be the only data collecting. From internal and external data such as stock quantity and price tracking. The retailer would have to keep up with competition by checking to make sure they can deliver the best prices for customers to return to their online retailer. The data warehouse would provide information to be able to make business decisions in the most effective manner. 

If the data collected within the retailer need more information the retailer would push for external data beyond their internal sources. This can be comparative to gauging the retailer to a larger scale. Perhaps a school is taking a poll to see what type of phone is most widely used at that moment in time. Information such as that will let a retailer know if they need to stock their shelves and focus an investment to a product. That was an example, I am sure there would be multiple schools, reviews, government agencies and social media statistics to justify the purchase and engage the product. With multiple sources to tap into that can prove difficult to generate data for a single organizational answer. Making a large business decision off external sources needs a good amount of proof. So, research on the secondary sources would be extensive compared to the reliable internal sources at hand. The more internal retailer information that can be collected the better for verifying the external data possibly needed for proof on a retailer’s business decision.
Next, we will interpret the Bubba Gump company that is a restaurant chain.  

![image](https://user-images.githubusercontent.com/75941814/115123670-1a468880-9f8c-11eb-812f-46ccc3bba0dd.png)

Figure 4
 
![image](https://user-images.githubusercontent.com/75941814/115123677-25011d80-9f8c-11eb-891a-fd5e5ea8454f.png)
![image](https://user-images.githubusercontent.com/75941814/115123680-292d3b00-9f8c-11eb-8fcd-3ee6277de709.png)
![image](https://user-images.githubusercontent.com/75941814/115123686-2df1ef00-9f8c-11eb-8037-24bf46011562.png)
 
Figure 5

![image](https://user-images.githubusercontent.com/75941814/115123701-3a764780-9f8c-11eb-9fdd-1a5a6e4ba20a.png)
![image](https://user-images.githubusercontent.com/75941814/115123704-3e09ce80-9f8c-11eb-9b82-f717d1dcf28c.png)
 
Figure 6

![image](https://user-images.githubusercontent.com/75941814/115123714-495cfa00-9f8c-11eb-820c-f03897012b09.png)
 
Figure 7

![image](https://user-images.githubusercontent.com/75941814/115123724-537ef880-9f8c-11eb-8a99-9e30f22b29f8.png)

Figure 8


With the above information we can gain much oversight on how our webstore is performing. Let us begin with figure four showing the activity of the webstore. This is based out of the five hundred customers that participated in the survey. The number of visits is on the y axis and the money spent on the webstore is our x axis. All the blue in this figure is showing no profit being made by the webstore. It does show that up to three visits were made by the customers in the blue area. The green and red on the diagram is showing profit made by either one, two or three visits. This is also displaying that most of our customers are not using the webstore. We can focus on making the webstore more user friendly with a targeted survey on just that. The customers are fifty-fifty on whether they spend money on our webstore. We will go more in detail on this oversight of the webstore activity.

Figure five has multiple layouts to go over. This is showing characteristics with our customers and how much is spent on the webstore. The characteristics that were chosen for this comparison was income, age and if they were married. The income variable generated an outcome of decline with the higher incomes. Vast majority of webstore activity was from the forty to seventy thousand yearly income. This is showing the company that the range of income from the customers slightly reflects on if they are going to use the webstore. Not solid information but information none the less. Next, we can see the activity of the webstore by age of the customer. The population at forty and below are more inclined to use the webstore than that of ages fifty and above. There is a slight gap between forty and fifty but nothing major. The older generation seems to not use or spend as much when it comes to the webstore. The last variable used was the status of the customer. With the married status they were spending more on the webstore. This could be due to having a family and bringing the food or merchandise home. This shows that family (more than one) customers tend to gauge more on the webstore and can be beneficial to know for making family deals on the webstore. 

With the next figure (Fig. 6) we can display the number of visits matched against the webstore to the restaurant. This is based on the restaurant identification to match the visits to them. With the results that we need to address. Some restaurants do not receive a third visit which can be disturbing to the company as to why. The webstore also shows a slight decline but not as major as the restaurant visits. The basis of this is regarding the webstore but wanted to show a discovery with the data to be later addressed. The focus on the webstore does show that the restaurants are more inclined to get webstore purchases rather than the restaurant visits. Steadily tapering off with the more visits which does need addressed. The first step with our webstore impacting better we should amplify or revamp our webstore to accommodate the customer easier. 

The next two figures (Fig.7 and Fig. 8) I want to tie together. This is good information for some good news. Figure seven is showing the third spending with webstore and restaurant visits. Also wanted to show the restaurant visits due to the webstore generating a zero visit so the data can coincide. More third visit spending is higher at the restaurant but as before seen the visits are declining with the customers. Here it is showing the webstore visits need more of an impact on the customer to want to use the website again. Then when we see figure eight is when we see the good news. Figure eight is displaying that with the webstore visits increase so does the spending on the webstore. This may seem conflicting because I compared this to the third visit spending that did not show this. Overall, the webstore is receiving a higher spending rate with a broader outlook other than just one visit. The data set that we have can cover information that might give false outcome. This is good news for the webstore just as I said before we should probably focus on a targeted survey for the webstore. So, we can focus on customer wants and needs to better our customers experience with the website.  

The company should focus on the survey results as a baseline to begin a trend analysis. As stated, "clustered" results would be informational to the business to find the current trend of the time. Be able to generate a farther outlook to what we need to do in the future. Delivering a survey for credits is a great start to understand the customer habits. The data warehouse that the company has now gives us some background to match to the survey given. The ability to grow in the future and adjust to what the next priority that is wanted. The data warehouse collecting the point of sale, web sales, customer information and sales transactions are enough to get started with the data analysis. We can focus on what the customer uses more being at the store or online services. We should begin with a descriptive analysis approach. Focus on the data at hand and see what the benefits can come of it. To focus on the customers and the point of sales generates use of that data alone. Future steps can be made to begin another focal point but let us start small then gradually increase the use of other data. With this method we can create a solid baseline for our data collected. We will conquer the steps to move in the direction Bubba Gump needs.

A question to be addressed is needing more data and less data. Let us focus on more of the purchasing methods and each purchase (web or restaurant) and gathering meaningful data that can better our results. With the give and take let us take away the marriage status columns (Married_YN, MARR_BIN) and add other column(s) for the purchases. Add RESTAURANT_SPEND and HOUSEHOLD_AMOUNT so the comparison can be made on which one is making more. For future analysis this will grant solid information when comparing the two, restaurant or webstore. Household amount can show trends with larger purchases and make more sense with them. With the data we have now I want to show an analysis to move forward with my decision and have management make the final decision. 

Measuring progress on the matter is not to lose the data we are using. To have this data on hand for future analysis will prove to be valuable. The data gathered from the web store is a focus now. Able to compare the data we gather now and project it towards our next step. Compare the web store to the restaurant purchases. Show some trends within our customers to make our data for the webstore more intriguing. This will show which direction we can take on making more profit for Bubba Gump Company. On top of making more profit making it easier for the customer to connect to Bubba Gump company. The webstore can grant that aspect for the customer to connect virtually and have a great experience while doing so. 

Following up on the comparison of web versus restaurant will benefit and amplify on the original data that is collected now. I am sure the best interest would be to make more profit and customer satisfaction. Let us find what the customer uses more and give them a more enhanced way to make their purchases. We can identify trends in the customer to show what age, income or status to target for sales. Will we be able to generate a new survey with different information that is needed? This will be able to use our data now and match it to a future dataset. 

The resource that will come in handy is the data preparation for the next step for the company to visually decide to make forward progress. Keep a published document for monitoring the steps we are making to better the Bubba Gump Company. This can be traceable for your company to keep up to date information. Another resource we can incorporate is questions document brought up by management from the Bubba Gump Company to assess for discussion with the data analysis department. We can work together on this focus for the company’s behalf. We do not want to lead astray the company from their wants and needs. Let us create the background of the company’s interest and make the best effort to accommodate to Bubba Gump’s focus. We will also use some external data to compare to our information received from our customers. Additionally, incorporating the external data to support our data for analysis. 

Bubba Gump Company’s stepwise approach is focusing on the value of the webstore. We have broken down some data from the data center to come up with some solid background to the webstore. We also have data that is out of our control with what we have, and we will go over both aspects. The effective material that we have collected reflects on the five hundred customers use of the webstore. This can display how many customers are using the webstore to purchase and shows how many customers use the webstore and do not purchase. This information can generate a new survey to expose the question to why they log onto the webstore but do not purchase. We can identify the population of the five hundred customers per income, age and marital status. The data collected on the population can reflect focusing on a generation that uses Bubba Gump’s products more. One element that we do not have control over is the restaurant visits and how much went to the restaurant versus the webstore. Our data is more focused on the webstore and should have more information pertaining to the webstore and tie the data with the webstore more. The difference of restaurant to webstore is out of our control when it comes to analyzing the data. We cannot tie a webstore visit to a restaurant visit expenditure with the third visit column. As shown above in data visualizations we can use the third spending for the restaurant spending in this case until more information is gathered.
 
![image](https://user-images.githubusercontent.com/75941814/115123734-62fe4180-9f8c-11eb-9054-cf49cfec7c71.png)
![image](https://user-images.githubusercontent.com/75941814/115123737-672a5f00-9f8c-11eb-83e4-df1ede106493.png)
![image](https://user-images.githubusercontent.com/75941814/115123739-6abde600-9f8c-11eb-8aa2-52b8769fbadf.png)
![image](https://user-images.githubusercontent.com/75941814/115123744-6eea0380-9f8c-11eb-8d7d-0a79239670bb.png)
 
There is a source of error I had to address when using the data that is present. That was focusing on the webstore and most data pulled reflected a downgrade to the information. The data was showing more customers using the webstore but not purchasing. It also was showing that the older generations were not using the webstore as much. The higher income customers were not using the webstore and was showing a decline in that data. All data sets generated was showing that solid decline in our information. Then with and overview of webstore visits to webstore spending the incline appeared. If the in depth digging of the information did not happen then one might see a failure in the webstore when there is light at the end of that tunnel. It is worth adjusting the budget to amplify on the webstore’s appearance and user-friendly experience.

There are meaningful patterns with the data pertaining to our customers. As stated above our customers gave information about their income, marital status, age, and location. The webstore activity and spending are the information that can be tied directly to what we need to focus on. This does raise question to be able to get the best out of the data by asking each spend and if restaurant or webstore. That information can pinpoint the data set to have heavier focus on a known outcome. Third visits need some more clarification to its meaning I believe. Modify the column to reflect more information to what we need. Manage a database with the proper information will always be a very powerful tool to gain outlooks on many situations. 

Abiteboul, S., Hull, R., & Vianu, R. (1995). Foundations of Databases. Addison-Wesley.
Mood, A. M. (1950). Introduction to the theory of statistics. McGraw-Hill.
Blalock, H. M., Jr. (1960). Social statistics. McGraw-Hill.
Gerd Gigerenzer, Mindless statistics, The Journal of Socio-Economics, Volume 33, Issue 5, 2004, Pages 587-606, ISSN 1053-5357, https://doi.org/10.1016/j.socec.2004.09.033.
(https://www.sciencedirect.com/science/article/pii/S1053535704000927)

***************************************** Self Assessment *****************************************

My name is Eric Clancy and I have been in the Computer Science program at Southern New Hampshire University and graduated May of 2021. Before engaging with the university, I was just tinkering with C++ coding for fun to figure out how simple operations functioned. When I found myself spending many hours of trying to decipher simple operations of the code, that is when I met my wife, Christine. She knew I wanted to learn more about coding and began her trek on my outlooks of how to learn that. My loving wife re-activated my GI Bill from the military and began phone calls to schools. Southern New Hampshire University piqued my interest and none the less had a great military advisor call me and speak with me with clarity and laid out the entire program of what I needed. I was ready to make the next push and jump in. 
	
The courses that were placed in front of myself were not an easy task to complete. As I was learning about coding there was so many different avenues of that field. I was unaware of ninety percent of courses that were being taught to me from SNHU. The first class that sunk in deep was the software automation course. The programmers code sent to an individual to dissect and find bugs that would normally not show on a “normal” user run of the program. This was identifying issues that could be automated and run through a script that was generated to create those errors. The next course that I found to be paramount in my journey to software field was Secure Coding. Secure Coding introduced to me the fact that proper syntax and little variables could open a wide door for un-ethical individuals to begin to infiltrate your code/program. Again, showing me that creating secure code was a must if creating code, especially for a company that has sensitive information. Best practices need to be more than just a best but a must that should be present and always in the mind of the programmer. The third but not final important concept is the knowledge of Reverse Software Engineering. Once again, this course opened my eyes more on the field of software development. Able to re-learn code without source code is a big step in understanding another process that was out of my head. This could show weakness and if the programmers practiced Secure Coding and Test Automation of their software, reverse engineering code would not be necessary. Which I was wrong about software reverse engineering, can be once again another method of testing just with a program that you do not have access with. All the tools mentioned above are verification and validation methods of a good sound program and well-structured code. The code created has many ways of testing and making sure there are no holes for hackers to sneak in. 
	
Which “section” in that field do you ask? The answer to that question and the teachings from SNHU show that I can engage in many different sectors with the software field. I am new to this and would take an entry level position with this company and if that goal runs dry after obtaining my degree, I will look elsewhere with the smallest time gap of obtaining the degree. My specialization will be decided with the current opportunity presented to me. I am eager to begin another chapter in my life and software development is in that next chapter.       


