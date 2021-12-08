s = input()
s = reversed(s)
ans = list()
for i in s:
    if (i not in ans):
        ans = s.append(i)
ans.reverse()
print(ans)