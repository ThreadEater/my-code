def main():  
    s = input().split()
#读入一行用空格隔开的元素，并存入列表s中
    dict1 = {}
#创建空字典，键为出现的职业，值为出现的次数
    for i in s:
        if dict1.get(i,0):
            dict1[i] += 1
#每出现一次对应字典元素的值加一
        else:
            dict1[i] = 1
#只出现过一次的字典元素的值为1
    dict1 = sorted(dict1.items(), key=lambda x:x[1],reverse=True)
#按照出现次数对字典进行排序
    for key,value in dict1:
        print("{}:{}".format(key,value))
#按照键：值的格式对字典进行格式化输出
if __name__=="__main__": 
    main()