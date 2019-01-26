from little_help import *
import time

# most naive version
def main():
    
    count = 0
    for n in range(1, 101):
        for k in range(1, n):
            comb = countCombinations(n, k)
            
            if (comb > 1000000):
                print "n ", n, " k ", k, " n choose k ", comb
                count += 1
                
    print "count ", count
                
    
if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    
    print "exec time ", stop - start