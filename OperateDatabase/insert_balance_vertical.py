# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :insert_balance_vertical
# @Date     :2020/12/3 12:31 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from selectDataBase.select_balance_vertical import select_balance_vertical

print(select_balance_vertical("'balance_vertical'", "'ebitda'", 1, 2018))
