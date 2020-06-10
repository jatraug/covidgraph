import sys, getopt

def main(argv):
    doplot = True
    state = 'Washington'

    try:
        opts, args = getopt.getopt(argv,"hs:n")
    except getopt.GetoptError:
        print ('cases.py -n -s state')
        sys.exit("exiting")
    count = 0
    for opt, arg in opts:
        count +=1
        print(count, opt, arg)
        if opt == '-h':
            print ('cases.py [-n  (noplot)] [-s State]')
            sys.exit()
        elif opt in ("-n"):
            doplot = False
        elif opt in ("-s"):
            state = arg
    print(state, doplot)


if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(2)    
