#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import xlrd
def main():
    data=xlrd.open_workbook('上海_美食3.xlsx')
    table = data.sheets()[0]
    shopId=(table.col_values(0))[1:]
    shopName=pd.Series((table.col_values(1))[1:],index=shopId)
    dist_id=pd.Series((table.col_values(3))[1:],index=shopId)
    bizReg_id=pd.Series((table.col_values(5))[1:],index=shopId)
    geoLat=pd.Series((table.col_values(7))[1:],index=shopId)
    geoLng=pd.Series((table.col_values(8))[1:],index=shopId)
    midCategory_id=pd.Series((table.col_values(10))[1:],index=shopId)
    avgPrice=pd.Series((table.col_values(11))[1:],index=shopId)
    shopPower=pd.Series((table.col_values(12))[1:],index=shopId)
    avg_score=pd.Series((table.col_values(17))[1:],index=shopId)
    popularity=pd.Series((table.col_values(21))[1:],index=shopId)
    hasBookSetting=pd.Series((table.col_values(26))[1:],index=shopId)
    hasShortDeals=pd.Series((table.col_values(27))[1:],index=shopId)
    hasTakeAway=pd.Series((table.col_values(28))[1:],index=shopId)
    branchTotal=pd.Series((table.col_values(29))[1:],index=shopId)
    allData=pd.DataFrame({'a.shopName':shopName,'b.dist_id':dist_id,'c.bizReg_id':bizReg_id,'d.geoLat':geoLat,
                          'e.geoLng':geoLng,'f.midCategory_id':midCategory_id,'g.avgPrice':avgPrice,
                          'h.shopPower':shopPower,'i.popularity':popularity,'j.hasBookSetting':hasBookSetting,
                          'k.hasShortDeals':hasShortDeals,'l.hasTakeAway':hasTakeAway,'m.branchTotal':branchTotal,
                          'n.avg_score':avg_score})
    # columns=['shopName','dist_id','bizReg_id','geoLat','geoLng','midCategory_id','avgPrice'
    #          ,'shopPower','popularity','hasBookSetting','hasShortDeals','hasTakeAway','branchTotal',
    #          'avg_score' ]
    # writer=pd.ExcelWriter('Output.xlsx')
    # allData.to_excel(writer,'Sheet1')
    # writer.save()

    # result=allData.corr()
    # writer=pd.ExcelWriter('corr.xlsx')
    # result.to_excel(writer,'Sheet1')
    # writer.save()


if __name__=='__main__':
    main()