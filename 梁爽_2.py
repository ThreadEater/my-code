import random
def main():
    aList = [random.randint(1, 1000) for i in range(0,20)]
#列表推导式生成20个随机数
    aList.sort()
#排序
    for i in range(0,20):
        if (i == 19):
            print(aList[i])
        else:
            print(aList[i],end=",")
#打印结果
if __name__=="__main__":
    main()
