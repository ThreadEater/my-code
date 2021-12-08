import re
s = input()
ans = list(re.split("[^0-9]", s))
op = max(ans,key = len)
print(op)