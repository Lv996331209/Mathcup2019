import pandas as pd
import numpy as np
import xlrd
import os
import matplotlib.pyplot as plt
folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data2.0.xlsx')

x=['1630<=转炉终点温度<1635',
'1635<=转炉终点温度<1640',
'1640<=转炉终点温度<1645',
'1645<=转炉终点温度<1650',
'1650<=转炉终点温度<1655',
'1655<=转炉终点温度<1660',
]
df=df.query('C采收率<1&转炉终点温度!=0&转炉终点C!=0')
count=[]
for i in x:
    df = pd.read_excel(folder + 'data2.0.xlsx')
    df = df.query('C采收率<1&转炉终点温度!=0&转炉终点C!=0')
    df=df.query(i)
    y = list(df['C采收率'])
    sum = 0
    for i in y:
        sum = sum + i
    count.append(sum / len(y))
print(count)

plt.plot([1630,1635,1640,1645,1650,1655],count,'ro',c='red')
plt.show()