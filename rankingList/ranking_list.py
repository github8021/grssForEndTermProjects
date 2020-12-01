# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :ranking_list
# @Date     :2020/12/1 19:28
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql


def select_ranking_list_by_year(year, start, end):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    sql = """select * from total_financial_score
            where company_year=%s
            order by score desc
            limit %s,%s"""
    cur.execute(sql, (year, start, end))
    value = cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    return value


print(select_ranking_list_by_year(2018, 1, 3))
