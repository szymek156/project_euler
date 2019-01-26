from little_help import *
import time

def generateFamily(prime, i, j, k):
    primeCopy = list(prime)
    
    for num in xrange(0, 10):
        if  (i == 0 and num == 0):
            continue
           
        primeCopy[i] = str(num)            
        primeCopy[j] = str(num)
        primeCopy[k] = str(num)
        
        res = "".join(primeCopy)
        
        yield res
    
maxCount = 0
minP     = 10**8

def lookForFamily(sieve, i, j, k):
    global maxCount
    global minP
    
    crossout = set()
    
    print "i ", i, " j ", j, " k ", k
    
    for p in sieve:        
        if len(p) > k:
        
            mask = list(p)
            mask[i] = "X"
            mask[j] = "X"
            mask[k] = "X"
            
            mask = "".join(mask)
            
            if mask in crossout:
                continue
                
                
            crossout.add(mask)
            gen = generateFamily(p, i, j, k)
            
            count = 0
            for g in gen:
                if g in sieve:
                    count += 1
            
            
            if count == 8 and int(p) < minP:
                print p, " count ", count
                minP = int(p)
                return True
    
    return False

from itertools import ifilter, count, dropwhile

ALL_DIGS = '0123456789'
def not_in_family( prime, nfamily = 8):
   sp = list( str( prime)); ndig = len( sp)
   for nrepeat in xrange(1, ndig):
      # for every number of the recurring digit's repeats
      # try first family digit
      for ffd in ALL_DIGS[ :-nfamily+1]: 
         if sp[:-1].count( ffd) < nrepeat: 
            continue # if insufficient number of repeats  
         
         # find indexes in `prime' of `ffd'         
         inds = [sp.index( ffd)]
         for i in xrange( nrepeat-1):
            inds.append( sp.index( ffd, inds[i]+1))
            
         # find family
         s = sp[:]; fam = [prime]
         digs = ALL_DIGS[ ALL_DIGS.index(ffd)+1:]
         nfail, nfailmax = 0, len(digs) - nfamily + 1
         for dig in digs:
            for i in inds:
               s[i] = dig # replace corresponding digits
            p = int( ''.join( s))
            if isPrime( p): fam.append( p)
            elif nfail == nfailmax: break
            else: nfail += 1
               
         if len( fam) >= nfamily:
            for i in inds: # pretty printing stuff
               s[i] = '*'
            print ''.join(s), fam
            # `prime' begins a `nfamily' prime value family
            return False 
   # `prime' does NOT begin the family          
   return True
   
def main():
    # print dropwhile(not_in_family, ifilter(isPrime, count())).next()
    
    sieve = set(map(lambda a: str(a), erasthotenesSieve(10**6)))
    
    for i in range(0, 9):
         for j in range(i + 1, 9):
             for k in range (j + 1, 7):
                if (lookForFamily(sieve, i, j, k)):
                    return
    
    
    
    
if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    
    print "exec time ", stop - start