# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_First_power_weight
# @Date     :2020/12/5 17:39
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
数据库新建一级指标权重表（能力权重），并写查询、新增和修改接口，并自行插入数据
"""
import pymysql
#查询接口
def select_First_power_weight():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    cursor.execute("""select profitability,growth_ability,operating_capacity,solvency,management_ability
                          from first_power_weight""")
    a = cursor.fetchall()
    aa = list()
    for i in a:
        for j in i:
            aa.append(j)
    print(aa)
    db.rollback()
#select_First_power_weight()

# 新增接口
def insert_First_power_weight(profitability,growth_ability,operating_capacity,solvency,management_ability):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    list=(profitability,growth_ability,operating_capacity,solvency,management_ability)
    sql="""insert into  first_power_weight(profitability,growth_ability,operating_capacity,solvency,management_ability)
                      value (%s,%s,%s,%s,%s)"""
    cursor.execute(sql,list)
    db.commit()
    db.rollback()
#insert_First_power_weight(0.3,0.15,0.25,0.1,0.2)

#修改接口
def updata_First_power_weight(profitability,growth_ability,operating_capacity,solvency,management_ability):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    list=(profitability,growth_ability,operating_capacity,solvency,management_ability)
    sql="""UPDATE first_power_weight set profitability=%s,growth_ability=%s,operating_capacity=%s,
                                         solvency=%s,management_ability=%s"""
    cursor.execute(sql, list)
    db.commit()
    db.rollback()
updata_First_power_weight(0.15,0.15,0.25,0.25,0.2)










































































