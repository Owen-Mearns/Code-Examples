#Purpose: To make a program in pygames to show snow
#Author: Owen Mearns
#Date: 7/24/2022

#imports
import pygame
import abc
import random

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y
		
	def getLoc(self):
		return (self.__x, self.__y)
		
	def setLoc(self,p):
		self.__x = p[0]
		self.__y = p[1]
	
	
	@abc.abstractmethod
	def draw(self,surface):
		pass
#Draw a rectangle
class Rect(Drawable):
	def __init__(self, x, y, width, height, color):
		super().__init__(x, y)
		self.__width = width
		self.__height = height
		self.__color = color
	
	def draw(self, surface):
		white = (255, 255, 255)
		x_coor, y_coor = self.getLoc()
		pygame.draw.rect(surface, self.__color, (x_coor, y_coor, self.__width, self.__height))

#Draw the snowflakes
class Snowflake(Drawable):
	def __init__(self):
		super().__init__()
		self.__maxy = random.randint(height // 2, height)

	def getMax(self):
		return self.__maxy

	def setMax(self):
		y = random.randint(height // 2, height)
		self.__maxy = y
	
	def draw(self, surface):
		white = (255, 255, 255)
		x,y = self.getLoc()
		pygame.draw.line(surface, white, (x - 5, y), (x + 5, y))
		pygame.draw.line(surface, white, (x, y - 5), (x, y + 5))
		pygame.draw.line(surface, white, (x - 5, y - 5), (x + 5, y + 5))
		pygame.draw.line(surface, white, (x - 5, y + 5), (x + 5, y - 5))
	
	#Where code runs
if __name__ == '__main__':
	
	white = (255, 255, 255)
	blue = (0, 0, 255)
	green = (0, 255, 0)

	#Start pygame
	pygame.init()
	width = 400
	height = 400
	displaySurface = pygame.display.set_mode((width, height))
	displaySurface.fill(white)
	pygame.display.set_caption("Snowflake")

	#Make the sky and ground
	sky = Rect(0, 0, width, height // 2, blue)
	ground = Rect(0, height // 2, width, height // 2, green)
	snow = Snowflake()

	drawableObjects = []
	drawableObjects.append(sky)
	drawableObjects.append(ground)
	drawableObjects.append(snow)

	runStop = 1

	fpsClock = pygame.time.Clock()

	#make it so you can pause or exit the game
	while True:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
				pygame.quit()

			elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
				if runStop == 1:
					runStop = 0

				else:
					runStop = 1

		if runStop == 1:
			for drawable in drawableObjects:
				drawable.draw(displaySurface)

				if isinstance(drawable, Snowflake):
					x, y = drawable.getLoc()

					if y >= drawable.getMax():
						pass

					else:
						drawable.setLoc((x, y + 10))

					drawable.draw(displaySurface)
			
			snow = Snowflake()
			x = random.randint(0, width)
			snow.setLoc((x, 0))
			drawableObjects.append(snow)

			fpsClock.tick(10)
			pygame.display.update()



