from pyecharts import Line
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True,
         line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000',
         area_opacity=0.3, is_smooth=True)
line.show_config()
line.render()
