import pyecharts
# from pyecharts import Bar
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.use_theme('dark')                                  #暗色背景色
# bar.add("服装",                                        #注解==label
#         ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"], #横坐标
#         [5, 20, 36, 10, 75, 90])                       #纵坐标
# bar.render('./picture1.html')                          #文件存储路径（默认保存当前文件路径）


#
from pyecharts import Bar
# bar = Bar('基本柱状图','副标题')
# bar.add('服装',
#         ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'],
#         [5,20,36,10,75,90],
#         is_more_utils = True    #设置最右侧工具栏
#         )
# bar.show_config()               #调试输出pyecharts的js配置信息
# bar.render('./html/first01.html')


# from pyecharts import Bar
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# v2 = [10,25,8,60,20,80]
# bar = Bar('柱状信息堆叠图')
# bar.add('商家A',attr,v1,is_stack = True)  #is_stack = True才表示堆叠在一起
# bar.add('商家B',attr,v2,is_stack = True)
# bar.render('./html/first03.html')

# # ■ 并列（柱形）图
# from pyecharts import Bar
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# v2 = [10,25,8,60,20,80]
# bar = Bar('标记线和标记示例')
# bar.add('商家A',attr,v1,mark_point = ['average'])     #标记点：商家A的平均值
# bar.add('商家B',attr,v2,mark_line = ['min','max'])    #标记线：商家B最小/最大值
# bar.render('./html/first04.html')

#  # 横向并列（柱形）图
# from pyecharts import Bar
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# v2 = [10,25,8,60,20,80]
# bar = Bar('X 轴与 Y 轴交换')
# bar.add('商家A',attr,v1)
# bar.add('商家B',attr,v2,is_convert = True)    # is_convert = True:X 轴与 Y 轴交换
# bar.render('./html/first04.html')

# ▶代码1：
# from pyecharts import Line
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# v2 = [10,25,8,60,20,80]
# line = Line('折线示例图')
# line.add('商家A',attr,v1,mark_point = ['average'])
# line.add('商家B',attr,v2,is_smooth = True, mark_line = ['max','average'])
# line.render('./html/first05.html')
# --------------------------------------------------------------
# ▶代码2：(定制折线图)
# from pyecharts import Line
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# v2 = [10,25,8,60,20,80]
# line = Line('折线示例图')
# line.add('商家A',attr,v1,
#     mark_point = ['average','max','min'],  #标注点：平均值，最大值，最小值
#     mark_point_symbol = 'diamond',         #标注点：钻石形状
#     mark_point_textcolor = '#40ff27')      #标注点：标注文本颜色
# line.add('商家B',attr,v2,mark_point = ['average','max','min'],
#     mark_point_symbol = 'arrow',
#     mark_point_symbolsize = 40)
# line.render('./html/line01.html')
# import os
# print(os.path.abspath(__file__))
# ▶代码3：(面积图)
from pyecharts import Line
attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
line = Line('折线面积示例图')
line.add('商家A',attr,v1,is_fill = True,
    line_opacity = 0.2,      #线条不透明度
    area_opacity = 0.4,
    symbol = None)
line.add('商家B',attr,v2,is_fill = True,
    line_color = '#000',     #黑色
    area_opacity = 0.3,      #填充不透明度
    is_smooth = True)
line.render('./html/area01.html')