fo = open('earpa001_count.txt','w')
with open('earpa001.txt',encoding=('utf-8')) as fp:
    d = {}
    for line in fp:
        a = line.strip('\n').split(',')
        b = a[2] + '-' + a[3]
        if d.get(b,0):
            d[b] += 1
        else:
            d[b] = 1
    ls = list(d.items())
    ls.sort(key=lambda x:x[1], reverse=True) # ∏√”Ôæ‰”√”⁄≈≈–Ú
    for key,value in ls:
        fo.write('{},{}\n'.format(key,value))
fo.close()
fp.close()



