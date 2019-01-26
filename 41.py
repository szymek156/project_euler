from little_help import isPrime
from little_help import erasthotenesSieve

def isPalinSomething(i):
    iStr = str(i)
    
    for d in range(1, len(iStr) + 1):
        if not str(d) in iStr:
            return False
    
    return True
        
def main():
    i = 10**9 -1
    
    while i > 0:
        if isPalinSomething(i) and isPrime(i):
            print i
            break
            
            
        i -= 2
    
    
if __name__ == "__main__":
    main()