import pygame
from PathMgr import *
from ImageMgr.ImageLoader import *


class GameLoader:
    def __init__(self):
        self.__setDisplayMode(pygame.FULLSCREEN)
        self.__imageContainer = ImageContainer()
        self.__loadImages()

    def images(self):
        return self.__imageContainer

    def __setDisplayMode(self, mode, resolution = (0,0), depth = 0):
        pygame.display.set_mode(resolution, mode, depth)

    def __loadImages(self):
        path = PathMgr().getImagePath()
        imageLoader = ImageLoader()
        imageLoader.load(path, self.__imageContainer)


