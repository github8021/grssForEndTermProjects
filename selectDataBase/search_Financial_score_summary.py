# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Financial_score_summary
# @Date     :2020/12/1 16:16
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询最终指标——财务汇总表
import pymysql

def search_Financial_score_summary(company_id,company_years):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    a = list()
    for company_year in company_years:
        cursor.execute("""select gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,
                          net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,sales_to_cash_ratio,
                          current_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,
                          per_capita_output_value,per_capita_salary,seaapor,meaapor,ebitda,
                          profitability,growth_ability,operating_capacity,solvency,management_ability
                          from financial_score_summary
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        a.append(result)
    #print(a)
    return a


search_Financial_score_summary(1,[2018,2019])
