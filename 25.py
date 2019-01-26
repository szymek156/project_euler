import math

def getFib(n):
    return int(round((1/math.sqrt(5)) * ((1+math.sqrt(5))/2)**n))
    
def getFibGen():
    a = 0
    b = 1
    
    id = 1
    while True:
        sum = a + b
        a = b
        b = sum
        
        yield (id, sum)
        
        id += 1
    
    
def main():

    fibGen = getFibGen()
    i = 1
    fibLen = 0
    
    while fibLen < 1000:
        fibLen = len(str(fibGen.next()[1]))
        
        i += 1
        
    print i
    
if __name__ == "__main__":
    main()
