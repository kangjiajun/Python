from abc import ABCMeta, abstractmethod


class ResContainer:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__resources = {}

    @abstractmethod
    def add(self, name, res):
        pass

    def get(self, name):
        if self.exist(name):
            return self.__resources[name]
        else:
            return None

    def exist(self, resName):
        if resName in self.__resources.keys():
            print "True"
            return True
        else:
            return False
