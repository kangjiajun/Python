import pygame
from ResContainer import *


class ImageContainer(ResContainer):
    def __init__(self):
        ResContainer.__init__(self)

    def add(self, name, resSource):
        if not isinstance(resSource, pygame.Surface):
            raise TypeError("ImageContainer only accepts type : pygame.Surface")

        if self.exist(name):
            raise Exception("Image with key : " + name + " already exist")

        self.__resources[name] = resSource
