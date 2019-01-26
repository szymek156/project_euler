
def main():
    i = 1
    j = 1
    sum = 0
    term = 0
    
    while term <= 4000000:
        term = i + j
        
        if (term % 2 == 0):
            sum += term

        print term
        i = j
        j = term

    print sum


if __name__ == "__main__":
    main()