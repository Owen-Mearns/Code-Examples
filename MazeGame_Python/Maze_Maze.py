class Maze:
	#constructor for Maze class
	#intialises the start(st), exit(ex) and current(cur) variable
	def __init__(self, st=None, ex=None):
		self.st = st
		self.ex = ex
		#initialise the current room to starting room
		self.cur=st
	
	#returns the current room
	def getCurrent(self):
		return self.cur
	
	#returns True if current room is exit room otherwise False
	def atExit(self):
		return self.cur == self.ex
	
	#moves to east or print invalid movement
	def moveEast(self):
		if self.cur.east == None:
			print("Direction invalid, try again.")
		else:
			self.cur = self.cur.east
			print("You went east")
	
	#moves to west or print invalid movement
	def moveWest(self):
		if self.cur.west == None:
			print("Direction invalid, try again.")
		else:
			self.cur = self.cur.west
			print("You went west")
	
	#moves to north or print invalid movement
	def moveNorth(self):
		if self.cur.north == None:
			print("Direction invalid, try again.")
		else:
			self.cur = self.cur.north
			print("You went north")
	
	#moves to south or print invalid movement
	def moveSouth(self):
		if self.cur.south == None:
			print("Direction invalid, try again.")
		else:
			self.cur = self.cur.south
			print("You went south")
	
	#sets the current Room as the starting room
	def reset(self):
		self.cur = self.st
		print("You went back to the start !")
