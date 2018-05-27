#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import xlrd

def main():
    data=xlrd.open_workbook('上海_美食_优秀.xlsx')
    table = data.sheets()[0]
    bizReg =(table.col_values(4))[1:]
    Region_dict=dict()
    for i in bizReg:
        if i not in Region_dict:
            Region_dict[i]=0
        else:
            Region_dict[i]+=1
    x=pd.Series(Region_dict)
    writer=pd.ExcelWriter('优秀餐馆所属区域.xlsx')
    x.to_excel(writer,'Sheet1')
    writer.save()

if __name__=='__main__':
    main()