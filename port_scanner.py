#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
	target =socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4

else:
	print("Invalid amount of argument")
	print("syntex:python3 port_scanner.py <ip>")

#Add a pretty banner to make it cool

print("-"*50)
print("Scanning target"+target)
print("Time started"+str(datetime.now()))
print("-"*50)

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #AF_INET is IPv4 and SOCK_STREAM is our port
		socket.setdefaulttimeout(1)  
#this is going to connect to the port.If the port is not connected it is going to wait for 
#1 sec and move on.
		result=s.connect_ex((target,port))  #retruns an error indicator(boolean value)
		if result==0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:    #like Ctrl+c
		 print("\nExiting program.")
		 sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit() 

except socket.error:
	print("Couldn't connect to server")
	sys.exit()


