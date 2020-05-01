import numpy as np
import pandas as pd
from pandas import *

# DataFrame
#基本特征： 一个表格型的数据结构
#含有一组有序的列（类似于index） 大致可看成共享同一个index的Series集合
#DataFrame对象可以由列表，元组，字典创建也可以由ndarray或者Series创建
data ={'name':['Wangdachui','Linling','Niuyun'],'pay':[4000,5000,6000]}
frame = pd.DataFrame(data)
print(frame)
data2 =np.array([('Wangdachui',4000),('Linling',5000),('Niuyuan',6000)])
frame2 =pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
print(frame2)
print(frame.iloc[:2,1])

#DataFrame对象的修改和删除
frame['name']='admin'  #修改列属性
print(frame)
del frame['pay']  #删除列
print(frame)

#DataFrame 的统计功能
print(frame2.pay.min())
print(frame2[frame2.pay>=5000])

