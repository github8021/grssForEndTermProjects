# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :processDocuments
# @Date     :2020/11/23 3:44 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd

files_path = ['./Documents/basis_assets.xls',
              './Documents/basis_cash.xls',
              './Documents/basis_profit.xls']

df1 = pd.read_excel(files_path[0])
df2 = pd.read_excel(files_path[1])
df3 = pd.read_excel(files_path[2])

df1 = df1.drop(19700101, 1)
df1 = df1.drop(20050630, 1)
df1 = df1.drop(20050930, 1)
df2 = df2.drop(19700101, 1)
df2 = df2.drop(20050630, 1)
df2 = df2.drop(20050930, 1)
df3 = df3.drop(19700101, 1)
df3 = df3.drop(20040630, 1)
df3 = df3.drop(20040930, 1)
df3 = df3.drop(20050331, 1)
df3 = df3.drop(20050630, 1)
df3 = df3.drop(20050930, 1)

for year in range(2006, 2021):
    df1 = df1.drop(int('{}0930'.format(year)), 1)
    df1 = df1.drop(int('{}0630'.format(year)), 1)
    df1 = df1.drop(int('{}0331'.format(year)), 1)
    df2 = df2.drop(int('{}0930'.format(year)), 1)
    df2 = df2.drop(int('{}0630'.format(year)), 1)
    df2 = df2.drop(int('{}0331'.format(year)), 1)
    df3 = df3.drop(int('{}0930'.format(year)), 1)
    df3 = df3.drop(int('{}0630'.format(year)), 1)
    df3 = df3.drop(int('{}0331'.format(year)), 1)
df1 = df1.T
df2 = df2.T
df3 = df3.T
df1.to_excel('./Documents/new_basis_assets.xls', index=True)
df2.to_excel('./Documents/new_basis_cash.xls', index=True)
df3.to_excel('./Documents/new_basis_profit.xls', index=True)
print('Done!')
