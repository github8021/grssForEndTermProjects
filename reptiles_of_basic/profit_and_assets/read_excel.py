# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :read_excel
# @Date     :2020/11/18 1:31 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd
import numpy as np
import pymysql
import datetime
from pandas.tests.io.excel.test_xlrd import xlrd

df=pd.DataFrame(pd.read_excel('/Users/inter.d/PycharmProjects/ShangKe/pa/TbbZcfz.xls',header=1))
print(df.iloc[0:11, 0:32])
# df = df.iloc[1:,0:]
# df = df.set_index('id')
# df.to_excel('/Users/inter.d/PycharmProjects/ShangKe/pa/TbbZcfz1.xls', sheet_name='mySheet')
# conn=pymysql.connect(host='localhost',user='root',password='root1234',
#                      db='grss',charset='utf8')
# cousor=conn.cursr()
# fname = "TbbXjll.xls"
# bk = xlrd.open_workbook(fname)
# sh = bk.sheets()[0]
# start_time = datetime.datetime.now()
# sql3 = ''
# for i in range(1,sh.nrows):
#     a = []
#     sql = '('
#     for j in range(sh.ncols):
#         sql += "'" + str(sh.cell(i,j).value)+"'"+','
#         sql2 = sql.strip(",")
#         sql3 += sql2.strip()+'),'
#         if i%1000==0:
#             sql3 = sql3.rstrip(",")
#             sql1 = "insert into Flow()"
