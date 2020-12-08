# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :delete_Corresponding_by_sjw
# @Date     :2020/12/8 15:17
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

def delete_Corresponding_by_sjw_one(a):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute( """delete from corresponding_by_sjw where corresponding_id=%s""",(a))
    db.commit()
#delete_Corresponding_by_sjw_one(6)

def delete_Corresponding_by_sjw_list(list):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.executemany( """delete from corresponding_by_sjw where corresponding_id=(%s)""",list)
    db.commit()
#delete_Corresponding_by_sjw_list([])