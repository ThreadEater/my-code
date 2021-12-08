def f(s):
    temp = list(map(str,s.split()))
    temp.reverse()
    ans = ' '.join(temp)
    return ans
if __name__ == "__main__":
    s = input()
    print(f(s))