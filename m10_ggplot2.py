# Module #10 - ggplot2
# 03/28/2020 
# Emily Milstead

#ggplot
from ggplot import *
import numpy as np

#Positive cases of COVID-19 as of 03/28/2020 @ 4:54pm: 
data = {
	"United States": 116505,
	"Italy": 92472,
	"China": 81999
}


ggplot (data, aes(x='Countires', y='Positive Cases of COVID-19'), data = 'data' +\
 	geom_bar())
