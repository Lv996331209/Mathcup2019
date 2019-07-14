import pandas as pd
import numpy as np
import xlrd
import os
import matplotlib.pyplot as plt
folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data4.0.xlsx')

x=['1630<=转炉终点温度<1635',
'1635<=转炉终点温度<1640',
'1640<=转炉终点温度<1645',
'1645<=转炉终点温度<1650',
'1650<=转炉终点温度<1655',
'1655<=转炉终点温度<1660',
]
df=df.query('C采收率<1&转炉终点温度!=0&0.0002<转炉终点C<0.0015')
#df=df.query('1630<=转炉终点温度<1660')
tem=list(df['转炉终点温度'])
rate=list(df['C采收率'])
si=list(df['转炉终点Si'])
s=list(df['转炉终点S'])
p=list(df['转炉终点P'])
c=list(df['转炉终点C'])
gang=list(df['钢水净重'])
sica=list(df['锰硅合金FeMn68Si18(合格块)'])
mn=list(df['转炉终点Mn'])
fan1=list(df['钒铁(FeV50-A)'])
fan2=list(df['钒铁(FeV50-B)'])

x=[]
y=[]
t=[]


array=list(np.linspace(0.0005,0.0016,12))

for i in array:
    sum=0
    num=0
    for j in range(len(mn)):
        if i==mn[j]:
            sum=sum+rate[j]
            num=num+1
    if num!=0:
        sum=sum/num
    else:
        sum=0
    x.append(i)
    y.append(sum)

dict={'x':x,'y':y}
df3 = pd.DataFrame(dict)
df3.to_csv(path_or_buf='mn_c.csv',header=None,index=None,encoding='gbk')

plt.plot(x,y,'ro',c='red')

plt.show()
