import abc

class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x=0, y=0, visibility=True):
        self.__x = x
        self.__y = y
        self.__visible = visibility

    def getPosition(self):
        return self.__x, self.__y

    def setPosition(self, position):
        self.__x = position[0]
        self.__y = position[1]

    def setVisible(self, visibility):
        self.__visible = visibility

    def getVisible(self):
        return self.__visible

    @abc.abstractmethod
    def getRect(self):
        pass

    @abc.abstractmethod
    def draw(self, surface):
        pass