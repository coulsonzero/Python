import numpy as np
from icecream import ic

a = np.array(([1,2,3],[4,5,6]))


b = np.array((1,2,3,4,56,7))


c= np.random.randint(40, 100, (10, 5))


d = np.array(([75, 58, 53, 77, 72],
              [62, 45, 79, 80, 82],
              [96, 52, 50, 95, 63]))
'''
科学计算
np.array(): 数组
np.random.ranint(start, end, seize=(...)): 生成矩阵
np.average(x, axis=1): 平均数
np.std(x): 标准差
np.var(x): 方差
np.max(x, axis=1): 最大值
np.sum(x): 和
np.sort(x): 排序
np.unique(x): 去重
np.bincount(x): 统计次数 
'''
if __name__ == '__main__':
    ic.disable()
    ic(a)
    ic(b)
    ic(c)
    ic(d.T)
    ic(np.average(d, axis=1))
    ic(np.max(d, axis=1))

    ic.enable()