# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_field_translation
# @Date     :2020/12/2 8:36 下午
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


def select_trans_by_ch(table_ch, attribute_ch):
    cursor.execute(
        "select source_directory_english,english_name from field_translation where source_directory=%s and chinese_name=%s" % (
        table_ch, attribute_ch))
    english_info = cursor.fetchone()
    return english_info


def select_trans_by_eng(table_eng, attribute_eng):
    cursor.execute(
        "select source_directory,chinese_name from field_translation where source_directory_english=%s and english_name=%s" % (
        table_eng, attribute_eng))
    english_info = cursor.fetchone()
    return english_info

# 注意传参数时的格式 写在 "'   (company_name)   '"中

# print(select_trans_by_ch("'横向差额表'", "'销售毛利率'"))
# print(select_trans_by_eng("'balance_horizontal'", "'balance_horizontal_id'"))
