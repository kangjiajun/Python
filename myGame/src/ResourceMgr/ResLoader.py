import os
from ResContainer import *


class ResLoader:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def _load(self, resDir, resContainer):
        if not isinstance(resContainer, ResContainer):
            raise TypeError("Parameter two should be of type : ResContainer")
        nodes = os.listdir(resDir)
        for i in nodes:
            resPath = os.path.join(resDir, i)
            if os.path.isfile(resPath) and self.__isResType(resPath):
                self.__loadOneRes(resContainer, resPath)

    @abstractmethod
    def __loadOneRes(self, resContainer, resPath):
        pass

    @abstractmethod
    def __isResType(self, resPath):
        pass
