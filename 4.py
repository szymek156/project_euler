
def isPalindrome(product):
    prodStr = str(product)
    reversed = prodStr[::-1]
    
    return (prodStr == reversed)
    

def main():
    biggest = 0
    for i in range(10, 1000):
        for j in range(10, 1000):
            product = i * j 
            
            if (isPalindrome(product)):
                if (product > biggest):
                    biggest = product
                    print "i ", i, ", j ", j
                    print biggest
            



if __name__ == "__main__":
    main()