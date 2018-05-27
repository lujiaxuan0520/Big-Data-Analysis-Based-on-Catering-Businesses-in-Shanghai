#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(15, 6))
n = 17
X = np.arange(n) + 1
# set_matplot_zh_font()

Y= [7.52,7.5,7.38,7.33,7.3,7.3,7.29,7.25,7.25,7.25,7.22,7.21,7.21,7.21,7.15,7.14,7.13]
p=plt.bar(X, Y, width=0.7, facecolor='b', edgecolor='white')
xlabel=['卢湾区','静安区','长宁区','徐汇区','杨浦区','闵行区','黄浦区','浦东新区','闸北区','虹口区','普陀区','宝山区','松江区','嘉定区','青浦区','金山区','奉贤区']
for x, y in zip(X, Y):
    plt.text(x , y + 0.05, '%.2f' % y, ha='center', va='bottom')
plt.xlabel('区县')
plt.ylabel('餐馆均分')
plt.title('各区餐馆均分')
plt.ylim(+6.8, +7.8)#显示的高度范围

plt.xticks(X,xlabel)
plt.savefig('各区餐馆均分柱状图.png')
plt.show()
