#!/usr/bin/env python
from datetime import datetime
import socket,sys

def port_scanner(port_no,scan_type):

	if scan_type == 'TCP':
		protocol = socket.SOCK_STREAM
	elif scan_type == 'UDP':
		protocol = socket.SOCK_DGRAM









#input of remote host


	remoteServer = raw_input("Enter a remote host to scan : ")
	remoteServerIP = socket.gethostbyname(remoteServer)

	t1 = datetime.now()

	try:
		for port in port_no:
			sock = socket.socket(socket.AF_INET,protocol)

			result = sock.connect_ex((remoteServerIP,port))
			
			if result == 0:
				
				print "Port{}:	Open".format(port) + '  ' + socket.getservbyport(port,str(scan_type))
				#print socket.getservbyport(port,str(scan_type))


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




