from drawable import Drawable
import pygame


class Block(Drawable):
    def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__color = color
        self.__rect = pygame.Rect(x, y, size, size)

    def draw(self, surface):
        if self.getVisible():
            outline_color = (0, 0, 0)
            outline_width = 3
            
            pygame.draw.rect(surface, self.__color, self.__rect, 0)
            pygame.draw.rect(surface, outline_color, self.__rect, outline_width)

    def getRect(self):
        pos = self.getPosition()
        size = self.getSize()
        self.__rect = pygame.Rect(pos[0], pos[1], size, size)
        return self.__rect

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color