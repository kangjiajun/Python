from abc import ABCMeta, abstractmethod
from People import *
class Employee(People):
    __metaclass__ = ABCMeta
    @abstractmethod
    def jobId(self):
        pass

    @abstractmethod
    def setJobId(self):
        pass

    @abstractmethod
    def company(self):
        pass
