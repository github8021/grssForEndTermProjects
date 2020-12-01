# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_by_user
# @Date     :2020/12/1 20:32
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql


def select_corresponding_by_user(table, name):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    sql = """select * from corresponding_by_sjw 
    where attribute_inquired=%s and table_inquired=%s"""
    cur.execute(sql, (name, table))
    value = cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    return value


print(select_corresponding_by_user("total_financial_score", "score"))
