# Module #9 TestCase page
# 03/15/2020 
# Emily Milstead


import unittest
from M9 import add

class addTest (unittest.TestCase):
	def test_add (self):
		p=add()
		p.sum(2+3)
		assert p.sum() == 5

