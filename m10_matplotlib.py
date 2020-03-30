# Module #10 - Matplotlib
# 03/28/2020
# Emily Milstead

#matplotlib importation
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()

#Positive cases of COVID-19 as of 03/28/2020 @ 4:54pm: 
data = {
	"United States": 116505,
	"Italy": 92472,
	"China": 81999
}

#X & Y axis value keys: 
x_axis_data = data.keys()
y_axis_data = data.values()

#How to plot a bar graph: 
ax.bar(x_axis_data, y_axis_data)

#Naming axes on a graph: 
ax.set(ylim = [0, 200000],
	ylabel='Positive Cases',
	xlabel='Countries',
	title='Comparing Positive Cases of COVID-19 Across Various Countries')

#Displaying the graph: 
plt.show()

