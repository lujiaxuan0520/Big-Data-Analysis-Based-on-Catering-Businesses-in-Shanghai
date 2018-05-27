#!/usr/bin/python
#encoding=utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
def main():
    # Pie chart
    labels = ['没有评分数值的数据', '拥有评分数值的数据']
    sizes = [47758,132851]
    explode = (0.1, 0)
    fig1, ax1 = plt.subplots()
    p=ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90,pctdistance=0.65)
    ax1.axis('equal')
    plt.tight_layout()
    for front in p[1]:
        front.set_fontproperties(mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\STXINGKA.TTF'))
    plt.savefig('无score数据占比.png')
    plt.show()
    
if __name__=='__main__':
    main()