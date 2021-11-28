def main():
    number = 3
#从3开始遍历查找
    while (True):
        number += 1
        if (number%3==2 and number%5==3 and number%7==2):
#判断是否为要求的数
            print(number)
            break
#找到一个结果后停止执行
if __name__=="__main__":
    main()