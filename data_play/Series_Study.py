#Series 基本特征：类似一维数组的对象，由数组和索引组成
from pandas import Series
import pandas as pd
import numpy
aSer =pd.Series([1,2.0,'a'])  #创建数组，自带索引
print(pd.Series(['apple','peach','lemon'],index=[1,2,3]))
print(aSer)    #查看索引，index属性，查看值，values属性
bSer = Series([3,5,7],index=['a','b','c'])
print(bSer*2)
print(bSer['a'])
print(numpy.exp(bSer))   #计算自然对数的n次方

data = {'AXP':'88.60','CSCO':'122.64','BA':'99.44'}
sindex = {'AXP','CSCO','BA','SSPL'}
cSer=pd.Series(data,sindex)   # 数据对齐
print(cSer)
print(pd.isnull(cSer))  #判断是否为空
# 两组数据也可以进行 加减乘除，有对应的话，进行运算，没有的话，为NaN

#可以指定对象的name属性
cSer.name = 'cnames'
cSer.index.name='volume'
print(cSer)
