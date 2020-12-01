# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Basis_cash
# @Date     :2020/12/1 14:08
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询基础表——基础现金表
import pymysql

def search_Basic_cash(company_id,company_years):
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
        cursor.execute("""select crfsgapls,tax_refund,ocrrtoa,socifoa,cpfpgarls,
                          cptfe,various_taxes_paid,oprtoa,socofoa,ncffoa,
                          crfi,crfii,ncrfdofaiaaolta,ncrfdosaobu,ocrrtia,
                          soifia,cpftpacofaiaaolta,cash_paid_for_investment,otncpbsaobu,ocprtia,
                          socofia,ncffia,acrfi,icrbsfamsi,gcrfb,
                          crfiob,rocrtfa,sociffa,cpfdr,cpfdodpoip,
                          idappbstms,pocrtfa,socoffa,ncfffa,eotcotexrocate,
                          niicace,abocaceatbotp,bocaceateotp,net_profit,minority_interests,
                          unrecognized_investment_loss,impairment_of_assets,dofadooagadopm,amortization_of_intangible_assets,aoltde,
                          rope,increase_accrued_expenses,lodofaiaaolta,lfsfa,lfcifv,
                          increase_in_deferred_revenue,estimated_liabilities,financial_expenses,investment_loss,decrease_deferred_income,
                          iiditl,decrease_in_inventory,decrease_in_operating_receiv,ables,increase_in_operating_payables,reduction_completed_unsettled_payments,
                          increase_settled_unfinished_payment,other,from_operating_activities,conversion_of_debt_capital,ccbdwoy,
                          flofa,ending_balance_of_cash,opening_balance_of_cash,ending_balance_cash_equivalents,opening_balance_cash_equivalents,
                          cash_and_cash_equivalents
                          from basis_cash
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()
        print(result)

search_Basic_cash(1,[2018,2019])
