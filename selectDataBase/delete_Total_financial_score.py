# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :delete_Total_financial_score
# @Date     :2020/12/8 18:05
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

def delete_Total_financial_score_one(a):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute( """delete from total_financial_score where total_financial_score_id=%s""",(a))
    db.commit()
#delete_Total_financial_score_one(6)

def delete_Total_financial_score_list(list):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.executemany("""delete from total_financial_score where total_financial_score_id=(%s)""",list)
    db.commit()
#delete_Total_financial_score_list([])