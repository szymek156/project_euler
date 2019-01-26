from little_help import *
from itertools import permutations

def isPermutation(a, b):
    strA = list(str(a))
    strB = list(str(b))
    
    strA.sort()
    strB.sort()
    
    return strA == strB
        

def main():
    
    sieve = erasthotenesSieve(10000)
    answer = ""
    
    for i in xrange(len(sieve)):
        if sieve[i] > 1000:
            for j in xrange(i + 1, len(sieve)):            
                diff = sieve[j] - sieve[i]
                
                n = sieve[i] + diff
                
                count = 1
                while n in sieve and isPermutation(sieve[i], n):
                    count += 1
                    n += diff
                    
                if count == 3:
                    print sieve[i], sieve[i] + diff, sieve[i] + 2*diff, "diff ", diff
        
    print answer
    
if __name__ == "__main__":
    main()