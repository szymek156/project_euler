from little_help import *
import math
maxN = 0

def checkPoly(a, b):
    global maxN
    
    n = 0
    pn = n*n + a*n + b
    
    while (isPrime(abs(pn))):
        n += 1
        pn = n*n + a*n + b

    if ( a == 1 and b == 41):
        print n, " consective primes, with coeff ", a, " " , b
        
    if (n > maxN):
        maxN = n
        print maxN, " consective primes, with coeff ", a, " " , b
    

def main():
    # poly in form n^2 + an + b
    for a in range(-1000, 1000):
        for b in range(-1000, 1001):
            if isPrime(abs(b)):
                checkPoly(a, b)
                
            

        
if __name__ == "__main__":
    main()
