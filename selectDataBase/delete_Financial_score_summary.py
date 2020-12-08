# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :delete_Financial_score_summary
# @Date     :2020/12/8 17:40
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

def delete_Financial_score_summary_one(a):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute( """delete from financial_score_summary where financial_score_summary_id=%s""",(a))
    db.commit()
#delete_Financial_score_summary_one(6)

def delete_Financial_score_summary_list(list):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.executemany("""delete from financial_score_summary where financial_score_summary_id=(%s)""",list)
    db.commit()
#delete_Financial_score_summary_list([])