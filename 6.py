
def main():
    sumOfSquares = 0
    squareOfSum  = 0
    
    for i in range(1, 101):
        sumOfSquares += (i * i)
        squareOfSum  += i
        
    squareOfSum *= squareOfSum
    
    print "sum of squares ", sumOfSquares, " squareOfSum ", squareOfSum, " diff ", squareOfSum - sumOfSquares

if __name__ == "__main__":
    main()