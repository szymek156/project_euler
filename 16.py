import math

def main():
    lenistwo = str(2**1000)
    
    lenistwo = str(math.factorial(100))
    
    sum = 0
    for i in lenistwo:
        sum += int(i)
        
    print sum

if __name__ == "__main__":
    main()