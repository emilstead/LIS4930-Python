#Emily Milstead 
#Module 5 Assignment 
#02/15/2020

#Question 1
print_code_steps = """
import math
def add (a,b):
	sum = a+b
	print("The sum of " + str(a) + " plus " + str(b) + " = " + str(sum))
add(2,6)
""" 
print(print_code_steps)

exec(print_code_steps)



import math
def add (a,b):
	sum = a+b
	print("The sum of " + str(a) + " plus " + str(b) + " = " + str(sum))





#Question 2
def whole_name(first_last_name,middle_name):
	return first_last_name[:6] + middle_name + first_last_name[5:]
print ()
print(whole_name('Emily Milstead','Grace'))
