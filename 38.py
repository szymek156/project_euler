
def validate(concatenated, resStr):
    if (len(concatenated) + len(resStr) > 9):
        return False
        
    for c in concatenated:
        if (resStr.find(c) != -1):
            return False;
            
    return True;
    
def isPandigital(candidate):

    if (len(candidate) != 9):
        return False
    
    for d in "123456789":
        if (candidate.find(d) == -1):
            return False
            
    return True;

def solution():   
    integer = 987654320 / 2
    foundSoFar = 0;
    
    while integer != 0:
        i = 0
        concatenated = ""
        resStr = ""
        while len(concatenated) < 10:
            resStr = str(integer * (i + 1))
            
            if (validate(concatenated, resStr)):
                concatenated += resStr
                i+=1
            else:
                break
            
            
            
        if (i > 1 and isPandigital(concatenated)):
            pandigital = int(concatenated, 10)
            print pandigital, " int ", integer, " i ", i
        
        integer -=1

def main():
    gen = solution()
    

if __name__ == "__main__":
    main()