#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2018/12/24 15:17
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import xlrd
import matplotlib.pyplot as plt
data = pd.read_excel('C:\\Users\\Administrator\\PycharmProjects\\data_clean\\info.xls')
s = DataFrame(data)
s = data.isnull().sum().sort_values(ascending=False)
s1 = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
#查看缺失百分比
new = pd.concat([s,s1], axis=1, keys=['s','s1'])
# 视觉上直观查看缺失值
import missingno
missingno.matrix(data)
datas = data.dropna(thresh=data.shape[0]*0.5,axis=1)
#如果某一行全部都是NAN才删除
s3 = data.dropna(axis=0,how='all')
#默认情况下只留没有空值的行
data = data.dropna(axis=0)
# 统计重复记录数
s4 = data.duplicated().sum()
#删除重复数据
data.drop_duplicates()
# 对连续型数据和离散型数据分开处理
col = data.columns
id_col=['汽车类型']
cat_col = ['汽车类型','最低价']
cont_col = ['汽车类型','最高价']
from matplotlib import pyplot as plt
for i in cat_col:
    # print(pd.Series(data[i].value_counts()))
    plt.plot(data[i])
var = '最高价'
data = pd.concat([data['最低价'], data[var]], axis=1)
data.plot.scatter(x=var, y='最低价', ylim=(0,300))

#print(Q)
