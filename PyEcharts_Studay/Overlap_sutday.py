# add(chart,
#     xaxis_index = 0,
#     yaxis_index = 0,
#     is_add_xaxis = False,
#     is_add_yaxis = False)
# 属性：
# is_add_xaxis / is_add_yaxis 是否新增坐标X/Y 默认 False

# ▶代码1：bar + line 叠加
from pyecharts import Bar,Line,Overlap
attr = ['A','B','C','D','E','F']
v1 = [10,20,30,40,50,60]
v2 = [38,28,35,58,65,70]
bar = Bar('Line - Bar示例')
bar.add('bar',attr,v1)
line = Line()
line.add('line',attr,v2)

overlop = Overlap()
overlop.add(bar)
overlop.add(line)
overlop.render('./html/line-bar01.html')