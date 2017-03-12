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

    def getFileNameFromPath(self, imagePath):
        length = len(imagePath)
        begin = imagePath.rfind("\\") + 1
        return imagePath[begin:length]
