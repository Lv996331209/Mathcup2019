import numpy as np
import matplotlib.pyplot as plt
#读取1stOpt拟合结果
x=[]
y=[]
y_fit=[]
f=open("数据2132.txt","r")
for line in f:
    tag=line.split()
    x.append(int(tag[0]))
    y.append(float(tag[1]))
    y_fit.append(float(tag[2]))
#处理数据添加于新的列表中
newx=[]
newy=[]
newfit=[]
for i in range(len(x)):
        newx.append(x[i]*3.2)
        newy.append(y[i])
        newfit.append(y_fit[i])

#计算拟合优度R^2
def cal_rr(y0, y):
    sstot = 0
    ave = np.mean(y)
    for i in y:
        sstot = sstot + (i - ave) ** 2
    ssreg = 0
    for i in y0:
        ssreg = ssreg + (i - ave) ** 2
    ssres = 0
    for i in range(len(y0)):
        ssres = ssres + (y[i] - y0[i]) ** 2
    r2 = 1 - ssres / sstot
    return r2
print(cal_rr(y_fit,y))
print(cal_rr(newfit,newy))
#绘图显示拟合曲线与实际数据
plt.ylim(0.8, 1.0)
plt.plot(newx,newy,'.',label='data')
plt.plot(newx,newfit,'red',label='fit')
plt.show()
