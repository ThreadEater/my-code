def main():  
    j = 1
    factor = []
    number = int(input())
    number1 = number
    while(number != 1):
        j+=1
        if (number % j == 0):
            number /= j
            factor.append(str(j))
            j = 1
    print(number1,'=','*'.join(factor))
if (__name__ == '__main__'):
    main()      
            
