def main():
    addAge = 0
    maleNumber = 0
    population = 0
    while(True): 
        line = input()
        if (line ==""):
            break;
        else:
            population += 1
            name,sex,age = line.split()
            if (sex=="男"):
                maleNumber += 1
            addAge += int(age)
    averageAge = addAge/population
    print("平均年龄是：","%.2f" % averageAge)
    print("男生的人数是：",maleNumber)
if (__name__=="__main__"):
    main()
    
        