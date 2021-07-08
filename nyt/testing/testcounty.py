import counties
import sys


def main(argv):
    cg = counties.countyGraph(argv)
    print(cg.getCounty())
    assert cg.getCounty() == 'Fubar'

    assert cg.opts.getDoplot() == False



if __name__ == "__main__":
    main(sys.argv[1:])    
