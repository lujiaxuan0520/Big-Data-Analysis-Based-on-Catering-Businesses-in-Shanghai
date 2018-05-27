#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import xlrd
import re
def main():
    data=xlrd.open_workbook('上海_美食3.xlsx')
    table = data.sheets()[0]
    dishTag =(table.col_values(19))[1:]
    dishTags = (table.col_values(20))[1:]
    s_dishTag=",".join(dishTag)
    f=open('words1.txt','w')
    f.write(s_dishTag)
    f.close()

    fp=open('words2.txt','a',encoding="utf-8")
    for item in dishTags:
        if item:
            s=""
            words = re.split(r',[0-9]+\|', item)
            for i in words:
                if i:
                    s+=i
                    s+=','
            fp.write(s)
            fp.write(',')

if __name__=='__main__':
    main()