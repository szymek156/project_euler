import math

def isPentagonal(x):
    nominator = (math.sqrt(24 * x + 1) + 1)
    
    if nominator % 6 == 0:
        #n = nominator / 6
        return True
    else:
        #n = -1
        return False
        
def makePentagonal(n):
    return (3*n*n - n)/2

# smallest, in this case simply means first one found
def main():
    for m in xrange(1, 10000):
        for n in xrange(m, 10000):
            mp = makePentagonal(m)
            np = makePentagonal(n)
            
            sum = mp + np
            diff = abs(mp - np)
            
            if isPentagonal(sum) and isPentagonal(diff):
                print  mp, ", ", np, " is uber-pentagonal pair, diff: ", diff                 
    
    
if __name__ == "__main__":
    main()