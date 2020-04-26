#Final Project 
#Emily Milstead 
#04/21/2020 

#In order to have the code run smoothly, we need to import a few libraries from Python to utilize. 
import math as m
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt

#The following line allows for graph plotting. 
fig, ax = plt.subplots()

#These are the names in each column from the CSV file. 
counties = []
population =[]
tested =[]
positive =[]
deaths = []


#Calculation variables that will be called in later in the code for percent calulations. 
ptest = []
i = []
death = []


with open ("fp_data.csv", 'r') as o:
    csv_reader = csv.reader(o, delimiter =',')
    next(csv_reader,None) #This line of code takes out the headers from your CSV file, in order to use only the values presented. 

     
#This reads the CSV and creates a list for each column.(This is embedded in the "with" statement.)
    for row in csv_reader:
        counties.append(row[0])
        population.append(row[1])
        tested.append(row[2])
        positive.append(row[3])
        deaths.append(row[4])


#Calculation for percent of population tested.
def pt2():
    for q in range (len(population)):
        x=population[q]
        y=tested[q]
        z=(int(y)/(int(x)))
        ptest.append(z)
pt2()


#Calculation for percent of population infected.
def pi2():
    for q in range (len(population)):
        x=population[q]
        y=positive[q]
        z=(int(y)/(int(x)))
        i.append(z)
pi2()


#Calculation for percent of population dead. 
def pd2():
    for q in range (len(population)):
        x=population[q]
        y=deaths[q]
        z=(int(y)/(int(x)))
        death.append(z)
pd2()


#Not needed for graph, but these are the values from the CSV & percentages calculated represented. 
print(counties)
print(population)
print(tested)
print(positive)
print(deaths)
print(ptest)
print(i)
print(death)

#This arranges the x-axis spacing/width to the number of counties provided.
x_indexes = np.arange(len(counties))

#Width of bars on graph.
width = 0.25

#This sets the range for the y-axis. 
plt.ylim(top=0.011)
plt.ylim(bottom=0)

#These are each bar on the graph including the width, color, and label, 
plt.bar(x_indexes - width, ptest, width = width, color="#000080", label= "Percent of Population Tested")
plt.bar(x_indexes, i, width = width, color="#0CD743", label= "Percent of Positive Cases")
plt.bar(x_indexes + width, death, width = width, color="#FF0000", label= "Percent of Deaths")

#This shows the legend for each color on the graph. 
plt.legend()

#This allows my x-axis to be names instead of numbers.
plt.xticks(ticks=x_indexes, labels=counties)

#These are the labels for each axis. 
plt.title("COVID-19 Population Percentages by County")
plt.xlabel("Counties")
plt.ylabel("Percentages")


#Displaying the graph: 
plt.show()
