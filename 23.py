import time
from little_help import *

def main():
    abundantNumbers = []
    
    # it is known that the greatest number that cannot be expressed as 
    # the sum of two abundant numbers is less than 28123.
    for i in range(2, 28123 + 1):
        sum = getDivisorsSum(i) - i
        
        if (sum > i):
            abundantNumbers.append(i)

    # Create cartesian product of all abundant numbers, then add them, this will generate all
    # numbers which can be written as sum of 2 abundant numbers
    sumOf2AbundantNumbers = set(map(lambda (a,b): a+b, itertools.product(abundantNumbers, repeat = 2)))
    
    # Find the sum of all the positive integers which cannot be 
    # written as the sum of two abundant numbers.
    sum = 0
    for i in range(1, 28123 + 1):
        if (i not in sumOf2AbundantNumbers):
            sum += i
    
    print sum
    
if __name__ == "__main__":
    main()
