import pandas as pd
import os

folder='data/'
filenames = os.listdir(folder)
df = pd.read_excel(folder + 'data7.0.xlsx')

def func(df):#并行计算C与Mn的采收率
    #Mn添加量
    mn_add=df['硅铝锰合金球']*0.3+df['硅锰面（硅锰渣）']*0.664+df['锰硅合金FeMn64Si27(合格块)']*0.664+df['锰硅合金FeMn68Si18(合格块)']*0.664
    #C添加量
    c_add=df['钒铁(FeV50-A)']*0.0031+df['钒铁(FeV50-B)']*0.0031+df['硅铝合金FeAl30Si25']*0.00374\
      +df['硅锰面（硅锰渣）']*0.017+df['硅铁(合格块)']*0.0006+df['硅铁FeSi75-B']*0.0006\
       +df['石油焦增碳剂']*0.96+df['锰硅合金FeMn64Si27(合格块)']*0.017+df['锰硅合金FeMn68Si18(合格块)']*0.017\
      +df['碳化硅(55%)']*0.3+df['硅钙碳脱氧剂']*0.225692308
    #添加剂总量
    sumadd=df['钒铁(FeV50-A)']+df['钒铁(FeV50-B)']+df['硅铝合金FeAl30Si25']\
        +df['硅锰面（硅锰渣）']+df['硅铁(合格块)']+df['硅铁FeSi75-B']\
        +df['石油焦增碳剂']+df['锰硅合金FeMn64Si27(合格块)']+df['锰硅合金FeMn68Si18(合格块)']\
        +df['碳化硅(55%)']+df['硅钙碳脱氧剂']+df['氮化钒铁FeV55N11-A']+df['低铝硅铁']\
        +df['钒氮合金(进口)']+df['硅铝钙']+df['硅铝锰合金球']
    #C变化量
    c_a=df['连铸正样C']*(df['钢水净重']-sumadd)-df['转炉终点C']*(df['钢水净重'])
    #Mn变化量
    mn_a=df['连铸正样Mn']*(df['钢水净重']-sumadd)-df['转炉终点Mn']*(df['钢水净重'])

    b_c=c_add
    b_mn=mn_add
    #C、Mn采收率
    c_rate=c_a/c_add
    mn_rate=mn_a/mn_add
    return c_rate
rate=func(df)
print(rate)

#保存于csv中
df = pd.read_csv(folder + 'data1.0.csv',encoding='gbk')


