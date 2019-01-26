from little_help import generatePrimitiveTriplet

def main():
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
                
                while (ka + kb + kc <= 1000):
                    # non primitive triplets
                    
                    if (ka + kb + kc == 1000):
                        print "m ", m, "n ", n ," a ", ka, " b ", kb , " c ", kc, " sum ", ka+kb+kc, " prod ", ka * kb * kc
                        
                    k += 1
                    ka = k * a
                    kb = k * b
                    kc = k * c
                

    

if __name__ == "__main__":
    main()