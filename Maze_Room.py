#Author: Owen Mearns
#Purpose: Make a maze some one can naviagte

class Room:
	#constructor, descr is description of Room
	#also it initialises the four links(north, east, west, south) to None
	def __init__(self, descr):
		self.descr = descr
		self.east = None
		self.west = None
		self.north = None
		self.south = None
	
	#returns string description of the Room
	def __str__(self):
		return self.descr
	
	#returna north variable
	def getNorth(self):
		return self.north
	
	#returns south variable
	def getSouth(self):
		return self.south
	
	#returna east variable
	def getEast(self):
		return self.east
	
	#return west variable
	def getWest(self):
		return self.west
	
	#set the value of descr variable
	def setDescription(self, d):
		self.descr = d
	
	#set the value of north variable
	def setNorth(self, n):
		self.north = n
	
	#set the valie of south variable
	def setSouth(self, s):
		self.south = s
	
	#set the value of east variable
	def setEast(self, e):
		self.east = e
	
	#set the value of west variable	
	def setWest(self, w):
		self.west = w
