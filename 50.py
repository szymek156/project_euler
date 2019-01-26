from little_help import *
        
def main():
    
    sieve = erasthotenesSieve(10**6)
    maxCount = 0
    
    print "sieve len ", len(sieve)
    
    for i in xrange(len(sieve) - 1, 0, -1):
        upto = sieve[i]
        
        for j in xrange(0, i):
            sum = 0
            count = 0
            for k in xrange(j, i):
                sum += sieve[k]
                count += 1
                
                if sum >= upto:
                    break
                    
            if sum == upto:                
                if count > maxCount :
                    print upto, " in ", count, " terms"
                    maxCount = count
                
                break
            
    
    
    
if __name__ == "__main__":
    main()