from drawable import Drawable
import pygame


class Ball(Drawable):
    def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__color = color
        left = x - size
        top = y - size
        self.__rect = pygame.Rect(left, top, size*2, size*2)

    def draw(self, surface):
        if self.getVisible():
            pygame.draw.circle(surface, self.__color, self.getPosition(), self.__size, 0)

    def getRect(self):
        pos = self.getPosition()
        size = self.getSize()
        left = pos[0] - size
        top = pos[1] - size
        self.__rect = pygame.Rect(left, top, size * 2, size * 2)
        return self.__rect

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color