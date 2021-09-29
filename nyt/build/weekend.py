"""
Some states don't publish data on weekends. For these states don't
make graphs on weekends.

"""
import timetools as tt #Uncover weekends
import os
import sys
import facts 
import activity





##  os.remove("file.jpg")

class RemoveFiles:
    def __init__(self, lazyStates):
        self.removeTheseFiles = []
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
            self.removeTheseFiles.append(f)
        self.prepareAllFileRemoval()

    def doOrDontRemove(self,  pathname):
        ''' filled in later (by init) to be one of the weekend funcs
        '''
        ## assert False
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
                self.removeTheseFiles.append(f)
        self.prepareAllFileRemoval()

    def writeNativeRemoveFiles(self):
        with  open("nativeRemove.txt", "w") as fs:
            fs.write("#### This file created my weekend.py. Do not edit!! ###\n")            
            fs.write("import os\n")
            fs.write("flist = [ ")
            for file in self.removeTheseFiles:
                pfile = os.path.join(facts.IMAGES, file)
                fs.write(f'"{pfile}",\n ')
                #fs.write(f"os.remove({pfile})\n")
            fs.write("]\n")
            fs.write("for f in flist:\n")
            fs.write(f"    try:\n")

            fs.write("        os.remove(f)\n" ) ## + "\}')\n")
            
            fs.write(f"    except FileNotFoundError as e:\n")
            fs.write("        print(e)\n")
                     
        fs.close()

    def  writeDropboxRemoveFiles(self):
        with  open("dboxRemove.txt", "w") as fs:
            fs.write("#### This file created my weekend.py. Do not edit!! ###\n")            
            fs.write("import os\n")
            fs.write("flist = [ ")
            for file in self.removeTheseFiles:
                pfile = os.path.join(facts.DBIMG, file)
                fs.write(f'"{pfile}",\n ')
                #fs.write(f"os.remove({pfile})\n")
            fs.write("]\n")
            fs.write("for f in flist:\n")
            fs.write(f"    try:\n")

            fs.write("        os.remove(f)\n" ) ## + "\}')\n")
            
            fs.write(f"    except FileNotFoundError as e:\n")
            fs.write("        print(e)\n")
                     
        fs.close()


        

    def writeBitnamiRemoveFiles(self):
        with  open("../web/bitnamiRemove.txt", "w") as fs:
            fs.write("#### This file created my weekend.py. Do not edit!! ###\n")
            fs.write("import os\n")
            for file in self.removeTheseFiles:
                #qpfile = os.path.join(facts.AWSIMG, file)
                fs.write(f"os.remove({file})\n")
        fs.close()
    def writeNativeBuildFiles():
        pass

    def writeDropboxBuildFiles():
        pass
    
    def writeBitnamiBuildFiles():
        pass
    
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
