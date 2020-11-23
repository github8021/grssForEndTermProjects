# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :excel_to_sql
# @Date     :2020/11/23 5:08 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd
from sqlalchemy import create_engine

files_path = ['./Documents/final_basis_assets.xls',
              './Documents/final_basis_cash.xls',
              './Documents/final_basis_profit.xls']

df1 = pd.read_excel(files_path[0])
df2 = pd.read_excel(files_path[1])
df3 = pd.read_excel(files_path[2])

engine = create_engine("mysql+mysqlconnector://root:root1234@127.0.0.1:3306/dymtest", echo=False)

df1.to_sql(name='basis_assets', con=engine, if_exists='replace', index='basis_assets_id')
df2.to_sql(name='basis_cash', con=engine, if_exists='replace', index='basis_cash_id')
df2.to_sql(name='basis_profit', con=engine, if_exists='replace', index='basis_profit_id')
print(engine.execute("show create table basis_assets").first()[1])
print(engine.execute("show create table basis_cash").first()[1])
print(engine.execute("show create table basis_profit").first()[1])
print('Done!')
