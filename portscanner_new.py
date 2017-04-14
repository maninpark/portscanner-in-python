import test_function

import socket,subprocess,sys,thread
from datetime import datetime



#list for most used port numbers

most_used = [20,21,22,23,25,53,67,68,69,80,110,123,137,138,139,143,161,162,179,389,443,636,989,990]

#taking Inputs


print 'What type of ports you want to scan : \n 1. TCP \n 2. UDP'
print '-' * 60

scan_type = input('Enter your choice : ')

if scan_type == 1:
	scan_type = 'TCP'
elif scan_type == 2:
	scan_type = 'UDP'

else:
	print 'Choose valid scan type...!'
	sys.exit()



print 'What do you want to scan \n 1. Most commonly used ports\n 2. Range of ports\n 3. Specific ports'

print '-' * 60

choice = input('Enter your choice for port selection : ')

if choice == 1:
	choice = most_used
elif choice == 2:
	
	port_range_min = input('Enter starting port number : ')
	port_range_max = input('Enter ending port number (less than 65536) : ')
	choice = range(port_range_min,port_range_max)

elif choice == 3:
	total = input('Enter total number of ports you want to scan : ')
	choice = []
	for i in range(total):
		item = input('Enter one port at a time : ')
		choice = choice.append(item)
else:
	print 'Enter valid port selection choice...!'
	sys.exit()





test_function.port_scanner(choice,scan_type)