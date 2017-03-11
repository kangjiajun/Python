import os
from ImageContainer import *
from Game.PathMgr import *


class ImageLoader:
    def __init__(self):
        pass

    def load(self, imageDir, imageContainer):
        if not isinstance(imageContainer, ImageContainer):
            raise TypeError("Parameter two should be of type : ImageContainer")
        nodes = os.listdir(imageDir)
        for i in nodes:
            imagePath = os.path.join(imageDir, i)
            if os.path.isfile(imagePath):
                self.__loadImage(imageContainer, imagePath)

    def __loadImage(self, imageContainer, imagePath):
        image = pygame.image.load_basic(imagePath).convert()
        imageName = PathMgr().getImageName(imagePath)
        if imageContainer.exist(imageName):
            raise Exception("cannot add image with key : " + imageName)
        imageContainer.add(imageName, image)


