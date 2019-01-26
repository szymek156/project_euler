from little_help import erasthotenesSieve

    

def main():
    table = erasthotenesSieve(2 * 1000 * 1000)
    
    sum = 0
    for prime in table:
        sum += prime
        
    print sum


if __name__ == "__main__":
    main()