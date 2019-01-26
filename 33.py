def main():
    for j in range(10, 100):
        for i in range(j, 100):
        
            result = j/float(i)
            
            if result == 1.0:
                continue
           
            j1 = j / 10
            j2 = j % 10
            i1 = i / 10
            i2 = i % 10
            
            if i2 == 0 or (i1 == i2 and j1 == j2):
                continue
                
            result2 = 0
            result3 = 0 
            result4 = 0 
            result5 = 0
            
            if i1 != 0:
                if j2 == i2:
                    result2 = j1 / float(i1)
                if j1 == i2:
                    result4 = j2 / float(i1)
                
            if i2 != 0:
                if j2 == i1:
                    result3 = j1 / float(i2)
                if j1 == i1:
                    result5 = j2 / float(i2)
                
            if result in [result2, result3, result4, result5]:
                print j, "/", i
            


if __name__ == "__main__":
    main()