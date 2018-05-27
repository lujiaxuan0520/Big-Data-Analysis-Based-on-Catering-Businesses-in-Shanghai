#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20, 6))
n = 20
X = np.arange(n) + 1
# set_matplot_zh_font()

Y= [164,130,116,114,107,106,92,85,77,76,73,67,64,63,58,57,56,52,51,47]
p=plt.bar(X, Y, width=0.7, facecolor='g', edgecolor='white')
# width:柱的宽度
# 水平柱状图plt.barh，属性中宽度width变成了高度height
# 打两组数据时用+
# facecolor柱状图里填充的颜色
# edgecolor是边框的颜色
# 想把一组数据打到下边，在数据前使用负号
# plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
# 给图加text
xlabel=['五角场/大学区','淮海路','静安寺','南京西路','虹桥镇','虹桥','中山公园','外滩','徐家汇','陆家嘴','打浦桥',
         '人民广场','八佰伴','七宝','漕河泾/田林','天山','世纪公园','金桥','新天地','大宁地区']
for x, y in zip(X, Y):
    plt.text(x , y + 0.05, '%.0f' % y, ha='center', va='bottom')
plt.ylabel('数量')
plt.title('各区域评分在8.5以上的餐馆数量（前20）')
plt.ylim(+20, +170)#显示的高度范围
# for front in p[1]:
#     front.set_fontproperties(mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINGKA.TTF'))

plt.xticks(X,xlabel)
plt.savefig('优秀餐馆所在区域前20柱状图.png')
plt.show()
