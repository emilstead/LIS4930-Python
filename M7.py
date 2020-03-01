#Module 7 Assignment 
#03/01/2020 
#Emily Milstead

#This properly runs the current date and time to the milisecond for question #1.  
import datetime 
x = datetime.datetime.now()
print("The current time is:")
print (x)
print()


# 1. "Try the code below and revise it to current time."
# Professor's code that would not run properly. 

#Revised code to output the current date & time.
import sys
x= datetime.datetime.now()
m= x.strftime ("%B")
d= x.strftime ("%d")
y= x.strftime ("%Y")
print ("Today's date is:")
print (m, d, y)
print()

#Did not use this portion of Professor's code once revised. 
# for line in sys.stdin:
# data = line.strip().split("\t")
# if len(data) == 6:
# date, time, store, item, cost, payment = data
# print "{0}\t{1}".format(item, cost)


#2a. "Add the timedelta to the datetime and subtract 60 seconds and add two years."
#2b. "For each condition, state the code and output."
from datetime import datetime, timedelta 
print("The date/time at this exact moment, one week ago was:")
print (x - timedelta(days=7))
print ()
  

# 3. "Create a timedelta object representing 100 days, 10 hours, and 13 minutes."
from datetime import timedelta 
print ("The date/time 100 days, 10 hours, and 13 minutes ago was:")
print (x - timedelta(days=100), timedelta(hours=10), timedelta(minutes=13))

# 4. "Write a function that takes two arguments (feet and inches) with this time object."

#1st attempt, nothing output
# import datetime
# from datetime import timedelta
# feet1=6
# inches1=2 
# feet2=3
# inches2=1

# datetimeFormat = m, d, y
# date1 = datetime.datetime.now()
# date2 = datetime.datetime.now() - timedelta(days=2)
# diff = datetime.datetime.strptime (feet1, inches1, date1, datetimeFormat)\
# 	-datetime.datetime.strptime (feet2, inches2, datetimeFormat)
# print ("difference:", diff)

#2nd attempt, nothing output
# def log(feet, inches, when=datetime.now()):
# 	print ('%s, %s' % (when, feet, inches))
# log(6,2) 
# sleep(days=1)
# log (3,1)
# from datetime import datetime 
# datetime_object = datetime.now()
# feet1 = 6
# inches1= 2
# feet2=3
# inches2=1
# print(x, feet1, inches1) - (timedelta(days=2), feet2, inches2)