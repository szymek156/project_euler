def main():

    sizeOfSquare = 1001
    
    sumOfDiagonals = 0
    
    firstDiag = 1

    # for i in range(2, sizeOfSquare + 3, 2):
        # firstDiag += (((i+1)/2) - 1) * 8
        # secondDiag = firstDiag - (i - 2)
        # thirdDiag  = secondDiag - (i - 2)
        # fourthDiag = thirdDiag - (i - 2)
        
        # print "#1 ", firstDiag
        
        # sumOfDiagonals += firstDiag 
        
        # if (secondDiag > 1):
            # print "#2 ", secondDiag
            # sumOfDiagonals += secondDiag 
        # if (thirdDiag > 1):
            # print "#3 ", thirdDiag
            # sumOfDiagonals += thirdDiag 
        # if (fourthDiag > 1):
            # print "#4 ", fourthDiag
            # sumOfDiagonals += fourthDiag 
            
        # print "#############################"

    # print "Sum of diags ", sumOfDiagonals
    
    
    for k in range (3, 9 + 1, 2):
        firstDiag = k*k
        secondDiag = firstDiag - (k-1)
        thirdDiag = secondDiag - (k-1)
        fourthDiag = thirdDiag - (k-1)

        print "#1 ", firstDiag
        sumOfDiagonals = 0
        
        sumOfDiagonals += firstDiag 
        
        if (secondDiag > 1):
            print "#2 ", secondDiag
            sumOfDiagonals += secondDiag 
        if (thirdDiag > 1):
            print "#3 ", thirdDiag
            sumOfDiagonals += thirdDiag 
        if (fourthDiag > 1):
            print "#4 ", fourthDiag
            sumOfDiagonals += fourthDiag         
        
        print "Sum of diags ", sumOfDiagonals
        print "poly ", 4*k*k - 6*k + 6
        
        print "#############################"
        
if __name__ == "__main__":
    main()
