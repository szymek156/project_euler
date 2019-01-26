from little_help import *

def main():
    
    sum = 0
    
    # last 10 digits -> mod 10000000000
    for m in xrange(1, 1001):
        sum = (sum + pow(m, m, 10000000000)) % 10000000000
        
        
    print sum
    
if __name__ == "__main__":
    main()