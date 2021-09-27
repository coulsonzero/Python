from pyecharts import Gauge
gauge = Gauge('今日加班概率')
gauge.add('', "可能性", 99.99, angle_range=[225, -45],
          scale_range=[0, 100], is_legend_show=False)
gauge.render()
gauge
