import math
def main():
    prime = []
    s = 0
    for i in range(51,151):  
        judge = True
        for j in range(2,math.ceil(math.sqrt(i))):
            if (i % j == 0):
                judge = False
        if (judge == True):
            s += 1
            prime.append(i)
            
    print(s)
    print(prime)
    
if (__name__ == "__main__"):
    main()