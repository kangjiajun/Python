from Game.PathMgr import *
from ImageContainer import *
from ResLoader import *


class ImageLoader(ResLoader):
    def __init__(self):
        ResLoader.__init__(self)

    def load(self, imageDir, container):
        if not isinstance(container, ImageContainer):
            raise TypeError("ImageContainer expected")
        ResLoader._load(self, imageDir, container)

    def __loadOneRes(self, container, path):
        image = pygame.image.load_basic(path).convert()
        imageName = PathMgr().getFileNameFromPath(path)
        if container.exist(imageName):
            raise Exception("cannot load image with key : " + imageName)
        container.add(imageName, image)

    def __isResType(self, resPath):
        # todo
        return True
