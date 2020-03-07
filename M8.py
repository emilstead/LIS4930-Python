# Module 8 Assignment
# Emily Milstead
# 03/07/2020

# Find or create your own data set. 
# Conduct four types of interator functions. 

#Data set:
females = ['Emily', 'April', 'Stephanie', 'Tania', 'Erin']
males = ['Kevin', 'Raymond', 'Manuel', 'Odel', 'George']
x= [2,4,6,8,10]
y = [1,3,5,7,9]

#import itertools library
import itertools


#itertools - repeat function
print("Females listed twice:")

for i in itertools.repeat(females,2):
	print (i)
	print()

print("Males listed twice:")
for i in itertools.repeat(males,2): 
	print (i)
	print()

#itertools cycle function
print("This is the output from the cycle fucntion:")
count=0
for i in itertools.cycle(x):
	if count >9:
		break
	else:
		print(i, end = " ")
		count+=1
		print()

#itertools chain function 
print()
print("This is the output for the chain function:")
for i in itertools.chain(females,males):
 	print(i)
print()

#itertools islice function
print("This is the output for the slice function:")
from itertools import *
for i in itertools.islice(count(), 5):
	print(i)
