# add(
#     name,attr,value,
#     maptype = 'china',
#     is_roam = True,
#     is_map_symobol_show = True
#     **kwargs
#     )
# maptype -> str: 地图类型，支持China，world，北京，天津，上海，湖南，湖北，……363个二线城市
# is_roam -> bool/str 是否开启鼠标缩放，漫游等，默认 True,
#                     若只想开启缩放/平移 设置scale/move 设置成 True 开启
# is_map_symobol_show 是否显示地图标记，默认 True。

# ▶代码1：
# from pyecharts import Map
# value = [155,10,66,78]
# attr = ['福建','山东','北京','上海']
# map = Map('全国地图示例',width = 1200,height = 600)
# map.add('',attr,value,maptype = 'china')
# map.render('./html/map01.html')

# ▶代码2：
from pyecharts import Map
value = [155,10,66,78]
attr = ['汕头市','汕尾市','揭阳市','肇庆市']
map = Map('广东地图示例',width = 1200,height = 600)
map.add('',attr,value,maptype = '广东',
        is_visualmap = True,
        visual_text_color = '#000',
        is_label_show = True
        )
map.render('./html/map02.html')
