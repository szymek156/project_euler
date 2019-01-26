from little_help import *
import time

# most naive version
def main():
    
    number = 1;
    while True:
        numberx1 = sorted(str(number))
        numberx2 = sorted(str(number * 2))
        numberx3 = sorted(str(number * 3))
        numberx4 = sorted(str(number * 4))
        numberx5 = sorted(str(number * 5))
        numberx6 = sorted(str(number * 6))
        
        
        
        if (cmp(numberx1, numberx2) == 0 and \
            cmp(numberx1, numberx3) == 0 and \
            cmp(numberx1, numberx4) == 0 and \
            cmp(numberx1, numberx5) == 0 and \
            cmp(numberx1, numberx6) == 0):
            
            print number
            break
            
        number += 1
    
if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    
    print "exec time ", stop - start