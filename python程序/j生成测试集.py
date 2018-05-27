#!/usr/bin/python
#coding=utf-8
import xlrd
import numpy as np
import random
if __name__=='__main__':
    data = xlrd.open_workbook('训练集.xlsx')
    table = data.sheets()[0]
    input_arr = np.array([None, None, None, None, None, None, None, None, None])
    output_arr = np.array([None])
    for j in range(10000):
        i=random.randint(1,50256)
        geoLat = table.cell(i, 6).value
        geoLng = table.cell(i, 7).value
        avgPrice = table.cell(i, 10).value
        shopPower = table.cell(i, 11).value
        popularity = table.cell(i, 13).value
        hasBookSetting = table.cell(i, 14).value
        hasShortDeals = table.cell(i, 15).value
        hasTakeAway = table.cell(i, 16).value
        branchTotal = table.cell(i, 17).value
        avg_score = table.cell(i, 12).value
        row = np.array(
            [geoLat, geoLng, avgPrice, shopPower, popularity, hasBookSetting, hasShortDeals, hasTakeAway, branchTotal])
        input_arr = np.row_stack((input_arr, row))
        output_arr = np.row_stack((output_arr, [avg_score]))
    input_arr = np.delete(input_arr, 0, 0)  # 删除第一行
    output_arr = np.delete(output_arr, 0, 0)
    np.savetxt("测试集input_arr.txt",input_arr)
    np.savetxt("测试集output_arr.txt",output_arr)

