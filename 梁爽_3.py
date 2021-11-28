import random
def main():
    a = list(map(str,input().split()))
#创建列表
    print(a[random.randint(0, len(a))])
#通过列表下标的随机数，随机输出列表中的元素
if __name__=="__main__":
    main()