from little_help import generatePrimitiveTriplet
    
def main():
    n = 1
    for i in range(1, 1000001):
    
        if n in [10, 100, 1000, 9998, 9999, 38890, 100000, 1000000]:
            print "n ", n, " i ", i
            
        offset = 1
        if i > 99999:
            offset = 6
        elif i > 9999:
            offset = 5
        elif i > 999:
            offset = 4
        elif i > 99:
            offset = 3
        elif i > 9:
            offset = 2
                
        n += offset
        
# n  188  2887  38886
# dn 99   999   9999

# for n >= 2890 n = (dn - 1000) * 4 + 2890
# dn = (n + 1110)/4

# for n >= 38890 n = (dn - 10000) * 5 + 38890
# dn = (n + 11114)/5

# in general
# n = (dn - order) * #digits per number + offset
    
if __name__ == "__main__":
    main()