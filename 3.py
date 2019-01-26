
def main():
    number = 600851475143

    factor = 2
    
    while (number != 1):
        while (number % factor == 0):
            print factor
            number /= factor
            
        factor += 1


if __name__ == "__main__":
    main()