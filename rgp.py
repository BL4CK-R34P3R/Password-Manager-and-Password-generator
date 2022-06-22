#!/usr/bin/env python3
import sys
import random
import os
import os.path
from os import read
import subprocess
############################### Functions ######################
### generate password ###
def generate():
	username = input("username:")
	mail = input("mail:")	
	social = input("social media:")

	index = 0
	sf=open('password.txt','r')

	for line  in sf:
		if username in line and social in line:
			index = 1
	if index == 1:
		print("credentials exist run again and update it")
	elif index == 0:
		username = f"username:{username}"
		mail = f"mail:{mail}"
		social = f"social:{social}"

		lower = "abcdefghijklmnopqrstuvwxyz"
		upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		num = "1234567890"
		symbols = "!@#$%^&*().><,"

		strings = lower + upper + num + symbols
		password = "".join(random.sample(strings,16))
		password= f'password:{password}'

		with open('password.txt','a') as f:
			f.write('\n')
			f.write(username)
			f.write(' ')
			f.write(social)
			f.write('\n')
			f.write(mail)
			f.write('\n')
			f.write(password)
			f.write('\n')
	subprocess.call(['sh', './encode.sh'])
### search password ###
def search():
	s_username = input('username: ')
	s_social = input('social media name:')
	flag = 0
	upto = 0
	index = 0
	sf=open('password.txt','r')

	for line  in sf:
		flag += 1
		if s_username in line and s_social in line:
			upto = flag + 2
			index = 1
			with open('password.txt','r') as sf1:
				rd = sf1.readlines()
				rd1 = rd[flag:upto]
				print (rd1)
	if index == 0 :
			print("credentials does not exist in logs")
	subprocess.call(['sh', './encode.sh'])
### update ###

def update():
	def delete_line(original_file, line_number):
		is_skipped = False
		current_index = 0
		dummy_file = original_file + '.bak'

		with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
			for line in read_obj:
				if current_index != line_number:
					write_obj.write(line)
					current_index += 1
				else:
					is_skipped = True
					current_index += 1

				

		if is_skipped:
			os.remove(original_file)
			os.rename(dummy_file, original_file)
		else:
			os.remove(dummy_file)


	s_username = input('username: ')
	s_social = input('social media name:')
	find = 0
	flag = 0
	upto = 0
	index = 0
	sf=open('password.txt','r')

	for line  in sf:
		find += 1
		if s_username in line and s_social in line:
			flag = find - 1
			upto = flag + 2
			index = 1
			delete_line('password.txt',upto)
			delete_line('password.txt',upto-1)
			delete_line('password.txt',upto-2)
			print("\n enter new credentials \n")
			generate()
	if index == 0 :
		print("credentials does not exist in logs")
	subprocess.call(['sh', './encode.sh'])
### clear logs ###
def clear():
	os.remove("password.txt")
### 
###########################################################################
try:
	while 1:
		subprocess.call(['sh', './decode.sh'])
		print("\n--> 0 to exit\n--> 1 to display all password log \n--> 2 to generate random password \n--> 3 to search password\n--> 4 to update\n--> 5 to clear logs\n--> 6 clear previous log and generate new log")
		var = input("choose:")
		print("\n")

		if (var == "1"):
			path = str(os.path.isfile("password.txt"))
			if (path == "False"):
				print("\n log does not exist")
		
			else:
				f = open("password.txt", "r")
				print(f.read())
				subprocess.call(['sh', './encode.sh'])

		elif(var == "2"):
			path = str(os.path.isfile("password.txt"))
			if (path == "False"):
				print("\n log does not exist")
			else:	
				generate()

		elif(var == "3"):
			search()
		elif(var == "4"):
			update()

		elif(var == "5"):
			path = str(os.path.isfile("password.txt"))
			if (path == "False"):
				print("\n log does not exist")
				exit()
			else:
				clear()
		elif(var=="6"):
			raww = input("are you sure y/n::")
			if (raww == "y"):
				with open('password.txt','w') as f:
					f.write("### password Log ###")
					f.write("\n")
				subprocess.call(['sh', './encode.sh'])

		elif (var == "0"):
			subprocess.call(['sh', './encode.sh'])
			exit()

		else:
			print("invalid choice")
			subprocess.call(['sh', './encode.sh'])

except KeyboardInterrupt:
	subprocess.call(['sh', './encode.sh'])
	sys.exit()