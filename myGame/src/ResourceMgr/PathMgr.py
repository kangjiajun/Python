import os


class PathMgr:
    def getProjectDir(self):
        curPath = self.getCurDir()
        splitPos = curPath.rfind("\\")
        return curPath[0:splitPos]

    def getImageDir(self):
        return "".join([self.getProjectDir(), "\\resources\\images"])

    def getSoundDir(self):
        return "".join([self.getProjectDir(), "\\resources\\sounds"])

    def getSrcDir(self):
        return self.getCurDir()

    def getCurDir(self):
        return os.getcwd()

    def getShortFileNameFromPath(self, imagePath):
        (filePath, fileName) = os.path.split((imagePath))
        (shortName, extension) = os.path.splitext(fileName)
        return shortName
