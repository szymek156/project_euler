from little_help import isPrime
    
def main():
    # Number of primes below 10**5 is 9592, so lets start to search from there
    number = 10**5 + 1
    primeIdx = 9592
    
    while (primeIdx != 10001):
        if (isPrime(number)):
            primeIdx += 1
            print "Found ", primeIdx, "th prime ", number

        # Omit even numbers
        number += 2
        
    # for i in range(3, 201, 2):
        # if (isPrime(i)):
            # print i
    
    

if __name__ == "__main__":
    main()