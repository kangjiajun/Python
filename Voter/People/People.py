from abc import ABCMeta, abstractmethod
class People:
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        pass;

