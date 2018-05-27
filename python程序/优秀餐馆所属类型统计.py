#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import xlrd

def main():
    data=xlrd.open_workbook('上海_美食_优秀.xlsx')
    table = data.sheets()[0]
    Category =(table.col_values(9))[1:]
    Category_dict=dict()
    for i in Category:
        if i not in Category_dict:
            Category_dict[i]=0
        else:
            Category_dict[i]+=1
    x=pd.Series(Category_dict)
    writer=pd.ExcelWriter('优秀餐馆所属类型.xlsx')
    x.to_excel(writer,'Sheet1')
    writer.save()

if __name__=='__main__':
    main()