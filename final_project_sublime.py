#Final Project 
#Emily Milstead 
#04/21/2020 

#In order to have the code run smoothly, we need to import a few libraries from Python. 
import math as m
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt

fig, ax = plt.subplots()
df= pd.read_csv("fp_data.csv")
dictionary=df.to_dict(orient='records')



#Lines 14-18 names each column list from my csv file. 
counties = []
population =[]
tested =[]
positive =[]
deaths = []
#Calculation variables
ptest = []
i = []
death = []

#Lines 22-30 creates a list of information from each column in my csv file. 
with open ("fp_data.csv", 'r') as o:
     csv_reader = csv.reader(o, delimiter =',')
     next(csv_reader,None) #This line of code is for if you do not want to include the headers from your csv file. 
     


     for row in csv_reader:
         counties.append(row[0])
         population.append(row[1])
         tested.append(row[2])
         positive.append(row[3])
         deaths.append(row[4])
         # p=row[1]
         # t=row[2]
         # s=row[3]
         # d=row[4]
         # ptested=(round(((float(t))/(float(p)))*100),4)
         # ppositive=(round(((float(s))/(float(p)))*100),4)
         # pdeath=(round(((float(d))/(float(p)))*100),4)
         # ptest.append(ptested)
         # i.append(ppositive)
         # death.append(pdeath)
        #ptest.append(round(((int(row[2])/(int(row[1]))*100),4))
         # i.append(round(((int(row[3])/(int(row[1]))*100),4))
         # death.append(round(((int(row[4])/(int(row[1]))*100),4))    
#ptest = []
#def ptestc():
def testcalc():
	 end_index = len(tested)

	 for i in range(end_index):
		 ptest.append(round((float(tested[i])/float(population[i])*100),4)
testcalc()
        #     for x in range(len(population)): 
#         result = (round(((int(tested[x])/(int(population[x]))*100),4))
#         ptest.append(result[x])
# i = []
# death = []

# data {["Population"] 
# }
#plt.style.use("fivethirtyeight")
#Lines 33-37 print the information from each column in my csv file as separate lists.          
# print(counties)
# print(population)
# print(tested)
# print(positive)
# print(deaths)
# print(ptest)
# print(i)
# print(death)

#         counties.append(row.split()[0])
#     print(counties)

# counties = dictionary[0]



#Naming variables to use and creating calculations. 
# def calcs ():
#     for row in dictionary:
#         p= row["Population"]
#         t= row["Population Tested"]
#         s= row["Positive Cases"]
#         d= row["Death Rate"]
#         cpopulation=p 
#         ptested=round(((t/p)*100),4)
#         ppositive=round(((s/p)*100),4)
#         pdeath=round(((d/p)*100),4)


#         gdata = {(row["County"], row["Population"],  ptested, ppositive, pdeath)}
# #    #gdata = {("Population of", row["County"], "=" ,row["Population"], "Percent of Population Tested:", ptested,"%", "Percent of Positive Cases:",ppositive, "%", "Death Rate:",pdeath,"%")}
#         print(gdata)
# calcs()

#Importation of matplotlib to graph my data.    
#import matplotlib.pyplot as plt 
#fig, ax = plt.subplots()

# #X & Y axis value keys: 
# x_axis_data = data.keys()
# y_axis_data = data.values()

# #How to plot a bar graph: 
# ax.bar(x_axis_data, y_axis_data)

# #Naming axes on a graph: 
# ax.set(ylim = [0, 200000],
#     ylabel='Positive Cases',
#     xlabel='Countries',
#     title='Comparing Positive Cases of COVID-19 Across Various Countries')

x_indexes = np.arange(len(counties))

width = 0.2
plt.ylim = (-5, 100)

#plt.bar(x_indexes - width, population, width = width, color="#FF0000", label= "Population")
plt.bar(x_indexes, ptest, width = width, color="#FFFF00", label= "Percent of Population Tested")
plt.bar(x_indexes + width, i, width = width, color="#FF0000", label= "Percent of Positive Cases")
plt.bar(x_indexes + width + width, death, width = width, color="#0CD743", label= "Percent of Deaths")

plt.legend()

plt.xticks(ticks=x_indexes, labels=counties)

plt.title("COVID-19 Population Percentages by County")
plt.xlabel("Counties")
plt.ylabel("Percentages")



# plt.tight_layout()

# #Displaying the graph: 
plt.show()



