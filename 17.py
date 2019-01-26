
numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
    1000 : "onethousand"
}

def getNumberName(order, mod):
    number = order * mod
    
    if (number == 100):
        return "onehundred"
    if (number in numbers):
        return numbers[number]
    else:
        return numbers[mod] + numbers[order]    

def stupidProblem(int):
    
    result = ""
    order = 1
    
    if (int > 100 and int % 100 != 0):
        result += "and"
    
    if (int % 100 in range(11, 20)):
        result += numbers[int % 100]
        int /= 100
        order *= 100
        
    
    

    while (int != 0):
        mod = int % 10

        if (mod != 0): # omit zero to avoid crap like hyaku zero zero == 100
            chunk = getNumberName(order, mod)
            result = chunk + "" + result
        
        int /= 10
        order *= 10
        
    result = result.rstrip()
    
    print result, " ", len(result)
    
    return result

def main():
    sum = 0;
    
    for i in range(1, 1001):
        iStr = stupidProblem(i)
        sum += len(iStr)
        
    print sum

if __name__ == "__main__":
    main()
