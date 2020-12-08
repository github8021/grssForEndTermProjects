# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :delete_Supplementary_data
# @Date     :2020/12/8 18:03
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

def delete_Supplementary_data_one(a):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute( """delete from supplementary_data where supplementary_data_id=%s""",(a))
    db.commit()
#delete_Supplementary_data_one(6)

def delete_Supplementary_data_list(list):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.executemany("""delete from supplementary_data where supplementary_data_id=(%s)""",list)
    db.commit()
#delete_Supplementary_data_list([])