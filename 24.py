import itertools

def permute(elem):
    """ Generates permutations in lexicographic order, alg by Narayana Pandita. 
        Does same thing as itertools.permutations(num)"""
    perm = list(elem)
    N = len(perm)
    
    yield perm
    
    while (True):
        # Find the largest index k such that a[k] < a[k + 1]. 
        # If no such index exists, the permutation is the last permutation.
        k = N - 2
        while (k >= 0 and perm[k] > perm[k+1]):
            k -= 1
        
        if (k == -1):
            return

        # Find the largest index l greater than k such that a[k] < a[l].
        l = k + 1
        while (l < N and perm[k] < perm[l]):
            l += 1    
        l -= 1
    
        # Swap the value of a[k] with that of a[l].    
        temp    = perm[k]
        perm[k] = perm[l]
        perm[l] = temp
    
        # Reverse the sequence from a[k + 1] up to and including 
        # the final element a[n].            
        i = k + 1
        j = N - 1
        while (i < j):
            temp    = perm[i]
            perm[i] = perm[j]
            perm[j] = temp
            i += 1
            j -= 1
            
        
        yield perm
    
def main():
    num = range(0, 200)

    # its too easy with python...    
    # for perm in itertools.permutations(num):
        # print perm
            
    print "====================================="

    
    print  getPerm(num, 10**10)
    

    
    id = 1
    #for perm in itertools.permutations(num):
    for perm in permute(num):
        if (id == 10**10):
            print perm
            break
        id += 1
    
if __name__ == "__main__":
    main()
