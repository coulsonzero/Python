"""
@author: coulson
@version: 2021/7/23  14:46
"""


import time
from tqdm import tqdm

a = []
for i in tqdm(range(5000)):
   # 模拟你的任务
   time.sleep(0.001)
   # a.append(i)

print("Finished!")

