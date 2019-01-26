def main():
    s = set()
    
    for i in range(1, 100):        
        for j in range(i, 9999):
            prod = j*i
            
            eqStr = str(j) + str(i) + str(prod)
            
            if len(eqStr) == 9 and (not "0" in eqStr):
                digits = set()
                for d in eqStr:
                    digits.add(d)
                
                if len(digits) == 9:
                    s.add(prod)
                    print i, "*", j, "=", prod
    
    sum = 0
    for el in s:
        sum += el
        
        
    print sum


if __name__ == "__main__":
    main()