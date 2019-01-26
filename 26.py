import fractions
from little_help import multOrder
    
def main():
    maxO = 0
    for i in range(1, 1000):
        o = multOrder(i, 10 )
        if maxO < o:
            maxO = o
            print "i ", i,  " mult order ", o
        
    
if __name__ == "__main__":
    main()