import pandas as pd
import numpy as np
import xlrd
import os
import matplotlib.pyplot as plt
folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data2.0.xlsx')
#def func(df):
#    df['C采收率']>
add = df['硅铝锰合金球'] * 0.3 + df['硅锰面（硅锰渣'] * 0.664 + df['锰硅合金FeMn64Si27(合格块)'] * 0.664 + df['锰硅合金FeMn68Si18(合格块)'] * 0.664
#df=df.query('钢号==\'HRB400B    \'&C采收率<1&转炉终点温度!=0&转炉终点C!=0')
#print(df)
x=['1600<=转炉终点温度<1610',
'1610<=转炉终点温度<1620',
'1620<=转炉终点温度<1630',
'1630<=转炉终点温度<1640',
'1640<=转炉终点温度<1650',
'1650<=转炉终点温度<1660',
'1660<=转炉终点温度<1670',
'1670<=转炉终点温度<1680',
'1680<=转炉终点温度<1690',
'1700<=转炉终点温度<1710',
'1710<=转炉终点温度<1720',
'1720<=转炉终点温度<1730',
'1730<=转炉终点温度<1740',
'1740<=转炉终点温度<1750']
df=df.query('C采收率<1&转炉终点温度!=0&转炉终点C!=0')
for i in x:
    df = pd.read_excel(folder + 'data2.0.xlsx')
    df = df.query('C采收率<1&转炉终点温度!=0&转炉终点C!=0')
    df=df.query(i)

    print(len(df))
tem=list(df['转炉终点温度'])
y=list(df['C采收率'])
c=list(df['转炉终点C'])
s=list(df['转炉终点S'])
p=list(df['转炉终点P'])
si=list(df['转炉终点Si'])
#xs=[]
#xp=[]
#for i in range(len(c)):
#    xs.append(s[i]/c[i])
#    xp.append(p[i]/c[i])

#print(df)
sum=0
for i in y:
    sum=sum+i
print(sum/len(y))
#array=list(np.linspace(1600,1750,16))
#print(array)

#plt.plot(tem,y,'ro',c='red')
#plt.plot(xp,y,'ro',c='blue')
#plt.legend(['S','P','Si'])
#plt.show()
#df.to_csv('C>1.csv',encoding='gbk')
#y=[
#0.838085179
#,0.82685368
#,0.813300862
y=[0.886437403
,0.86841818
,0.879503029
,0.881665317
,0.873647903
,0.875265956
,0.850447333]
#,0.850765989
#,0.864460812
#,0.92803351
#,0.972844519]

plt.plot([1630,1640,1650,1660,1670,1680,1690],y,'ro',c='red')
plt.show()