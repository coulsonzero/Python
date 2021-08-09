from icecream import ic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 折线图
df = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df['A'] = pd.Series(list(range(len(df))))
plt.figure()
df.plot(x='A')
ic(plt.show())

# 垂直柱状图
df = pd.DataFrame(np.random.rand(10, 4), columns=['a','b','c','d'])
df.plot(kind='bar')
ic(plt.show())

# 折叠水平柱状图
df.plot(kind='barh', stacked=True)
ic(plt.show())


# 散点图
df = pd.DataFrame({'height': [180, 170, 172, 183, 179, 178, 160],
                   'weight': [85, 80, 85, 75, 78, 70, 72]})
df.plot(x='height', y='weight', kind='scatter',
        marker='*', s=60, label='height-weight')
ic(plt.show())

'''
# 饼图
df = pd.DataFrame({'height':[180, 170, 172, 183, 179, 178, 160],
                   'weight': [85, 80, 85, 75, 78, 70, 72]})
df.plot(x='height', y='weight', kind='scatter',
        marker='*', s=60, label='height-weight')
df['weight'].plot(kind='pie', autopct='%.2f%%', labels=df['weight'].values,
                  shadow=True)
ic(plt.show())
'''

