from little_help import *

def main():

    foundSum = 0
    
    for i in range(2, 100000000):
        j = i
        digits = []
        while j != 0:
            digits.append(j % 10)
            j /= 10
            
        sum = reduce(lambda x, y: x+y, map(lambda x: x**4, digits))
        #print digits, " sum ", sum
        
        if sum == i:
            print i
            foundSum += sum
            
    print foundSum
            
 # (Python)
 # from itertools import combinations_with_replacement
 # A252648_list = [1]
 # for m in range(1,21):
     # l, L, dm, xlist, q = 1, 1, [d**m for d in range(10)], [0], 9**m
     # while l*q >= L:
         # for c in combinations_with_replacement(range(1,10),l):
             # n = sum(dm[d] for d in c)
             # if sorted(int(d) for d in str(n)) == [0]*(len(str(n))-len(c))+list(c):
                 # xlist.append(n)
         # l += 1
         # L *= 10
     # A252648_list.extend(sorted(xlist)) # _Chai Wah Wu_, Jan 04 2016
            
if __name__ == "__main__":
    main()