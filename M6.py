#Module 6 Assignment
#02/22/2020 
#Emily Milstead

#Creating function with class rectangle:

#
graphics.py 
from graphics import * 
win = Graphwin ('rectangle', 320, 200)
win.setBackground ('white')

#Main
c = rectanlge(point(30,40), Point(240,170))
c.setFill('red')
c.setOutline('black')
c.draw(win)

win.getMouse() #Pause for click in window
win.close()
print ('done')


#class Rectangle():


#	def __init__(self, width, height, x, y):
#'''Create rectangle at position x,y with height and width w, h'''
#		self.width = width
#		self.height = height
#		self.x = x
#		self.y = y

#	def dispString(self):
#'''Display Parameters of Rectangle in 4 Separate Strings'''
#		print('Width: ' + str(self.width))
#		print('Height: ' + str(self.height))
#		print('X-Coordinate: ' + str(self.x))
#		print('Y-Coordinate: ' +str(self.y))

#	def shiftRec(self, dx, dy):
#'''Shift X and Y Coordinates of Rectangle with Positive or Negative Values'''
#		self.dx = dx
#		self.dy = dy

#global x
#self.x = self.x + self.dx

#global y
#self.y = self.y + self.dy

#print('New X-Coordinate: ' + str(self.x))
#print('New Y-Coordinate: ' + str(self.y))

#def newRectangle(self, dx, dy):
#'''Create New Rectangle and Display its Parameters in Strings'''
#		self.dx = dx
#		self.dy = dy

#x1 = self.x + self.dx
#y1 = self.y + self.dy

#print('New Rectangle Created!')
#rint('Width: ' + str(self.width))
#print('Height: ' + str(self.height))
#print('X-Coordinate: ' + str(x1))
#print('Y-Coordinate: ' +str(y1))
	








#	def __init__(self, posn, w, h):
#		""" Initialize rectangle at posn, with width w, height h """
#		self.corner = posn
#		self.width = w
#		self.height = h

#	def __str__(self):
#		return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

#box = Rectangle((0, 0), 100, 200)
#bomb = Rectangle((100, 80), 5, 10)
#print("box: ", box)
#print("bomb: ", bomb)

#x= input("x-value")
#y= input("y-value")
#print ("Enter your x and y values: " + x + y )
 

#Testing functions:
"""
r1 = create_rectangle(10, 20, 30, 40)
print str_rectangle(r1)
shift_rectangle(r1, -10, -20)
print str_rectangle(r1)
r2 = offset_rectangle(r1, 100, 100)
print str_rectangle(r1) # should be same as previous
print str_rectangle(r2)

"""