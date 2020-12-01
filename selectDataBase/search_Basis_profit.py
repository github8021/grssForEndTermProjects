# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Basis_cash
# @Date     :2020/12/1 14:00
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询基础表——基础利润表
import pymysql

def search_Basic_profit(company_id,company_years):
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
        cursor.execute("""select total_operating_income,operating_income,total_operating_costs,operating_costs，business_tax_and_surcharges，
                          sales_expense,management_costs,financial_expenses，rd_expenses，asset_impairment_loss，
                          lncome_changes_in_value,investment_income,iiifaajv,exchange_gains,operating_profit,
                          anoi,lnoe,llodonca,the_total_profit,deduct_income_tax_expense,
                          net_profit,trpbttpco,earnings_per_share，basic_earnings_per_share,diluted_earnings_per_share,
                          other_comprehensive_income,total_comprehensive_income,tciatootp,tciatms
                          from basis_profit
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        print(result)
        db.commit()

search_Basic_profit(1,[2018,2019])
