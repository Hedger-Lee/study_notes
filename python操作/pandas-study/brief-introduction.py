"""
对pandas的简单入门学习
"""
import numpy as np
import pandas as pd

# 生成Series对象
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# 生成时间格式的索引标签
dates = pd.date_range('20130101', periods=6)
# print(dates)
# print(np.random.randn(6, 4))  # 生成6行，每行4个，都是0到1的浮点数
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)
