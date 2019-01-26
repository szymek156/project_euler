import math
import time
from little_help import factorize
from little_help import erasthotenesSieve
from little_help import getDivisorsCount

def main():    
    triangle = 1
    nextNumber = 2
    divisorsCountMax = 0
    
    sieve = erasthotenesSieve(int(math.sqrt(2**32)))
    
    while (True):
        factors = factorize(triangle, sieve)
        
        divisorsCount = getDivisorsCount(triangle, factors)
        
        if (divisorsCount > 500):
            print "triangle ", triangle, "divs len ", divisorsCount
            break
        
        triangle += nextNumber
        nextNumber += 1
        
        
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    
    print "Exec time ", (end - start)