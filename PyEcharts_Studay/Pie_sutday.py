# add(name,attr,value,radius = None,center = None,rosetype = None,**kwargs)
# attr:属性名称
# radius：饼图半径，数组第一项是内径，第二项是外径，默认[0,75,],设置成百分比
# center：圆心，数组第一项是X轴，第二项是Y轴，默认[50,50]
# rosetype: 是否展示成南丁格尔图，用过半径区分数据大小，radius和area两种模式，默认radius

# ▶代码1：(饼图)
# from pyecharts import Pie
#
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,75,90]
# pie = Pie('饼图示例')
# pie.add('',attr,v1,is_label_show = True)
# pie.render('./html/pie01.html')
# ▶代码2：(环形图)
from pyecharts import Pie

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
pie = Pie('饼图-环形图示例',title_pos = 'center')
pie.add(
        '',attr,v1,                 #''：图例名（不使用图例）
        radius = [40,75],           #环形内外圆的半径
        is_label_show = True,       #是否显示标签
        label_text_color = None,    #标签颜色
        legend_orient = 'vertical', #图例垂直
        legend_pos = 'left'
        )
pie.render('./html/pie02.html')