# -*- coding: utf-8 -*-
import fractions
import math
from collections import namedtuple
from decimal import Decimal
import itertools

def generatePrimitiveTriplet(m, n):
    """ Generates all primitive Pythagorean triplet, m > n > 0.
        Non-primitive are computed as follows: k*a, k*b, k*c 
        for some k > 0 """
    
    if (m <= n):
        raise ValueError("generatePrimitiveTriplet: m=" + str(m) +\
        " has to be greater than n=" + str(n))
    
    if (fractions.gcd(m, n) == 1, ((m + n) % 2 == 1)):
        # m, n are coprime, sum is odd, so 
        # produced triplet will be primitive
        
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        
        if (a < b):
            return [a, b, c]
        else:
            return [b, a, c]
    else:
        return [0, 0, 0]
 
def multOrder(n, a = 10):
    """ Mult order of a: smallest e, for which a^e = 1 (mod n)
        Mult order of 10 mod n, for n co-prime with 10 retrurns 
        length of period of recurring decimal expansion, for ex.
        
        10^6 = 1 (mod 7), e = 6, therefore:
        1/7 = 0.(142857), length of cycle is 6 """
        
    b = 1
    
    
    while b < n and modularPow(a, b, n) != 1:
    # while b < n and ((a**b) % n) != 1:
        b += 1
        
    if b < n:
        return b
    else:
        return 0

def modularPow(a, e, n):
    """ Fast exponentiation algorithm result = a^e mod n"""
    
    result = 1
    
    eBits = str(bin(e))[2:]
    eBits = eBits[::-1]
    
    for bit in eBits:
        if bit == "1":
            result = (a * result) % n
         
        a = (a*a) % n
    
    return result
    
        
def isPrime(number):
    """ Rabin Miller test, for small numbers is deterministic
        e.x. if n < 10**6 < 1,373,653, it is enough to test 
        a = 2 and 3 """
    
    # Test works for n > 3, and n has to be odd
    if (number in [0, 1]):
        return False
    if (number in [2, 3]):
        return True
    if (number % 2 == 0):
        return False
        
    aList = []
    
    if (number < 2047): 
        aList = [2]
    elif (number < 1373653):
        aList = [2, 3]
    elif (number < 9080191):
        aList = [31, 73]
    elif (number < 25326001):
        aList = [2, 3, 5]
    elif (number < 3215031751):
        aList = [2, 3, 5, 7]
    elif (number < 4759123141):
        aList = [2, 7, 61]
    elif (number < 1122004669633):
        aList = [2, 13, 23, 1662803]
    elif (number < 2152302898747):
        aList = [2, 3, 5, 7, 11]
    elif (number < 3474749660383):
        aList = [2, 3, 5, 7, 11, 13]
    elif (number < 341550071728321):
        aList = [2, 3, 5, 7, 11, 13, 17]
    elif (number < 3825123056546413051):
        aList = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif (number < 318665857834031151167461):
        aList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif (number < 3317044064679887385961981):
        aList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    else:
        raise ValueError("isPrime: Number to test " + str(number) + " is too big!")

    
    n1 = number - 1
    
    rest = n1
    s = 0
    
    while (rest % 2 == 0):
        s += 1
        rest /= 2
        
    d = rest
    
    for a in aList:
        #if (((a**d) % number) != 1):
        #if (modularPow(a, d, number) != 1):        
        if (pow(a, d, number) != 1):        
            liar = 0
            for r in range(0, s):
                #if (((a ** ((2**r) * d)) % number) != n1):
                #if (modularPow(a, ((2**r) * d), number) != n1):
                if (pow(a, ((2**r) * d), number) != n1):
                    liar += 1
                    
            if (liar == s):    
                return False
                
    return True
    

def getNextIdx(table, old):
    idx = old + 1
    while (idx < len(table) and table[idx] == 0):
        idx += 1
        
    return idx

def erasthotenesSieve(maxSize):
    """ Proposition of implementation optimizations can be found in
        overview of problem #10 """
        
    table = range(0, maxSize + 3)
    
    finished = False
    
    idx = 2
    while (idx < math.sqrt(len(table))):            
        number = table[idx]
        
        crossOut = number + number
        while (crossOut < len(table)):
            table[crossOut] = 0
            crossOut += number
            
        idx = getNextIdx(table, idx)
    
    return filter(lambda a: a != 0 and a != 1, table) 
    
def factorize(number, primes = None):
    """ Return list of prime factors in form of a pair (prime, exponent)
        e.x. factorize(1024) -> [(2, 10)] """

    factors = []
    
    if (primes == None):
        # Do dummy way
        divisor = 2
        
        while number > 1:
            exponent = 0
            while (number % divisor == 0):
                exponent += 1
                number /= divisor
                
            if (exponent > 0):
                factors.append((divisor, exponent))
                
            divisor += 1
    else:
        # Shit is way slower on pypy, than without primes.
        
        # However it returns expected boost on standard interpreter:
        # No primes   
        # $ python 21.py
        # factorize execution  159.044999838

        # With primes (primes generation not count to execution)
        # $ python 21.py
        # factorize execution  147.174000025
        
        for prime in primes:
            exponent = 0
            while (number % prime == 0):
                exponent += 1
                number /= prime
                
            if (exponent > 0):
                factors.append((prime, exponent))

    if (len(factors) == 0):
        # Number itself is a prime
        factors.append((number, 1))
        
    return factors

def getDivisorsCount(number, primeFactors = None):
    """ Implementation of tau funcion, returns a # of divisors,
        e.x. getDivisorsCount(28) -> 6, because 28 is divisible
        by [1, 2, 4, 7, 14, 28] """
        
    if (primeFactors == None):
        primeFactors = factorize(number)
    
    divisorCount = 1
    
    for (prime, exponent) in primeFactors:
        divisorCount *= (exponent + 1)
        
    return divisorCount
    
def getDivisorsSum(n, primeFactors = None):
    """ Returns sum of all divisors (including n)
        uses formula: prod_k (p_k**(a_k+1) - 1)/ (p_k - 1)
        where p_k is prime from factorization, and a_k is its exponent.
        
        i.e. getDivisorsSum(100) = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 + 100 = 217
     """
     
    if (primeFactors == None):
        primeFactors = factorize(n)
        
    return reduce(lambda acc, (p, a) :  acc * ((p**(a+1) - 1) / (p-1)), primeFactors, 1)
    
def getDivisors(n, primeFactors = None):
    """ Make a cartesian product of all prime factors, i.e.
        100 = 2**2 * 5**2
        
        So all divisors of 100 are:
              2**0  2**1   2**2
        5**0    1     2     4
        5**1    5     10    20
        5**2    25    50    100
        
        returns all divisors, including n itself, and not in any order!
    """
    
    if (primeFactors == None):
        primeFactors = factorize(n)
    
    allFactors = []
    
    for (prime, exponent) in primeFactors:
        primeMult = []
        
        e = 0
        while (e <= exponent):
            primeMult.append(prime ** e)
            e+=1
            
        allFactors.append(primeMult)
    
    # itertools.product(*iterables) <- expects arbitraty number of iterables to 
    # make product of them. Star -> *allFactors, unpacks list of allFactors, to arguments
    # i.e. allFactors = [[1, 2, 4], [1, 5, 25]], 
    # *allFactors -> iterable1 = [1, 2, 4], iterable2 = [2, 5, 25]
    
    # product() returns generator of tuples: (1, 1), (1, 2), (1, 5), (2, 1), (2, 2)...:
    productGenerator = itertools.product(*allFactors)
    
    # Multiply all tuples to get divisors!
    return map(lambda tuple: reduce(lambda x, y: x*y, tuple), productGenerator)
                
def collatzSequence(n):
    """ Returns list of visited nodes for sequence:
        n -> n/2    if n even
        n -> 3n + 1 if n odd """
        
    travel = []
    
    while (n > 1):
        travel.append(n)
        
        if (n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1

    travel.append(1)
    
    return travel

def collatzSequenceCount(n, previousResults = None):
    """ Returns # of visited nodes for sequence:
        n -> n/2    if n even
        n -> 3n + 1 if n odd 
        
        Can work faster if in previousResults list there are
        seqences for all m < n"""
            
    visitedNodes = 1
    start = n
    
    while (n > 1):
        if (n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        
        if (previousResults != None and n < start):
            prevTravel = previousResults[n]
            visitedNodes += prevTravel
            break
            
        visitedNodes += 1
            
    if (previousResults != None):
        previousResults.append(visitedNodes)
    
    return visitedNodes

Neighbour = namedtuple("Neighbour", ["idx", "weight"])

def shortestPath(graph, source, target = None):
    """ Dijkstra, 
        graph - adjacent list, where graph[nodeIdx] -> [(neighborIdx1, weight), (neighborIdx2, weight)...]
        source - node to start
        
        returns list of prevs, from which, path from arbitrary node can be reconstructed (if target is None). 
        For example:
        
        path = []
        # Reconstruct path from last node
        prev = len(graph) - 1
        while (prev != source):
            path.append(prev)
            prev = prevs[prev]
        
        path.append(prev)
        path.reverse()
        print "Path ", path
        
        
        Can be further improved by adding prio queue"""
    
    dist = []
    prev = []
    Q    = []
    
    for vertexIdx in range(len(graph)):
        dist.append(Decimal("Infinity"))
        prev.append(None)
        Q.append(vertexIdx)
    
    dist[source] = 0
    
    # While there are verticies in Q
    while Q:
        # u <- vertex in Q with min dist[u]
        u = Q[0]
        for q in Q:
            if (dist[q] < dist[u]):
                u = q
        
        if (target != None and target == u):
            return prev
            
        # remove u from Q 
        Q.remove(u)
        
        #  for each neighbor v of u:           // where v is still in Q.
        neighbors = graph[u]
        for v in neighbors:
            if v.idx in Q:
                alt = dist[u] + v.weight
                
                if (alt < dist[v.idx]):
                    dist[v.idx] = alt
                    prev[v.idx] = u
                    
                    
    #print "Dist ", dist
    #print "Prev ", prev
    
    return prev


def getFactorialRepresentation(number):
    """ Returns factoradic representation of a decimal number.
        i.e. 1000000 = 2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 2*2! + 0*1! + 0*0! =
             2662512200
             
        Convert a number into factorial representation producing digits from right to left, by
        repeatedly dividing the number by the place values (1, 2, 3, ...), taking the
        remainder as digits, and continuing with the integer quotient, until this quotient
        becomes 0.
    """
    
    division = 1
    factoradic = []
    
    while number != 0:
        rest = number % division
        factoradic.append(rest)
        
        number /= division
        division += 1
    
    factoradic.reverse()
    
    return factoradic
    
def getPerm(elements, id):
    """ Gets id-th (counting from 1) permutation from lexicographic order of elements 
        For example 1000000th lex permutation of numbers 0-9 is 2783915460 
        
        getPerm(range(0,10), 1000000) -> 2783915460
    """
    # Alg counts starting from 0 
    if (id > 0):
        id -= 1
    
    # Make a copy, because alg. modifyies this list
    elements = list(elements)
    
    # By converting a number less than n! to factorial representation, one obtains a sequence
    # of n digits that can be converted to a permutation of n in a straightforward way, either
    # using them as Lehmer code or as inversion table representation;
    
    # There is a natural mapping between the integers 0, ..., n! − 1 (or equivalently the
    # numbers with n digits in factorial representation) and permutations of n elements in
    # lexicographical order, when the integers are expressed in factoradic form. This mapping
    # has been termed the Lehmer code (or inversion table).
    
    factoradic = getFactorialRepresentation(id)
    
    # Fill up with zeros if factoradic representation is shorter than set of numbers to permute
    zeros = [0] * (len(elements) - len(factoradic))
    factoradic = zeros + factoradic
    
    permutation = []
    for digit in factoradic:
        permutation.append(elements[digit])
        del elements[digit]
        
    return permutation

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
        
def countCombinationsWithReplacement(n, k):
    """ How many are there combinations with replacement of k elements fron n el set? """
    res = math.factorial(k+n-1) / (math.factorial(k) * math.factorial(n-1))
    return res
    
    
def countCombinations(n, k):
    """In mathematics, a combination is a selection of items from a collection, such that (unlike permutations) the order of selection does not matter. 
    
    For example, given three fruits, say an apple, an orange and a pear, there are three combinations of two that can be drawn from this set: an apple and a pear; an apple and an orange; or a pear and an orange. 
    
    More formally, a k-combination of a set S is a subset of k distinct elements of S. If the set has n elements, the number of k-combinations is equal to the binomial coefficient."""
    
    assert k <= n, "k parameter must be <= n !!!"
    
    res = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    
    return res
    
    
def getFibGen():
    """ Generates Fibonacci seq in from (id, value) """
    
    a = 0
    b = 1

    id = 0
    while True:
        sum = a + b
        a = b
        b = sum
        id += 1
        
        yield (id, sum)

def isTriangular(x):
    nominator = (math.sqrt(8 * x + 1) - 1)
    
    n = 0
    if nominator % 2 == 0:
        n = nominator / 2
        
    return n
    
def isPentagonal(x):
    nominator = (math.sqrt(24 * x + 1) + 1)
    
    n = 0
    if nominator % 6 == 0:
        n = nominator / 6
        
    return n

def isHexagonal(x):
    nominator = (math.sqrt(8 * x + 1) + 1)
    
    n = 0
    if nominator % 4 == 0:
        n = nominator / 4
        
    return n

    
def makeTriangular(n):
    return (n*n + n)/2
    
def makePentagonal(n):
    return (3*n*n - n)/2     

def makeHexagonal(n):
    return 2*n*n - n    

    