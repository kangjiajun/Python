from ImageContainer import *


class ImageLoader:
    def __init__(self):
        pass

    def load(self, dirPath, imageContainer):
        if not isinstance(imageContainer, ImageContainer):
            raise TypeError("Parameter two should be of type : ImageContainer")
