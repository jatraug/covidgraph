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
        if self.is_weekend():
            self.doOrDontRemove = self.remove_is_weekend
        else:
            self.doOrDontRemove = self.remove_not_weekend

    def is_weekend(self):
        return tt.is_weekend()

    def remove_not_weekend(self, pathname):
        for f in os.listdir(pathname):
            self.removeFiles.append(f)
        self.prepareAllFileRemoval()

    def doOrDontRemove(self,  pathname):
        pass
    
    def remove_is_weekend(self,  pathname):

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
        with  open("nativeRemove.txt", "w") as fs:
            fs.write("import os\n")
            for file in self.removeFiles:
                pfile = os.path.join(facts.IMAGES, file)
                fs.write(f"os.remove({pfile})\n")
        fs.close()

    def  writeDropboxRemoveFiles(self):
        with  open("dboxRemove.txt", "w") as fs:
            fs.write("import os\n")
            for file in self.removeFiles:
                pfile = os.path.join(facts.DBIMG, file)
                fs.write(f"os.remove({pfile})\n")
        fs.close()


        

    def writeBitnamiRemoveFiles(self):
        with  open("web/bitnamiRemove.txt", "w") as fs:
            fs.write("import os\n")            
            for file in self.removeFiles:
                #qpfile = os.path.join(facts.AWSIMG, file)
                fs.write(f"os.remove({file})\n")
        fs.close()

    
    def prepareAllFileRemoval(self):
        self.writeDropboxRemoveFiles()
        self.writeNativeRemoveFiles()
        self.writeBitnamiRemoveFiles()
    def runner(self):
        self.doOrDontRemove(facts.IMAGES)

def main():
    rf = RemoveFiles(facts.lazyStates)
    rf.runner()
##    rf.doOrDontRemove(facts.IMAGES)
    
if __name__ == "__main__":
    main()
