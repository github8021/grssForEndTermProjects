# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_company
# @Date     :2020/12/2 8:25 下午
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


def select_company_by_id(company_id):
    cursor.execute("select company_name from company where company_id=%d" % (company_id))
    company_name = cursor.fetchone()[0]
    return company_name


def select_company_by_name(company_name):
    cursor.execute("select company_id from company where company_name=%s" % (company_name))
    company_id = cursor.fetchone()[0]
    return company_id


# 注意传参数时的格式 写在 "'   (company_name)   '"中

# print(select_company_by_name("'兔宝宝'"))
