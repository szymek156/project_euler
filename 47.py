from little_help import *

def main():

    sieve = erasthotenesSieve(100000)
    
    counter = 0
    
    for m in xrange(3, 10000000):
        factors = factorize(m)
        
        if len(factors) == 4:
            counter += 1
        else:
            counter = 0
            
        if counter == 4:
            print "Answer ", m - 3
            break
    
    
if __name__ == "__main__":
    main()