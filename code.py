import subprocess
import platform
import socket
import time
import os

path = 'C:/'
path2 = 'E:/'
path3 = 'D:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("""Kinect | Cyber Terminal [Version 1.00]
(C) Kinect Software. All rights reserved.
	""")

while True:
	command = input("@" + host_name + "> ")

	if command == 'list/C':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)

	if command == 'list/E':
		dir_list2 = os.listdir(path2)
		print("Files and Directories in '", path2, "' :")
		print(dir_list2)

	if command == 'ping -s':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

	if command == 'local':
		print("Your Local IPS Is: " + host_ip)

	if command == 'proxy -l':
		port = input("Enter Port: ")
		os.system('python3 -m http.server ' + port)

	if command == 'proxy -w':
		port2 = input("Enter Port: ")
		os.system('python -m http.server ' + port2)

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))

	else:
		os.system(command)
