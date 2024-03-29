from room import Room
from maze import Maze


def play(Maze):
	
	#keep running the loop till it finds exit where it breaks
	while not Maze.atExit():
		#print description of current room
		print(Maze.cur)
		
		#take as input the direction in which the user want to move
		dir = input("Enter direction to move north west east south restart\n")
		#move according to input from user
		if dir == "east":
			Maze.moveEast()
		elif dir == "west":
			Maze.moveWest()
		elif dir == "north":
			Maze.moveNorth()
		elif dir == "south":
			Maze.moveSouth()
		elif dir == "restart":
			Maze.reset()
		
		else:
			print("Invalid Entry")
			
		
	#if cuurent room is exit room then print it and break from the loop
	
	print("You found the exit!")
		


simpleRoom = []
for i in range(1,4):
	simpleRoom.append(Room("Room"+str(i)+""))

# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE
simpleRoom[0].setEast(simpleRoom[1])
simpleRoom[1].setWest(simpleRoom[0])

simpleRoom[1].setNorth(simpleRoom[2])
simpleRoom[2].setSouth(simpleRoom[1])
SIMPLE_MAZE = Maze(simpleRoom[0], simpleRoom[2])


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE
itermdiateRoom = []
for i in range(1,7):
	itermdiateRoom.append(Room("Room"+str(i)+""))

itermdiateRoom[0].setWest(itermdiateRoom[1])
itermdiateRoom[1].setEast(itermdiateRoom[0])

itermdiateRoom[1].setWest(itermdiateRoom[2])
itermdiateRoom[2].setEast(itermdiateRoom[1])

itermdiateRoom[2].setWest(itermdiateRoom[3])
itermdiateRoom[3].setEast(itermdiateRoom[2])

itermdiateRoom[3].setNorth(itermdiateRoom[4])
itermdiateRoom[4].setSouth(itermdiateRoom[3])

itermdiateRoom[4].setEast(itermdiateRoom[5])
itermdiateRoom[5].setWest(itermdiateRoom[4])
INTERMEDIATE_MAZE = Maze(itermdiateRoom[0], itermdiateRoom[5])

if __name__=="__main__":
	
	play(INTERMEDIATE_MAZE)
