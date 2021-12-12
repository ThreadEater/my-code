fo = open('earpa001.txt','w')
with open('sensor.txt',encoding=('utf-8')) as fp:
    for line in fp:
        if ('earpa001' in line):
            a,b,c,d = line.strip('\n').split(',')
            fo.write('{},{},{},{}\n'.format(a,b,c,d))
fo.close()
fp.close()
            


