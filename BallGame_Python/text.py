from drawable import Drawable
import pygame


class Text(Drawable):

    def __init__(self, x=0, y=0, message='', visibility=True):
        super().__init__(x, y, visibility)
        self.__message = message
        fontObj = pygame.font.Font("freesansbold.ttf", 32)
        self.__surface = fontObj.render(message, True, (0, 0, 0))
        size = fontObj.size(message)
        self.__rect = pygame.Rect(x, y, size[0], size[1])

    def draw(self, target_surface):
        if self.getVisible():
            target_surface.blit(self.__surface, self.getPosition())

    def getRect(self):
        return self.__rect

    def getMessage(self):
        return self.__message

    def setMessage(self, message):
        self.__message = message
        fontObj = pygame.font.Font("freesansbold.ttf", 32)
        self.__surface = fontObj.render(message, True, (0, 0, 0))