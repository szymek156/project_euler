import time

from little_help import collatzSequenceCount

def main():
    maxSeq = 0
    maxN = 0
    
    knownSoFar = [1]
    
    n = 1
    while (n < 10**6):
        seq = collatzSequenceCount(n, knownSoFar)
       
        if (seq > maxSeq):
            maxN = n
            maxSeq = seq
            
        n += 1
        
    print "N = ", maxN, "Max seq len = ", maxSeq

if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    
    print "Exec time ", stop - start
    
    
    
    
# Naiive version collatzSequence, compare sequence lengths:
# $ python 14.py
# Max seq len =  525
# Exec time  28.4279999733

# $ pypy 14.py
# Max seq len =  525
# Exec time  1.03799986839

# collatzSequenceCount, do only visited nodes count
# $ pypy 14.py
# Max seq len =  525
# Exec time  0.600999832153

# dynamic programming, if used dictionary
# $ pypy 14.py
# Max seq len =  525
# Exec time  0.430999994278

# dynamic programming, if used list
# $ pypy 14.py
# Max seq len =  525
# Exec time  0.0969998836517

# $ python 14.py
# Max seq len =  525
# Exec time  1.51999998093


