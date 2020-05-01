#ndarray
import numpy as np
import time
import math
# aArray =np.array([1,2,3])
# print(aArray)
#
# print("----------------------")
# bArray = np.array([(7,8,9),(4,5,6)])
# # cArray = bArray.reshape(3,2)   #改变形状3*2  也可以用resize函数，此时bArray的形状真的改变
# # print(cArray)
# # print(bArray)
# dArray = np.array([[4,5,6],[9,8,7]])
# print(np.vstack((aArray,dArray)))  #垂直方向上拼接 水平方向上用hstack
# print(bArray[1]) # 输出第一行
# print(bArray[:,[0,1]])  #所有行 0,1列
# for row in bArray:
#     print(row)
#
#
# print(np.arange(1,5,0.5))
#
# #生成 2*2的 [0,1)的随机数
# print(np.random.random((2,2)))   #这里传递的是元组
# print(np.random.rand(2,2))      #这里传递行数和列数
#
# print(np.linspace(1,2,10,endpoint=False))  #此处的10 表示的是个数，默认的是50
#
# print(np.ones([2,3]))  #2*3 的1
#
# x =np.fromfunction(lambda i,j:(i+1)*(j+1),(9,9))
# print(x)
# print(x.ndim)  #轴的个数 即秩
# print(x.shape) #数组形状

#ndarray的运算
a= np.array([(1,2,3),(4,5,6)])
b=np.array([(2,3,4),(5,6,7)])
c=np.array([7,8,9])
d=np.array([(1,2,3),(4,5,6),(7,8,4)])
print(d.shape)
# print(a*b)  #一一对应着相乘
# print(a+b)  #一一对应相加
# print(a+c)  #不同的数组也可以相加，但须保持形状相同
#
# print(a.sum(axis= 1))
## 求和方法sum(axis=0) 0轴(即列)求和  sum()直接求和
# print(a.argmax()) #最小值
# print(a.mean())  #平均值
# print(a.var()) #方差
# print(a.std()) #标准差
#ndarray的专门应用--线性代数
# print(np.linalg.det(d))   #行列式
# print(np.linalg.inv(d))   #逆矩阵  此处矩阵的det不能为零，不然会报错
# print(np.dot(d,d))   #矩阵内积

#比较math和ndarray函数调用时的时间差距（计算sin(t)的平方）
x=np.arange(0,100,0.01)
t_m1 = time.clock()
for i,t in enumerate(x):
    x[i]=math.pow((math.sin(t)),2)
t_m2 = time.clock()
y=np.arange(0,100,0.01)
t_n1 = time.clock()
y=np.power(np.sin(y),2)
t_n2 = time.clock()
print("Running time of math:",t_m2 - t_m1)
print("Running time of numpy",t_n2 - t_n1)
