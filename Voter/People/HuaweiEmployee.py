from Employee import *


class HuaweiEmployee(Employee):
    def __init__(self, name="", jobId=""):
        self.__name = name
        self.__jobId = jobId
        self.__company = "Huawei"

    def jobId(self):
        return self.__jobId

    def setJobId(self, jobId):
        self.__jobId = jobId

    def name(self):
        return self.__name

    def company(self):
        return self.__company
