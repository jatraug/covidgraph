from options import Options
import sys
import os

###Test
def main(argv, exename):
    opts = Options(argv, exename)
    state = opts.getState()
    plot = opts.getDoplot()
    

    print('State: ', state)
    print('Plot: ', plot)
    
    
if __name__ == "__main__":
    main(sys.argv[1:], os.path.basename(__file__))


