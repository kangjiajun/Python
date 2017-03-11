import os

class PathMgr:

    def getProjectPath(self):
        curPath = self.getCurPath()
        splitPos = curPath.rfind("\\")
        return curPath[0:splitPos]

    def getImagePath(self):
        return "".join([self.getProjectPath(), "\\resources\\images"])

    def getSoundPath(self):
        return "".join([self.getProjectPath(), "\\resources\\sounds"])

    def getSrcPath(self):
        return self.getCurPath()

    def getCurPath(self):
        return os.getcwd()
