import pandas as pd
import numpy as np
import xlrd
import os
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d.axes3d import Axes3D

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = u'SimHei'

matplotlib.rcParams['axes.unicode_minus'] = False

x = np.random.randint(0, 10, size=100)
y = np.random.randint(-20, 20, size=100)
z = np.random.randint(0, 30, size=100)


folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data4.0.xlsx')
df=df.query('0<C采收率<1&转炉终点温度!=0&转炉终点C!=0')
df=df.query('转炉终点Si<0.005')

tem=list(df['转炉终点温度'])
rate=list(df['C采收率'])
c=list(df['转炉终点C'])
mn=list(df['转炉终点Mn'])
si=list(df['转炉终点Si'])
s=list(df['转炉终点S'])
p=list(df['转炉终点P'])

# x=[]
# y=[]
# z=[]
#
# array=list(np.linspace(1630,1750,121))
# sarray=[0.001,0.002,0.003,0.004]
# for ss in sarray:
#     for i in array:
#         sum=0
#         num=0
#         for j in range(len(tem)):
#             if i==tem[j] and ss==si[j]:
#                 sum=sum+rate[j]
#                 num=num+1
#         if num!=0:
#             sum=sum/num
#         else:
#             sum=0
#         x.append(i)
#         y.append(ss)
#         z.append(sum)

# 此处fig是二维
fig = plt.figure()

# 将二维转化为三维
axes3d = Axes3D(fig)
xx=c
yy=mn
zz=rate
# print(len(x))
# print(len(y))
# print(len(z))
# for j in range(len(z)):
#     if z[j]==0:
#         continue
#     else:
#         xx.append(x[j])
#         yy.append(y[j])
#         zz.append(z[j])

plt.xlabel('C')
plt.ylabel('Mn')


axes3d.scatter(xx, yy, zz)
plt.show()