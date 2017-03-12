from ResourceMgr.ImageLoader import *


class GameLoader:
    def __init__(self):
        self.__setDisplayMode(pygame.FULLSCREEN)
        self.__imageContainer = ImageContainer()
        self.__loadImages()

    def screen(self):
        return self.__screen

    def images(self):
        return self.__imageContainer

    def __setDisplayMode(self, mode, resolution = (0,0), depth = 0):
        self.__screen = pygame.display.set_mode(resolution, mode, depth)

    def __loadImages(self):
        path = PathMgr().getImageDir()
        imageLoader = ImageLoader()
        imageLoader.load(path, self.__imageContainer)


