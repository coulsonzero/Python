import pandas as pd
import numpy as np
from icecream import ic


score = np.random.randint(40, 100, (10, 5))
ic(score)

# pd.DataFrame(..., columns, index)
score_df = pd.DataFrame(score)
ic(score_df)

subjects = ["语", "数", "英", "政", "体"]
stu = ['同学' + str(i) for i in range(score_df.shape[0])]
data = pd.DataFrame(score, columns=subjects, index=stu)
ic(data)

stu = ['同学_' + str(i) for i in range(score_df.shape[0])]
data.index = stu
ic(data)


df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2016],
                   'sale': [60, 55, 40, 31]})
ic(df)
