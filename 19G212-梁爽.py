# -*- coding: utf-8 -*-
"""
Created on Mon Dec  12 12:30:22 2021

@author: 梁爽
"""
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox

#【任务一】、【任务二】
def dataPreprocessing():
    while True:
        try:
            #查看前五行、后两行
            df = pd.read_csv("pollution_us_5city_2006_2010_O3.csv",encoding=("utf8"))
            print(df.iloc[0:5],'\n',df.iloc[df.shape[0]-2:df.shape[0]])
            #选择2007-2009年的数据
            df1 = df[df['Date Local'].str.contains("2007|2008|2009")]
            #处理缺失值
            df1 = df1.dropna()
            # 结果导出
            df1.to_csv("pollution_us_5city_2007_2009_03.csv",index = False)
            return True
        except:
            return False

def dataSelecting():
    while True:
        try:
            #读取文件
            df = pd.read_csv("pollution_us_5city_2007_2009_03.csv")
            #按条件筛选切片
            df1 = df[df['City'] == 'Houston']
            df2 = df[df['City'] == 'New York']
            df3 = df[df['City'] == 'Washington']
            #导出
            df1.to_csv("pollution_us_Houston_2007_2009_O3.txt",sep=' ',index = False)
            df2.to_csv("pollution_us_NewYork_2007_2009_O3.txt",sep=' ',index = False)
            df3.to_csv("pollution_us_Washington_2007_2009_O3.txt",sep=' ',index = False)
            
            return True
        except:
            return False

def dataTransformation():
    while True:
        try:
            #读取文件
            df1 = pd.read_csv("pollution_us_Houston_2007_2009_O3.txt",sep=' ',encoding=("utf8"))
            df2 = pd.read_csv("pollution_us_NewYork_2007_2009_O3.txt",sep=' ',encoding=("utf8"))
            df3 = pd.read_csv("pollution_us_Washington_2007_2009_O3.txt",sep=' ',encoding=("utf8"))
            #转存文件
            df1.to_excel("pollution_us_Houston_2007_2009_03.xlsx",index = False)
            df2.to_excel("pollution_us_New York_2007_2009_03.xlsx",index = False)
            df3.to_excel("pollution_us_Washington_2007_2009_03.xlsx",index = False)
            return True
        except:
            return False
def dataVisualization():
    while True:
        try:
            #读取数据
            df1 = pd.read_excel("pollution_us_Houston_2007_2009_03.xlsx")
            df2 = pd.read_excel("pollution_us_New York_2007_2009_03.xlsx")
            df3 = pd.read_excel("pollution_us_Washington_2007_2009_03.xlsx")
            
            #df切片转列表生成绘图数据
            x1_data = df1['Date Local'].values.tolist()
            
            x2_data = df2['Date Local'].values.tolist()
            
            x3_data = df3['Date Local'].values.tolist()
            #改变数据样式
            for i in range(0,len(x1_data)):
                x1_data[i] = x1_data[i][0:x1_data[i].rindex('/')].replace("/","-")
                
            for i in range(0,len(x2_data)):
                x2_data[i] = x2_data[i][0:x2_data[i].rindex('/')].replace("/","-")
                
            for i in range(0,len(x3_data)):
                x3_data[i] = x3_data[i][0:x3_data[i].rindex('/')].replace("/","-")
            
            #数据去重并保持原顺序
            formatList = list(set(x1_data))
            formatList.sort(key=x1_data.index)
            x1_data = formatList
             
            formatList = list(set(x2_data))
            formatList.sort(key=x2_data.index)
            x2_data = formatList
            
            formatList = list(set(x3_data))
            formatList.sort(key=x3_data.index)
            x3_data = formatList
            
            #计算每个月的均值数据
            y1_data1 = []
            y1_data2 = []
            y1_data3 = []
            
            y2_data1 = []
            y2_data2 = []
            y2_data3 = []
            
            y3_data1 = []
            y3_data2 = []
            y3_data3 = []
                    
            for i in x1_data:    
                temp = df1[df1["Date Local"].str.contains(i.replace('-','/'))]
                y1_data1.append(sum(temp['O3 Mean'].values.tolist())/temp.shape[0])
                y2_data1.append(sum(temp['O3 AQI'].values.tolist())/temp.shape[0])
                y3_data1.append(sum(temp['O3 1st Max Hour'].values.tolist())/temp.shape[0])
                
            for i in x2_data:    
                temp = df2[df2["Date Local"].str.contains(i.replace('-','/'))]
                y1_data2.append(sum(temp['O3 Mean'].values.tolist())/temp.shape[0])
                y2_data2.append(sum(temp['O3 AQI'].values.tolist())/temp.shape[0])
                y3_data2.append(sum(temp['O3 1st Max Hour'].values.tolist())/temp.shape[0])    
                
            for i in x3_data:    
                temp = df3[df3["Date Local"].str.contains(i.replace('-','/'))]
                y1_data3.append(sum(temp['O3 Mean'].values.tolist())/temp.shape[0])
                y2_data3.append(sum(temp['O3 AQI'].values.tolist())/temp.shape[0])
                y3_data3.append(sum(temp['O3 1st Max Hour'].values.tolist())/temp.shape[0])
                
            #画图并设置图例与样式
            
            plt.figure(figsize=(20,10))
            plt.plot(x1_data,y1_data1,color = 'red',label = 'Houston')
            plt.plot(x1_data,y1_data2,color = 'green',label = 'New York')
            plt.plot(x1_data,y1_data3,color = 'blue',label = 'Washington')
            plt.xticks(rotation=90)
            plt.legend(loc="best")
            plt.xlabel('Year-Month')
            plt.ylabel('O3 Mean')
            plt.title('Houston NewYork Washington 2007-2009 O3 Mean')
            plt.savefig('Houston_NewYork_Washington_2007_2009_O3Mean.jpg',bbox_inches='tight',dpi=100)
            
            plt.figure(figsize=(20,10))
            plt.plot(x2_data,y2_data1,color = 'red',label = 'Houston')
            plt.plot(x2_data,y2_data2,color = 'green',label = 'New York')
            plt.plot(x2_data,y2_data3,color = 'blue',label = 'Washington')
            plt.xticks(rotation=90)
            plt.legend(loc="best")
            plt.xlabel('Year-Month')
            plt.ylabel('O3 AQI')
            plt.title('Houston NewYork Washington 2007-2009 O3 AQI')
            plt.savefig('Houston_NewYork_Washington_2007_2009_O3AQI.jpg',bbox_inches='tight',dpi=100)
            
            plt.figure(figsize=(20,10))
            plt.plot(x3_data,y3_data1,color = 'red',label = 'Houston')
            plt.plot(x3_data,y3_data2,color = 'green',label = 'New York')
            plt.plot(x3_data,y3_data3,color = 'blue',label = 'Washington')
            plt.xticks(rotation=90)
            plt.legend(loc="best")
            plt.xlabel('Year-Month')
            plt.ylabel('O3 1st Max Hour')
            plt.title('Houston NewYork Washington 2007-2009 O3 1st Max Hour')
            plt.savefig('Houston_NewYork_Washington_2007_2009_O31stMaxHour.jpg',bbox_inches='tight',dpi=100)
            
            return True
        except:
            
            return False

#定义按钮效果函数
def cmd1(): 
    #弹窗输入输出交互
    def cmd11():
        def cmd12():
            root2.destroy()
            judge = dataPreprocessing()
            if judge==True:
                tkinter.messagebox.showinfo("消息","任务一、任务二执行成功")
            else:
                tkinter.messagebox.showerror("错误","任务一、任务二执行失败")
        root1.destroy()
        root2 = tkinter.Tk()
        root2.title("交互界面")
        xls_text = tkinter.StringVar()
        l1 = tkinter.Label(root2, text="请输入要输出的文件名：pollution_us_5city_2007_2009_03.csv")
        l1.pack()  
        xls = tkinter.Entry(root2, textvariable=xls_text)
        xls_text.set("     ")
        xls.pack()
        tkinter.Button(root2, text="点击确认", command=cmd12).pack()
    
    root1 = tkinter.Tk()
    root1.title("交互界面")
    xls_text = tkinter.StringVar()
    l1 = tkinter.Label(root1, text="请输入要读取的文件名：pollution_us_5city_2006_2010_O3.csv")
    l1.pack()  
    xls = tkinter.Entry(root1, textvariable=xls_text)
    xls_text.set("     ")
    xls.pack()
    tkinter.Button(root1, text="点击确认", command=cmd11).pack()
    
def cmd2():
    #弹窗输入输出交互
    def cmd21():
        def cmd22():
            def cmd23():
                def cmd24():
                    root4.destroy()
                    judge = dataSelecting()
                    if judge==True:
                        tkinter.messagebox.showinfo("消息","任务三执行成功")
                    else:
                        tkinter.messagebox.showerror("错误","任务三执行失败")
                root3.destroy()
                root4 = tkinter.Tk()
                root4.title("交互界面")
                xls_text = tkinter.StringVar()
                l1 = tkinter.Label(root4, text="请输入要输出的第三个文件名：pollution_us_Washington_2007_2009_O3.txt")
                l1.pack()  
                xls = tkinter.Entry(root4, textvariable=xls_text)
                xls_text.set("     ")
                xls.pack()
                tkinter.Button(root4, text="点击确认", command=cmd24).pack()
                
            root2.destroy()
            root3 = tkinter.Tk()
            root3.title("交互界面")
            xls_text = tkinter.StringVar()
            l1 = tkinter.Label(root3, text="请输入要输出的第二个文件名：pollution_us_NewYork_2007_2009_03.txt")
            l1.pack()  
            xls = tkinter.Entry(root3, textvariable=xls_text)
            xls_text.set("     ")
            xls.pack()
            tkinter.Button(root3, text="点击确认", command=cmd23).pack()
            
        root1.destroy()
        root2 = tkinter.Tk()
        root2.title("交互界面")
        xls_text = tkinter.StringVar()
        l1 = tkinter.Label(root2, text="请输入要输出的第一个文件名：pollution_us_Houston_2007_2009_O3.txt")
        l1.pack()  
        xls = tkinter.Entry(root2, textvariable=xls_text)
        xls_text.set("     ")
        xls.pack()
        tkinter.Button(root2, text="点击确认", command=cmd22).pack()
        
    root1 = tkinter.Tk()
    root1.title("交互界面")
    xls_text = tkinter.StringVar()
    l1 = tkinter.Label(root1, text="请输入要读取的文件名：pollution_us_5city_2007_2009_03.csv")
    l1.pack()  
    xls = tkinter.Entry(root1, textvariable=xls_text)
    xls_text.set("     ")
    xls.pack()
    tkinter.Button(root1, text="点击确认", command=cmd21).pack()
    
def cmd3():
    #弹窗输入输出交互
    def cmd31():
        def cmd32():
            def cmd33():
                def cmd34():
                    def cmd35():
                        def cmd36():
                            root6.destroy()
                            judge = dataTransformation()
                            if judge==True:
                                tkinter.messagebox.showinfo("消息","任务四执行成功")
                            else:
                                tkinter.messagebox.showerror("错误","任务四执行失败")
                        root5.destroy()
                        root6 = tkinter.Tk()
                        root6.title("交互界面")
                        xls_text = tkinter.StringVar()
                        l1 = tkinter.Label(root6, text="请输入要输出的第三个文件名：pollution_us_Washington_2007_2009_O3.xlsx")
                        l1.pack()  
                        xls = tkinter.Entry(root6, textvariable=xls_text)
                        xls_text.set("     ")
                        xls.pack()
                        tkinter.Button(root6, text="点击确认", command=cmd36).pack()
                    root4.destroy()
                    root5 = tkinter.Tk()
                    root5.title("交互界面")
                    xls_text = tkinter.StringVar()
                    l1 = tkinter.Label(root5, text="请输入要输出的第二个文件名：pollution_us_NewYork_2007_2009_O3.xlsx")
                    l1.pack()  
                    xls = tkinter.Entry(root5, textvariable=xls_text)
                    xls_text.set("     ")
                    xls.pack()
                    tkinter.Button(root5, text="点击确认", command=cmd35).pack()
                root3.destroy()
                root4 = tkinter.Tk()
                root4.title("交互界面")
                xls_text = tkinter.StringVar()
                l1 = tkinter.Label(root4, text="请输入要输出的第一个文件名：pollution_us_Houston_2007_2009_O3.xlsx")
                l1.pack()  
                xls = tkinter.Entry(root4, textvariable=xls_text)
                xls_text.set("     ")
                xls.pack()
                tkinter.Button(root4, text="点击确认", command=cmd34).pack()
            root2.destroy()
            root3 = tkinter.Tk()
            root3.title("交互界面")
            xls_text = tkinter.StringVar()
            l1 = tkinter.Label(root3, text="请输入要读取的第三个文件名：pollution_us_Washington_2007_2009_O3.txt")
            l1.pack()  
            xls = tkinter.Entry(root3, textvariable=xls_text)
            xls_text.set("     ")
            xls.pack()
            tkinter.Button(root3, text="点击确认", command=cmd33).pack()
        root1.destroy()
        root2 = tkinter.Tk()
        root2.title("交互界面")
        xls_text = tkinter.StringVar()
        l1 = tkinter.Label(root2, text="请输入要读取的第二个文件名：pollution_us_NewYork_2007_2009_03.txt")
        l1.pack()  
        xls = tkinter.Entry(root2, textvariable=xls_text)
        xls_text.set("     ")
        xls.pack()
        tkinter.Button(root2, text="点击确认", command=cmd32).pack()
    root1 = tkinter.Tk()
    root1.title("交互界面")
    xls_text = tkinter.StringVar()
    l1 = tkinter.Label(root1, text="请输入要读取的第一个文件名：pollution_us_Houston_2007_2009_O3.txt")
    l1.pack()  
    xls = tkinter.Entry(root1, textvariable=xls_text)
    xls_text.set("     ")
    xls.pack()
    tkinter.Button(root1, text="点击确认", command=cmd31).pack()
def cmd4():
    #弹窗输入输出交互
    def cmd41():
        def cmd42():
            def cmd43():
                def cmd44():
                    def cmd45():
                        def cmd46():
                            root6.destroy()
                            judge = dataVisualization()
                            if judge==True:
                                tkinter.messagebox.showinfo("消息","任务五执行成功")
                            else:
                                tkinter.messagebox.showerror("错误","任务五执行失败")
                        root5.destroy()
                        root6 = tkinter.Tk()
                        root6.title("交互界面")
                        xls_text = tkinter.StringVar()
                        l1 = tkinter.Label(root6, text="请输入要输出的第三个文件名：Houston_ NewYork_Washington_2007 2009_O3lstMaxHour")
                        l1.pack()  
                        xls = tkinter.Entry(root6, textvariable=xls_text)
                        xls_text.set("     ")
                        xls.pack()
                        tkinter.Button(root6, text="点击确认", command=cmd46).pack()
                    root4.destroy()
                    root5 = tkinter.Tk()
                    root5.title("交互界面")
                    xls_text = tkinter.StringVar()
                    l1 = tkinter.Label(root5, text="请输入要输出的第二个文件名：Houston_NewYork_Washington_2007_2009_O3AQI")
                    l1.pack()  
                    xls = tkinter.Entry(root5, textvariable=xls_text)
                    xls_text.set("     ")
                    xls.pack()
                    tkinter.Button(root5, text="点击确认", command=cmd45).pack()
                root3.destroy()
                root4 = tkinter.Tk()
                root4.title("交互界面")
                xls_text = tkinter.StringVar()
                l1 = tkinter.Label(root4, text="请输入要输出的第一个文件名：Houston_NewYork_Washington 2007_2009_O3Mean")
                l1.pack()  
                xls = tkinter.Entry(root4, textvariable=xls_text)
                xls_text.set("     ")
                xls.pack()
                tkinter.Button(root4, text="点击确认", command=cmd44).pack()
            root2.destroy()
            root3 = tkinter.Tk()
            root3.title("交互界面")
            xls_text = tkinter.StringVar()
            l1 = tkinter.Label(root3, text="请输入要读取的第三个文件名：pollution_us_Washington_2007_2009_O3.xlsx")
            l1.pack()  
            xls = tkinter.Entry(root3, textvariable=xls_text)
            xls_text.set("     ")
            xls.pack()
            tkinter.Button(root3, text="点击确认", command=cmd43).pack()
        root1.destroy()
        root2 = tkinter.Tk()
        root2.title("交互界面")
        xls_text = tkinter.StringVar()
        l1 = tkinter.Label(root2, text="请输入要读取的第二个文件名：pollution_us_NewYork_2007_2009_O3.xlsx")
        l1.pack()  
        xls = tkinter.Entry(root2, textvariable=xls_text)
        xls_text.set("     ")
        xls.pack()
        tkinter.Button(root2, text="点击确认", command=cmd42).pack()
    root1 = tkinter.Tk()
    root1.title("交互界面")
    xls_text = tkinter.StringVar()
    l1 = tkinter.Label(root1, text="请输入要读取的第一个文件名：pollution_us_Houston_2007_2009_O3.xlsx")
    l1.pack()  
    xls = tkinter.Entry(root1, textvariable=xls_text)
    xls_text.set("     ")
    xls.pack()
    tkinter.Button(root1, text="点击确认", command=cmd41).pack()

#GUI界面模块
def GUI():
    
    root = tkinter.Tk()
    root['height'] = 300
    root['width'] = 600
    root.resizable(False,False)
    root.title("数据分析与可视化系统-19G212梁爽")
    
    #创建5个按钮并放置用于选择菜单
    button1 = tkinter.Button(root,
                             text ='1、数据读取与预处理',
                             command = cmd1)
    
    button1.place(x = 30,
                  y = 100,
                  width = 225,
                  height = 40)
    
    button2 = tkinter.Button(root,
                             text ='2、数据选择',
                             command = cmd2)
    button2.place(x = 330,
                  y = 100,
                  width = 225,
                  height = 40)
    
    button3 = tkinter.Button(root,
                             text ='3、数据转存',
                             command = cmd3) 
    button3.place(x = 30,
                  y = 200,
                  width = 225, 
                  height = 40)
    
    button4 = tkinter.Button(root,
                             text ='4、数据分析及可视化',
                             command = cmd4)
    button4.place(x = 330,
                  y = 200,
                  width = 225,
                  height = 40) 
    
    #创建标题
    labelTitle = tkinter.Label(root,
                               text='欢迎使用数据分析与可视化系统！请按1-4顺序操作！')
    labelTitle.place(x = 100,
                    y = 0,
                    width = 400,
                    height = 80)
    
    #窗口锁死循环并保持监听
    root.mainloop()
if __name__ == "__main__":    
    GUI()
#458lines