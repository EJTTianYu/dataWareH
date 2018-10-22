#coding=utf-8

import pandas as pd
import numpy as np

df=pd.read_csv('/Users/tianyu/PycharmProjects/dataWareH/venv/csvPre/trans.csv',sep=',')
#用于测试主键是否重复
print(len(df['trans_id'].unique())==len(df['trans_id']))
