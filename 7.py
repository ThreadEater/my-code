def fibonacci(number):
#定义斐波那契数列递归函数
    if (number == 1):
        return 1
    if (number == 2):
        return 1
#设置递归边界
    return fibonacci(number - 1) + fibonacci(number - 2)
#递归调用
if __name__== "__main__":
    print(fibonacci(12))
    