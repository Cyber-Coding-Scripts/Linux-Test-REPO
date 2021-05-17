import os, platform
import subprocess
import platform
import socket
import random
import string
import time
import os

path = 'C:/'
path2 = 'E:/'
path3 = 'D:/'
quit = "/h"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
chars_e = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

print("""Kinect | Cyber Terminal [Version 1.00]
(C) Kinect Software. All rights reserved.
	""")

def main():
	while True:
		command = input("@" + host_name + "> ")

		if command == '/t':
			print("Opening " + platform.system() + " " + platform.release() + " Terminal...")
			time.sleep(0.5)
			terminal()

		if command == 'list/C':
			list_C()

		if command == 'list/E':
			list_E()

		if command == 'ping':
			ping_s()

		if command == 'local':
			local()

		if command == 'proxy -w':
			proxy_w()

		if command == 'proxy -l':
			proxy_l()

		if command == 'help':
			help()

		if command == 'close':
			break

		if command == 'password':
			password()

		if command == 'color 0':
			os.system('color 0')

		if command == 'color 1':
			os.system('color 1')

		if command == 'color 2':
			os.system('color 2')

def terminal():
	while True:
		command2 = input("@" + host_name + "/>> ")

		if command2 == quit:
			print("Opening Home Terminal...")
			time.sleep(0.5)
			main()
		else:
			os.system(command2)

def list_C():
	dir_list = os.listdir(path)
	print("Files and Directories in '", path, "' :")
	print(dir_list)

def list_E():
	dir_listE = os.listdir(path2)
	print("Files and Directories in '", path2, "' :")
	print(dir_listE)

def ping_s():
	host = input("Enter Website To Ping: ")
	number = input("Enter How Many Times To Ping: ")

	def ping(host):
		param = '-n' if platform.system().lower() == 'windows' else '-c'
		run = ['ping', param, number, host]
		return subprocess.call(run)
	print(ping(host))

def local():
	print("Your Local IPS Is: " + host_ip)

def proxy_l():
	port = input("Enter Port: ")
	os.system('python3 -m http.server ' + port)

def proxy_w():
	port2 = input("Enter Port: ")
	os.system('python -m http.server ' + port2)

def password():
    number_e = input('Please Enter a Number of Passwords to Genirate: ')

    try:
    	number_e = int(number_e)
    except:
    	print("Error, please enter a number!")

    length_e = input('Enter how Many Chacaters To a Generate: ')
    try:
    	length_e = int(length_e)
    except:
    	print("Error, please enter a number!")
    print('\nHere are your password(s): ')

    for pwd_e in range(number_e):
    	password_e = ''
    	for c in range(length_e):
    		password_e += random.choice(chars_e)
    	print(password_e)

def help():
	print("""
[/t] Switch into terminal commands
[list/C] List all file in the C:/ Drive
[list/E] list all files in E:/ drive
[ping] Ping any website
[local] list your local IPS
[proxy -w] create a proxy server for windows
[proxy -l] create a proxy server for linux
[close] Close the terminal
[help] list all commands for Cyber-Terminal
	""")

main()
