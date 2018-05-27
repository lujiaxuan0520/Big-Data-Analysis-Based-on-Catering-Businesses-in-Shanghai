#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12, 6))
n = 10
X = np.arange(n) + 1
# set_matplot_zh_font()

Y= [18.00699301,14.94755245,12.20862471,6.876456876,5.477855478,4.924242424,4.836829837,4.691142191,
    4.516317016,3.583916084]
p=plt.bar(X, Y, width=0.7, facecolor='y', edgecolor='white')
# width:柱的宽度
# 水平柱状图plt.barh，属性中宽度width变成了高度height
# 打两组数据时用+
# facecolor柱状图里填充的颜色
# edgecolor是边框的颜色
# 想把一组数据打到下边，在数据前使用负号
# plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
# 给图加text
str="西餐 日本菜 火锅 面包甜点 咖啡厅 本帮江浙菜 烧烤 粤菜 川菜 其他美食"
xlabel=str.split(" ")
for x, y in zip(X, Y):
    plt.text(x , y, '%.1f%%' % y, ha='center', va='bottom')
plt.ylabel('百分比（%）')
plt.title('评分在8.5以上的餐馆菜类类型（前10）')
plt.ylim(+0, +20)#显示的高度范围
# for front in p[1]:
#     front.set_fontproperties(mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINGKA.TTF'))

plt.xticks(X,xlabel)
plt.savefig('优秀餐馆所属类型前10柱状图.png')
plt.show()
