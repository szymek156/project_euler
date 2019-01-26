

def main():
    sieve = range(2, 21)
    
    for i in range(0, len(sieve)):
        factor = sieve[i]
        
        for j in range(i + 1, len(sieve)):
            if (sieve[j] % factor == 0):
                sieve[j] /= factor
        
    print sieve
    
    prod = 1
    for i in sieve:
        prod *= i
        
    print prod

if __name__ == "__main__":
    main()