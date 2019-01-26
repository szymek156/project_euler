import time
from little_help import *

def d(divisors):
    divisors.sort()
    divisors.pop()
    
    return reduce(lambda x, y: x+y, divisors)
    
def main():
    
    evaluated = [0] * 10002
    
    start = time.time()
    for number in range(2, 10000 + 1):
        #sum = d(getDivisors(number))
        sum = getDivisorsSum(number) - number
        
        evaluated[number] = sum
        
    
    sum = 0
    #amicable = 0
    for number in range(len(evaluated)):
        amicable = evaluated[number]
        
        if (amicable != number and amicable < len(evaluated) and evaluated[amicable] == number):
            sum += number
  
    end = time.time()
    print "getDivisors execution ", end - start        
    
    print sum

    
if __name__ == "__main__":
    main()
