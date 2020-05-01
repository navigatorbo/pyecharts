# add(name,x_axis,y_axis,extra_data = None,symbol_size = 10,**kwargs)
# extra_data -> int:第三维数据（可在 visualmap 中将视图元素映射到第三维度）
# symbol_size -> int: 标记图形大小，默认为10

# ▶代码1：
# from pyecharts import Scatter
# v1 = [5,20,35,50,65,80]
# v2 = [10,20,30,40,50,60]
# scatter = Scatter('散点示例图')
# scatter.add('A',v1,v2)
# scatter.add('B',v1[::-1],v2)    #v1[::-1]代表切片倒序
# scatter.render('./html/scatter01.html')

# ▶代码2：(引入第三维/类似气泡图)
from pyecharts import Scatter
v1 = [5,20,35,50,65,80]
v2 = [10,20,30,40,50,60]
scatter = Scatter('散点-气泡示例图')
scatter.add('A',v1,v2)
scatter.add('B',v1[::-1],v2,                #v1[::-1]代表切片倒序
            is_visualmap = True,            #显示滑动条
            symbol_size = 30,               #显示图内标点大小
            vasual_range_size = [20,80])    #显示滑动范围
scatter.render('./html/scatter02.html')