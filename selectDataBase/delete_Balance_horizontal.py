# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :delete_Balance_horizontal
# @Date     :2020/12/8 14:51
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

def delete_Balance_horizontal_one(a):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute( """delete from balance_horizontal where balance_horizontal_id=%s""",(a))
    db.commit()
#delete_Balance_horizontal_one(1)

def delete_Balance_horizontal_list(list):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.executemany( """delete from balance_horizontal where balance_horizontal_id=(%s)""",list)
    db.commit()
#delete_Balance_horizontal_list([1]])