#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import xlrd

excel_path = 'Output.xlsx'
data= pd.read_excel(excel_path, sheet_name='Sheet1')
avg_score=np.array(data['n.avg_score'])
mean=avg_score.mean()
std=avg_score.std()

sns.set_palette("hls")
mpl.rc("figure", figsize=(9, 5))
data = avg_score
p=sns.distplot(data,color='b',axlabel='Avg_score')
sns.mpl.pyplot.ylabel('Frequency')
sns.mpl.pyplot.savefig('餐馆评分的概率分布图.png')
sns.mpl.pyplot.show()
