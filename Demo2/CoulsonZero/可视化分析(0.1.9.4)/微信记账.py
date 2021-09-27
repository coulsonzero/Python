from pyecharts import Bar       #pip install pyecharts==0.1.9.4
bar = Bar("微信4月账单", "记账表")
bar.add("价格", ['花呗','三人聚餐','月基本支出',
               '购物','外卖','交通'],
        ['136','197','317',
         '472','155','91.46'], is_more_utils=True)
#'电商','转账-购物','购物(联盛-殷家畈-其他)','购物-万达华府'
#'￥79.7','￥196','440.85','￥45.15',
bar.show_config()
bar.render()