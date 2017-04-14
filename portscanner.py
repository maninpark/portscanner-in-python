import socket,subprocess,sys,thread
from datetime import datetime



#list for most used port numbers

most_used = [20,21,22,23,25,53,67,68,69,80,110,123,137,138,139,143,161,162,179,389,443,636,989,990]

#taking inputs

remoteServer = raw_input("Enter a remote host to scan : ")
remoteServerIP = socket.gethostbyname(remoteServer)

print 'What type of ports you want to scan : \n 1. TCP \n 2. UDP'
print '-' * 60

scan_type = input('Enter your choice : ')



if scan_type == 1:
	print 'What do you want to scan \n 1. Most commonly used ports\n 2. Specific ports'

	print '-' * 60

	choice = input('Enter your choice for port selection : ')
	scan_type = TCP
	

	if choice == 1:
		t1 = datetime.now()

		try:
			for port in most_used:
				sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

				result = sock.connect_ex((remoteServerIP,port))
				
				if result == 0:
					
					print "Port{}:	Open".format(port)
					print socket.getservbyport(port,str(scan_type))

					sock.close()
			t2 = datetime.now()

			total = t2-t1


			print "scanning completed in : ", total
		except KeyboardInterrupt:
			print "You pressed Ctrl+C"
			sys.exit()

		except socket.gaierror:
			print 'Hostname Could not be resolved so Exiting'
			sys.exit()

		except socket.error:
			print 'Could not connect to server'
			sys.exit()


	elif choice == 2:

		#specify ports here


		starting_port = input("Enter starting port : ")

		ending_port = input("Enter ending port (Maximim 10000) : ")



		print '-' * 60
		print 'Please wait while the scanning remote host %s' %remoteServerIP
		print '-' * 60



		t1 = datetime.now()
		scan_type = 'TCP'




		try:
			for port in range(starting_port,ending_port):
				sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				result = sock.connect_ex((remoteServerIP,port))
				if result == 0:
					
					print "Port{}:	Open".format(port)
					print socket.getservbyport(port,str(scan_type))


					
					sock.close()
			t2 = datetime.now()

			total = t2-t1


			print "scanning completed in : ", total
		except KeyboardInterrupt:
			print "You pressed Ctrl+C"
			sys.exit()

		except socket.gaierror:
			print 'Hostname Could not be resolved so Exiting'
			sys.exit()

		except socket.error:
			print 'Could not connect to server'
			sys.exit()

	else:
		print 'Invalid option. Select valid ports to scan.'
		sys.exit()

elif scan_type == 2:
	
	print 'What do you want to scan \n 1. Most commonly used ports\n 2. Specific ports'

	print '-' * 60

	choice = input('Enter your choice : ')
	t1 = datetime.now()
	scan_type = 'UDP'


	try:
		for port in most_used:
			sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

			result = sock.connect_ex((remoteServerIP,port))
			#services = sock.getservbyport(port)
			if result == 0:
				
				print "Port{}:	Open".format(port)
				print socket.getservbyport(port,str(scan_type))

				
				sock.close()
		t2 = datetime.now()

		total = t2-t1


		print "scanning completed in : ", total
	except KeyboardInterrupt:
		print "You pressed Ctrl+C"
		sys.exit()

	except socket.gaierror:
		print 'Hostname Could not be resolved so Exiting'
		sys.exit()

	except socket.error:
		print 'Could not connect to server'
		sys.exit()

else:
	print 'Invalid Option. Please select valid scan type option.'





