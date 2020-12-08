# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Financial_scoring_rules
# @Date     :2020/12/1 16:03
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询一级指标——评分规则表
import pymysql

def search_Financial_scoring_rules(company_id,company_years):
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
        cursor.execute("""select gross_profit_margin_up,gross_profit_margin_down,sales_margin_up,sales_margin_down,roe_up,
                          roe_down,mbigr_up,mbigr_down,net_profit_growth_rate_up,net_profit_growth_rate_down,
                          net_assets_growth_rate_up,net_assets_growth_rate_down,rdiaapor_up,rdiaapor_down,artd_up,
                          artd_down,inventory_turnover_days_up,inventory_turnover_days_down,sales_to_cash_ratio_up,sales_to_cash_ratio_down,
                          current_ratio_up,current_ratio_down,quick_ratio_up,quick_ratio_down,interest_payment_multiple_up,
                          interest_payment_multiple_down,assets_and_liabilities_up,assets_and_liabilities_down,cash_short_debt_ratio_up,cash_short_debt_ratio_down,
                          per_capita_output_value_up,per_capita_output_value_down,per_capita_salary_up,per_capita_salary_down,seaapor_up,
                          seaapor_down,meaapor_up,meaapor_down,ebitda_up,ebitda_down,
                          power_horizontal,score,power_longitudinal,power_firm
                          from financial_scoring_rules
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        a.append(result)
    #print(a)
    return a

search_Financial_scoring_rules(1,[2018,2019])
