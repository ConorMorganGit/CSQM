# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("\n\n\tWelcome To The Calculator Program!!")
print ("\tThis repo is just for to test the Jenkins CI.")
print("\t===================================")
print("\t***********************************")

#function to add two numbers
def add(first_num,second_num):
	print ("{} + {} = {}".format(first_num,second_num,first_num + second_num))

#function to substract one number from another
def sub(first_num,second_num):
	print ("{} - {} = {}".format(first_num,second_num,first_num - second_num))

#function to multiply two numbers
def mul(first_num,second_num):
	print ("{} * {} = {}".format(first_num,second_num,first_num * second_num))

#function for division
def div(first_num,second_num):
	print ("{}/{} = {}".format(first_num,second_num,first_num/second_num))

print ('''
Enter + for addition
Enter - for Substraction
Enter * for multiplication
Enter / for Division
Enter q to Quit the program
''')

while True :
	print("")
	user_input = input ("Enter calculator type : ")
	if user_input == '+' :
		print ("To calculate (number 1 + number 2) :")
		add(int(input("Enter number 1 : ")),int(input("Enter number 2 : ")))
	elif user_input == '-':
		print ("To calculate (number 1 - number 2) :")
		sub(int(input("Enter number 1 : ")), int(input("Enter number 2 : ")))
	elif user_input == '*':
		print ("To calculate (number 1 * number 2) :")
		mul(int(input("Enter number 1 : ")), int(input("Enter number 2 : ")))
	elif user_input == '/':
		print ("To calculate (number 1 / number 2) :")
		div(int(input("Enter number 1 : ")), int(input("Enter number 2 : ")))
	elif user_input == 'q'
		break
		print ("")
	else:
		print ("Please Enter a Valid Input !!")
        
print("Here am tryint to break the program to test how Jenkins receat.")
print('We are trying to test the Jenkins')
main 