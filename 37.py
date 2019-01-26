from little_help import isPrime
from little_help import erasthotenesSieve

    
def main():
    sum = 0
    
    sieve = set(erasthotenesSieve(10**6))
    
    i = 11
    while sum != 11:
        i += 2
        strI = str(i)
        nextPlease = False
                
        turn = i
        turn2 = i
        while turn > 0:
            if turn < 10**8 and turn2 < 10**6:            
                if turn not in sieve or turn2 not in sieve:
                    nextPlease = True
                    break
            else:
                if not isPrime(turn) or not isPrime(turn2): # Tooks ages!
                    nextPlease = True
                    break
                
            turn /= 10
            if len(str(turn2)) > 1:
                turn2 = int(str(turn2)[1:], 10)
                
         
        if nextPlease:
            continue
        
        sum += i
        print sum

    print "sum", sum

if __name__ == "__main__":
    main()