from pyecharts import Map
'''
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg

'''

value = [120, 110, 130]
attr = ['江西', '北京', '上海']
map = Map('Map 结合 VisualMap 实例', width=800, height=400)
map.add('', attr, value, maptype='china',
        is_visualmap=True, visual_text_color='#000')
map.render()