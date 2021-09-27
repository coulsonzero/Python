# encoding: utf-8
import time
from pyecharts import Bar       #pip install pyecharts==0.1.9.4

v1 = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v2 = [5, 20, 36, 10, 75, 90]
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", v1, v2, is_more_utils=True)
bar.show_config()
bar.render()
