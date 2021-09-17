"""
Some states don't publish data on weekends. For these states don't
make graphs on weekends.

"""
import timetools as tt #Uncover weekends
import os
import sys
import facts





##  os.remove("file.jpg")

class RemoveFiles:
    def __init__(self, lazyStates):
        self.removeFiles = []
        self.empty = []
        self.lazyStates = lazyStates

    def doOrDontRemove(self,  pathname):

        for f in os.listdir(pathname):
            keepfile = False
            fname = os.path.join(pathname, f)
                
            for s in self.lazyStates:
                if s in f:
                    keepfile = True
                    break        
            if keepfile == True:
                pass
                #print(f"keep {f}")
            else:
                # print(f"remove {f}")
                self.removeFiles.append(f)
        self.prepareAllFileRemoval()

    def writeNativeRemoveFiles(self):
        with  open("NativeRemove.txt", "w") as fs:
            for file in self.removeFiles:
                pfile = os.path.join(facts.IMAGES, file)
                fs.write(f"os.remove({pfile})\n")
        fs.close()

    def  writeDropboxRemoveFiles(self):
        pass

    def writeBitnamiRemoveFiles(self):
        pass
    
    def prepareAllFileRemoval(self):
        self.writeDropboxRemoveFiles()
        self.writeNativeRemoveFiles()
        self.writeBitnamiRemoveFiles()


def main():
    rf = RemoveFiles(facts.lazyStates)
    rf.doOrDontRemove(facts.DBIMG)
    
if __name__ == "__main__":
    main()
