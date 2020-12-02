# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_power_weight
# @Date     :2020/12/2 8:55 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

db_username = 'root'
db_password = 'root1234'
db_name = 'grss'
db = pymysql.connect("localhost", db_username, db_password, db_name)

# cursor
cursor = db.cursor()

def select_power_weight():
    cursor.execute("select * from power_weight")
    power_weight_info = cursor.fetchall()[0]
    return power_weight_info


print(select_power_weight())
