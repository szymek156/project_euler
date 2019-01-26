import time

width  = 5
height = 5
count  = 0
map = ""

def go(x, y):
    global width
    global height
    global count
    global map
    
    if (x == width and y == height):
        count += 1
        print map
        
        return
    
    if (x + 1 <= width):
        map += "-"
        go(x + 1, y)
    else:
        map += "\n"
    
    # Board is a square so it's enough to count routes above diagonal, and then mult by 2
    if (x == 0):
        count *= 2
        return
        
    if (y + 1 <= height):
        
        map += " " * x + "|"
        go(x, y + 1)
    

def main():    
    #go(0, 0)
    
    global count

    #######################
    # Non recursive version
    
    depth = [0] * width
    
    last = width - 1
    countAtGivenLength = 0
    prevIdx = width
    
    while depth[0] == 0:
        
        print depth
        countAtGivenLength += 1
        count += 1
        
        depth[last] += 1
        
        if (depth[last] == width + 1):
            for idx in range(width - 1, -1, -1):
                if (depth[idx] < width):
                    depth[idx] += 1
                    
                    newValue = depth[idx]
                    for i in range(idx, width):
                        depth[i] = newValue
    
                    # if (idx < prevIdx):
                        # print "Length ", prevIdx, " count ", countAtGivenLength
                        
                        prevIdx = idx
                        countAtGivenLength = 0
                    break
    
    count *= 2
    
    print count
    
if __name__ == "__main__":
    # test = 2
    
    # while (test < 21):
        # width = test
        # height = test
        # count = 0
        
        start = time.time()
        main()
        stop = time.time()
        
        print "Grid: ", width, "x", height, " exec time ", stop - start
        # test += 1
        
        
        
        
# $ pypy 15.py
# 6
# Grid:  2 x 2  exec time  0.0
# 20
# Grid:  3 x 3  exec time  0.00399994850159
# 70
# Grid:  4 x 4  exec time  0.0
# 252
# Grid:  5 x 5  exec time  0.0
# 924
# Grid:  6 x 6  exec time  0.00400018692017
# 3432
# Grid:  7 x 7  exec time  0.0179998874664
# 12870
# Grid:  8 x 8  exec time  0.0120000839233
# 48620
# Grid:  9 x 9  exec time  0.0119998455048
# 184756
# Grid:  10 x 10  exec time  0.0150001049042
# 705432
# Grid:  11 x 11  exec time  0.0539999008179
# 2704156
# Grid:  12 x 12  exec time  0.209000110626
# 10400600
# Grid:  13 x 13  exec time  0.776999950409
# 40116600
# Grid:  14 x 14  exec time  3.02600002289
# 155117520
# Grid:  15 x 15  exec time  11.7249999046
