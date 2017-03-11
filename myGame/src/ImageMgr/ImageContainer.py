import pygame


class ImageContainer:
    def __init__(self):
        self.__images = {}

    def getImage(self, name):
        return self.__images[name]

    def add(self, name, surface):
        if not isinstance(surface, pygame.Surface):
            raise TypeError("ImageContainer only accepts type : pygame.Surface")

        if self.exist(name):
            raise Exception("cannot add image with key : " + name)

        self.__images[name] = surface

    def exist(self, imageName):
        if self.__images.has_key(imageName):
            return True
        else:
            return False
