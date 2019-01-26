from little_help import *

def main():

    sieve = erasthotenesSieve(100000)
    
    for m in xrange(3, 100000, 2):
        if m not in sieve:
            # odd and composite
            happyGoldbach = False
            
            for prime in sieve:
                if prime > m:
                    break
                
                s = 1
                while prime + 2*s*s < m:
                    s += 1
                    
                if prime + 2*s*s == m:
                    happyGoldbach = True
                    break
        
            if not happyGoldbach:
                print "Goldbach failed at ", m
                break
    
    
if __name__ == "__main__":
    main()