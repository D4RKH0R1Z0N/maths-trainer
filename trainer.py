from sys import platform, exit
try:
	from colorama import init, Fore
except:
	print("Please Install colorama!")
	exit()
try:
	from random import randint
except:
	print("Please Install random!")
	exit()
import os
init(autoreset=1)

if platform == "win32":
	clear = "cls"
else:
	clear = "clear"

def custom_level_1():
	global list_from
	global rand1
	print("\nMake Number List From : ")
	list_from = input()
	if list_from.isdigit():
		list_from = int(list_from)
		rand1 = list_from
	else:
		print("Please Enter a number!")
		custom_level_1()

def custom_level_2():
	global list_to
	global rand2
	print("\nMake Number List From", rand1, "To : ")
	list_to = input()
	if list_to.isdigit():
		list_to = int(list_to)
		if list_from == list_to:
			print("Can't Input the same Number!")
			custom_level_2()
		rand2 = list_to
	else:
		print("Please Enter a number!")
		custom_level_2()

def custom_level():
	custom_level_1()
	custom_level_2()

def get_difficulty():
	global level
	global rand1
	global rand2
	print("Enter Difficulty From 1 to 5 or enter 0 to make a custom Difficulty : ")
	difficulty = input()

	if difficulty == "1":
		rand1 = 5
		rand2 = 50
	elif difficulty == "2":
		rand1 = 100
		rand2 = 200
	elif difficulty == "3":
		rand1 = 250
		rand2 = 500
	elif difficulty == "4":
		rand1 = 600
		rand2 = 1500
	elif difficulty == "5":
		rand1 = 2500
		rand2 = 10000
	elif difficulty == "0":
		custom_level()
	else:
		os.system(clear)
		print("Please Enter a Valid Difficulty!\n")
		get_difficulty()

os.system(clear)
get_difficulty()
os.system(clear)

def program():
	def get_operator():
		global opr1
		global opr2
		global operator
		global c_operator
		opr1 = 1
		opr2 = 4
		operator = randint(opr1, opr2)
		if operator == 1:
			operator = "+"
			c_operator = 1
		elif operator == 2:
			operator = "-"
			c_operator = 2
		elif operator == 3:
			operator = "*"
			c_operator = 3
		elif operator == 4:
			operator = "/"
			c_operator = 4
		else:
			print("Unknown Error")
			exit()

	get_operator()
	num1 = randint(rand1, rand2)
	num2 = randint(rand1, rand2)
	if c_operator == 1:
		calculated = num1 + num2
	elif c_operator == 2:
		if num1 < num2:
			calculated = num2 - num1
		else:
			calculated = num1 - num2
	elif c_operator == 3:
		calculated = num1 * num2
	elif c_operator == 4:
		calculated = num1 // num2
	else:
		print("Unknown Error")
		exit()
	print(num1, operator, num2)
	def get_answer():
		global answer
		answer = input("Enter answer : ")
		if answer.isdigit():
			answer = int(answer)
		else:
			os.system(clear)
			print("Please Enter a number!\n", num1, operator, num2)
			get_answer()
	get_answer()
	os.system(clear)
	if answer == calculated:
		print(Fore.GREEN + "Correct!")
	else:
		print(Fore.RED + "Wrong!")

try:
	while True:
		program()
except KeyboardInterrupt:
	os.system(clear)
	print("Exiting...")
	exit()