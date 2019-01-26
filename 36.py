
def isDecimalPalindrome(binPalindrome):
    candidateDecimal = int(binPalindrome, 2)
    
    if candidateDecimal >= 1000000:
        return False
    
    candidateDecimalString = "" + str(candidateDecimal)
    
    # It may be more efficient to check by %10 /10, but come on, waste of time to write this...
    return candidateDecimalString == candidateDecimalString[::-1] 

def getPalindrome():
    counter = 1
    
    # There should be better bound: 2**9 and then take care of the rest:
    # 2**9...1000000, but I am too lazy
    while counter < 2**10:
        bin = format(counter, 'b');
        
        # first candidate '1101' + '1011' = 11011011
        candidate1 = bin + bin[::-1]        
        #print "candidate1 ", candidate1
        
        if isDecimalPalindrome(candidate1):
            yield int(candidate1, 2)
        
        # second: '110' + '1011' = 1101011
        candidate2 =  bin[0:len(bin)-1] + bin[::-1]        
        #print "candidate2 ", candidate2
        
        if isDecimalPalindrome(candidate2):
            yield int(candidate2, 2)
        
            
        counter += 1

def naiveVersion():
    for i in range (1, 1000000):
        if (str(i) == str(i)[::-1]):
    
            iBin = format(i, 'b')            
            if iBin == iBin[::-1]:
                yield i
            
            
            

def main():
    gen = getPalindrome()
    
    acc = 0
    for i in gen:
        print "palindrome ", i, " ", format(i, 'b')
        acc += i
    
    print "acc ", acc

if __name__ == "__main__":
    main()