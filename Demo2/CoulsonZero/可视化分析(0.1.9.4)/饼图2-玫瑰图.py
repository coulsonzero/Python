from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
# 标题，title_pos调整标题位置，title_text_size调整主标题文字大小
pie = Pie("饼图实例2-玫瑰图示例", title_pos='center', width=900, title_text_size=40)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[
        30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[
        30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
pie.show_config()
pie.render()
