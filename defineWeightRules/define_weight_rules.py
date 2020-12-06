# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :define_weight_rules
# @Date     :2020/12/6 15:08
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""

import pymysql


def insert_and_define_a_rules(gross_profit_margin, sales_margin, roe, mbigr, net_profit_growth_rate,
                              net_assets_growth_rate, rdiaapor, artd, inventory_turnover_days, sales_to_cash_ratio,
                              current_ratio, quick_ratio, interest_payment_multiple, assets_and_liabilities,
                              cash_short_debt_ratio, per_capita_output_value, per_capita_salary, seaapor, meaapor,
                              ebitda):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = """INSERT INTO power_weight(gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,sales_to_cash_ratio,current_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,per_capita_output_value,per_capita_salary,seaapor,meaapor,ebitda)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        cur.execute(sql, (
            gross_profit_margin, sales_margin, roe, mbigr, net_profit_growth_rate, net_assets_growth_rate, rdiaapor,
            artd,
            inventory_turnover_days, sales_to_cash_ratio, current_ratio, quick_ratio, interest_payment_multiple,
            assets_and_liabilities, cash_short_debt_ratio, per_capita_output_value, per_capita_salary, seaapor, meaapor,
            ebitda))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()


# insert_and_define_a_rules(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)

def update_and_define_a_rules(**identifier):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = "update power_weight set "
    i = 1
    words=[]
    for key, value in identifier.items():
        if (i != len(identifier)):
            sql = sql + str(key) + "=%s , "
        else:
            sql = sql + str(key) + "=%s"
        words.append(value)
        i += 1
    try:
        cur.execute(sql, words)
        db.commit()

    except Exception as e:
        print("修改数据库失败", e)
    cur.close()
    db.close()


update_and_define_a_rules(roe=0.3, artd=0.4)
