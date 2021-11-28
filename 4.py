import math
def main():  
    j = 1
    factor = []
    number = int(input())
    number1 = number
    while(number != 1):
        j+=1
        judge = True
        for k in range(2,math.ceil(math.sqrt(j))):
            if (j % k == 0):
                judge == False
        if (judge == True and number % j == 0):
            number /= j
            factor.append(j)
            j = 1
    print(number1,'=',end="")
    for i in range(0,len(factor)):
        if (i != len(factor)-1):
            print(factor[i],end="*")
        else:
            print(factor[i])
if (__name__ == '__main__'):
    main()
                
                
                
            