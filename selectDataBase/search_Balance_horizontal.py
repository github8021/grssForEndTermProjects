# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Balance_horizontal
# @Date     :2020/12/1 15:46
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询二级指标——横向差额表
import pymysql

def search_Balance_horizontal(company_id,company_years):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    for company_year in company_years:
        cursor.execute("""select gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,
                          net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,current_ratio,
                          sales_to_cash_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,
                          per_capita_output_value,per_capita_salary,seaapor,meaapor,ebitda
                          from balance_horizontal
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        print(result)
        db.commit()

search_Balance_horizontal(1,[2018,2019])
