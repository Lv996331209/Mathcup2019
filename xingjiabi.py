import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
#读取文件获取数据
folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'D题附件1已补全成本2236.xlsx')
df=df.query('转炉终点温度!=0&0.0002<转炉终点C<0.0015')
zhuan=list(df['转炉终点C'])
lian=list(df['连铸正样C'])
cost=list(df['成本'])
index=[]
x=[]
y=cost
#处理数据，计算C需求量
for i in range(len(zhuan)):
    x.append(lian[i]-zhuan[i])
    index.append(i)
print(min(x),max(x))
#创建数组保存最优配比
newx=[]
newy=[]
newin=[]
#获取C需求数列
array=list(np.linspace(0.00083,0.00218,136))
aa = -1
bb = -1
#计算同等需求量下最小值
for i in array:
    min=60000
    tag=10000
    check=0
    for j in range(len(x)):
        if x[j]==i:
            if y[j]<min:
                min=y[j]
                tag=index[j]
                check=1
    if check:
        newx.append(i)
        newy.append(min)
        newin.append(tag)
        aa=min
        bb=tag
    else:
        newx.append(i)
        newy.append(aa)
        newin.append(bb)


#保存数据输出
dict={'C需求':array,'成本':newy,'配方':newin}
df3 = pd.DataFrame(dict)
df3.to_csv(path_or_buf='成本配方.csv',header=None,index=None,encoding='gbk')
#绘图查看成本分布
plt.plot(newx, newy,'.',label='data')
plt.show()