# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Basic_assets
# @Date     :2020/12/1 11:38
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询基础表——基础资产表
import pymysql

def search_Basic_index_table(company_id,company_years):
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
        cursor.execute("""select current_assets,money_funds,transactional_financial_assets,derivative_financial_assets,notes_receivable_accounts_receivable
                          bill_receivable,accounts_receivable,receivable_financing,prepayments,other_receivables,
                          interest_receivable,dividend_receivable,bfaura,stock,diahfs,
                          ncadwoy,prepaid_expenses,pcagal,other_current_assets,other_current_assets,
                          total_current_assets,non_current_assets,loans_and_advances,available_sale_financial_assets,held_to_maturity_investments,
                          long_term_receivables,long_term_equity_investment,Investment_real_estate,construction_in_progress,engineer_material,
                          fixed_assets_and_liquidation,net_fixed_assets,fixed_assets_liquidation,productive_biological_assets,public_welfare_biological_assets,
                          oil_and_gas_asset,right_of_use_asset,intangible_assets,development_expenditure,goodwill,
                          long_term_prepaid_expenses,deferred_tax_assets,other_non_current_assets,total_non_current_assets,total_assets,
                          current_liabilities,short_term_loan,transactional_financial_liabilities,notes_payable_accounts_payable,bills_payable,
                          accounts_payable,advance_receipt,fees_and_commissions,employee_compensation_payable,taxes_payable,other_payables_total,
                          interest_payable,dividend_payable,other_payables,accrued_fees,deferred_within_one_year,
                          short_term_bonds_payable,current_liabilities_one_year,other_current_liabilities,total_current_liabilities,non_current_liabilities
                          long_term_loan,bonds_payable,lease_liability,ltecp,long_term_payables,
                          special_payables,estimated_non_current_liabilities,deferred_income_tax_liabilities,long_term_deferred_income,other_non_current_liabilities,
                          total_non_current_liabilities,total_liabilities,owners_equity,paid_in_capital_or_equity,capital_reserve,
                          less_treasury_stock,other_comprehensive_income,special_reserves,surplus_reserve,general_risk_preparation,
                          undistributed_profit,teatsotpc,toeose,tlaoeose
                          from basis_assets
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        print(result)
        db.commit()

search_Basic_index_table(1,[2018,2019])

























