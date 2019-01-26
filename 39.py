from little_help import generatePrimitiveTriplet
    
def main():
    solutions = {}
    sum = 0

    a = 0
    b = 0
    c = 0
    
    for n in range(1, 1000):
        for m in range(n + 1, 1000):
            [a, b, c] = generatePrimitiveTriplet(m, n)
            
            if (a != 0):
                k = 1
                ka = a
                kb = b
                kc = c
                
                perimeter = ka + kb + kc
                
                while (perimeter <= 1000):                    
                    if perimeter not in solutions:
                        solutions[perimeter] = set()
                    
                    solutions[perimeter].add((ka, kb, kc))
        
                    if perimeter == 120:        
                        print solutions[perimeter]
                    
                    k += 1
                    ka = k * a
                    kb = k * b
                    kc = k * c
                    
                    perimeter = ka + kb + kc

    
    pMax = 0
    cMax = 0
    for p in solutions.keys():
        if len(solutions[p]) > cMax:
            cMax = len(solutions[p])
            pMax = p
    
    print "pMax ", pMax, " cMax ", cMax
    
if __name__ == "__main__":
    main()