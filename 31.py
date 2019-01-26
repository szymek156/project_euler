
# def dummyWay(total):
    # found = 0
    # for h in range(0, total/200 + 1):
        # for g in range(0, total/100 + 1):
            # for f in range(0, total/50 + 1):
                # for e in range(0, total/20 + 1):
                    # for d in range(0, total/10 + 1):
                        # for c in range(0, total/5 + 1):
                            # for b in range(0, total/2 + 1):
                                # for a in range(0, total/1 + 1):
                                    # if h*200 + g*100 + f*50 + e*20 + d*10 + c*5 + b*2 + a == total:
                                        # #print "5x", c, " 2x", b, " 1x", a
                                        # found += 1
def smartWay(total):
    coinSizes = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (total + 1)
    ways[0] = 1
     
    for i in coinSizes:
        for j in range(i, total + 1):
            ways[j] += ways[j - i]
            
    print ways
    
def main():
    print  " found ", smartWay(100)
    


if __name__ == "__main__":
    main()