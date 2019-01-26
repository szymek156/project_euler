from little_help import isPrime
from little_help import erasthotenesSieve

def genRotations(n):
    strN = str(n)
    
    yield n
    
    for i in range(len(strN)-1):
        rot = strN[1:] + strN[0]
        strN = rot
        yield int(rot, 10)
    
def main():
    circPrimes = 4 # 2, 3, 5, 7
    sieve = set(erasthotenesSieve(10**6))
    
    for i in range(10, 10**6):
        strI = str(i)
        nextPlease = False
        
        # can be changed to get combinations with replacement for k=2,3,4,5 
        # from set {1,3,7,9}
        
        for s in strI:
            if s in ["0", "2", "4", "5", "6", "8"]:
                nextPlease = True
                break
                
        if nextPlease:
            continue
        
        genRot = genRotations(i)
        for rot in genRot:
            if rot not in sieve:
                nextPlease = True
                break
         
        if nextPlease:
            continue
            
        circPrimes += 1

    print circPrimes

if __name__ == "__main__":
    main()