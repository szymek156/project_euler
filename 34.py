import math
import itertools
    
def main():
    memo = [math.factorial(i) for i in range(0,10)]
    digits = range(0, 10)
    
    cnt = 0
    
    # Upper bound, 9! returns 6 digit number, so biggest 6 digit number is 999999 ->
    # which implies 6*9! which results 7 digit number, so it cannot be written as
    # sum of own digits because is one too many
    for i in range(2, 7):
        comb = itertools.combinations_with_replacement(digits, i)
        
        for c in comb:
            cnt += 1
            # DOESNT WORK sum = reduce(lambda a, b: a+memo[b], c, memo[c[0]])
            sum = 0
            for el in c:
                sum += memo[el]
        
            nope = False
            strSum = str(sum)
                
            if len(strSum) == len(c):
                for el in c:
                    if not str(el) in strSum:
                        nope = True
                        break
                    strSum = strSum.replace(str(el), "", 1)
                
                    
                if not nope:
                    print sum, " = ", c
        
    print cnt

if __name__ == "__main__":
    main()