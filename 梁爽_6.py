def main():
    peachNumber = 1
#最后剩一个苹果
    for i in range (1,10):
        peachNumber = (peachNumber + 1) * 2
#通过递推计算最初的苹果数
    print(peachNumber)
#输出结果
if __name__=="__main__":  
    main()
