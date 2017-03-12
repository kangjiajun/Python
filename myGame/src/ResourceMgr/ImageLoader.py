from ImageContainer import *
from ResLoader import *
from ResourceMgr.PathMgr import *


class ImageLoader(ResLoader):
    imageExtension = [".png", ".jpg", ".gif", ".bmp"]

    def __init__(self):
        ResLoader.__init__(self)

    def load(self, imageDir, container):
        if not isinstance(container, ImageContainer):
            raise TypeError("ImageContainer expected")
        ResLoader._load(self, imageDir, container)

    def _ResLoader__loadOneRes(self, container, path):
        image = pygame.image.load(path).convert()
        imageName = PathMgr().getShortFileNameFromPath(path)
        if container.exist(imageName):
            raise Exception("cannot load image with key : " + imageName)
        container.add(imageName, image)

    def _ResLoader__isResType(self, resPath):
        (filePath, fileName) = os.path.split((resPath))
        (shortName, extension) = os.path.splitext(fileName)
        if extension in ImageLoader.imageExtension:
            return True
        else:
            return False
