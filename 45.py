from little_help import *

def main():
    for m in xrange(1, 100000):
        tri = makeTriangular(m)
        
        if isPentagonal(tri) and isHexagonal(tri):
            print tri , " is uber number ", m
        
        
    
    
if __name__ == "__main__":
    main()