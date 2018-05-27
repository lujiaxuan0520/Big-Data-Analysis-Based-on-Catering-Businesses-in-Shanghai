#!/usr/bin/python
#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
labels = ['一般', '非常好', '好', '很好','尚可','差']
fracs = [25837,577,5367,2883,49156,165]
# explode = [0, 0, 0, 0]  # 0.1 凸出这部分
plt.figure(figsize=(9,6))
plt.axes(aspect=1)
p=plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.75)
for front in p[1]:
    front.set_fontproperties(mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINGKA.TTF'))
plt.savefig('餐馆评分等级的饼图.png')
plt.show()