from pyecharts import WordCloud

name = [u'网络', u'数据分析.txt', u'hadoop', u'flask']
value = [10000, 6000, 4000, 3000]
wd = WordCloud(width=1300, height=620)
wd.add('', name, value, word_size_range=(20, 100))
wd.render()