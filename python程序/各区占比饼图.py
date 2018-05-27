#!/usr/bin/python
#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
labels = [ '徐汇区', '静安区', '长宁区','浦东新区','黄浦区','普陀区','闸北区','虹口区',
    '杨浦区','闵行区','宝山区','松江区','嘉定区','其他（卢湾、青浦、奉贤、金山）']
fracs = [6077,2686,4579,17009,3548,4740,3592,3399,5058,9189,6091,5221,4591,8205]
# explode = [0, 0, 0, 0]  # 0.1 凸出这部分
plt.figure(figsize=(9,6))
plt.axes(aspect=1)
p=plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.75)
for front in p[1]:
    front.set_fontproperties(mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINGKA.TTF'))
plt.savefig('各区占比饼图.png')
plt.show()
