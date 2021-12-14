import pandas as pd
import matplotlib.pyplot as plt

#任务1：读取并处理缺失值
df = pd.read_csv('2020_City_Air_Quality_Index.csv',
                 encoding=('ANSI'))
df = df.dropna()

#任务2：折线图
df1 = pd.DataFrame(df[['date','AQI']])
plt.figure()
df1.plot(x='date')
plt.ylabel('AQI')
plt.title('Every Day-AQI')
plt.savefig('today_AQI.jpg')

#任务3：柱状图
plt.figure()
aqi = [0,0,0,0,0,0,0,0,0,0,0,0]
for index,row in df.iterrows():
    t = row['date']
    t = int(t[t.index('/')+1:t.rindex('/')])
    aqi[t-1] += int(row['AQI'])
month = [1,2,3,4,5,6,7,8,9,10,11,12]
aqi = [i/12 for i in aqi]
plt.bar(month,
        aqi,
        color = '#561225',
        alpha = 0.8,
        edgecolor = 'orange',
        linestyle = '-',
        linewidth = 1)
for x,y in zip(month,aqi):
    plt.text(x, y, '%d' % y)
plt.xlabel('month')
plt.ylabel('AQI')
plt.title('average AQI per month')
plt.savefig('average_AQI_month.jpg')
    
#任务4：输出文件
fo = open('maxMonth.txt','w')
difference = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,12):
    difference[i] = abs(aqi[i]-aqi[i-1])
idx = difference.index(max(difference))
rs = str(idx)+' '+str(idx+1)+'\n'
fo.write(rs)
fo.close()
 
#任务5：饼状图
se = df['AQI']
print
se = se.reset_index(drop = True)
cycle = []
temp = 0
for index,value in se.items():
    temp += value
    if ((index + 1) % 14 == 0):
        cycle.append(temp/14)
        temp = 0
    if ((index + 1 ) >= 70):
        break        
plt.figure()
plt.pie(cycle,
        explode=(0.01,0.02,0.03,0.04,0.05),
        labels=('cycle1','cycle2','cycle3','cycle4','cycle5'),
        colors=('yellow','green','blue','red','orange'),
        autopct='%1.1f%%')
plt.savefig('AQI_2weeks.jpg')
 

