import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math
import os

from matplotlib.font_manager import FontManager, FontProperties


plt.rcParams['figure.dpi'] = 300 #分辨率
with np.errstate(divide='ignore'):
    np.float64(1.0) / 0.0

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
def func(c,mn,csi, a1,a2,a3):

    #return a*np.power(b,r-1)#sigurd
    return a1*(-215023*c*c+133.41*c+0.9014)+a2*(32711*mn*mn-117.96*mn+0.9524)+a3*(0.00005*csi*csi-0.0061*csi+1.2579)

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

folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data7.0.xlsx')
df=df.query('C采收率<1&转炉终点温度!=0&0.0002<转炉终点C<0.0015')
c=list(df['转炉终点C'])
mn=list(df['转炉终点Mn'])
csi=list(df['碳化硅(55%)'])
rate=list(df['C采收率'])

c = (np.array(c))
mn = (np.array(mn))
csi= (np.array(csi))
rate= (np.array(rate))


a1=7.14731948768581E-5
a2=1.12909534244663
a3=-0.0554334702947239
a4=0.00748929395470595

result=func(c,mn,csi,a1,a2,a3)
plt.plot(x, y, 'green', label='data', linestyle=":")
plt.plot(x, y_fit, 'black', label='fit')
plt.show()
