from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter('动态散点图示例')
es.add('effectScatter', v1, v2)
es.render()