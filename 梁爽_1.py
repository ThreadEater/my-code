def main():
    s = 0
#累加变量赋初值为0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
#输入两个列表
    for i in range (0,min(len(a),len(b))):
        s += a[i]*b[i]
#通过循环累加
    print (s)
if __name__=="__main__":
    main()