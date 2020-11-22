# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :study
# @File     :read_excel
# @Date     :2020/11/18 21:41
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import time

import pandas as pd
import MySQLdb

for y in range(2019,2007,-1):
    df = pd.DataFrame(pd.read_excel('D:\\Phthon\\study\\work\\Final assignment\\basis_cash.xls', header=1))#路径要改
    df = df.T
    db = MySQLdb.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',#密码
        db='grss',#库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    # 插入语句，这个要变
    sql1 = """insert into basis_cash(crfsgapls,tax_refund,ocrrtoa,socifoa,cpfpgarls,cptfe,various_taxes_paid,oprtoa,socofoa,ncffoa,
    crfi,crfii,ncrfdofaiaaolta,ncrfdosaobu,ocrrtia,soifia,cpftpacofaiaaolta,cash_paid_for_investment,otncpbsaobu,ocprtia,socofia,ncffia,
    acrfi,gcrfb,icrbsfamsi,crfiob,rocrtfa,sociffa,cpfdr,cpfdodpoip,idappbstms,pocrtfa,socoffa,ncfffa,eotcotexrocate,niicace,abocaceatbotp,bocaceateotp,
    net_profit,minority_interests,unrecognized_investment_loss,impairment_of_assets,dofadooagadopm,amortization_of_intangible_assets,aoltde,rope,increase_accrued_expenses,lodofaiaaolta,lfsfa,lfcifv,increase_in_deferred_revenue,estimated_liabilities,financial_expenses,investment_loss,decrease_deferred_income,iiditl,decrease_in_inventory,
    decrease_in_operating_receivables,increase_in_operating_payables,reduction_completed_unsettled_payments,increase_settled_unfinished_payment,other,from_operating_activities,conversion_of_debt_capital,ccbdwoy,flofa,ending_balance_of_cash,opening_balance_of_cash,ending_balance_cash_equivalents,opening_balance_cash_equivalents,cash_and_cash_equivalents,
    company_year)
              value( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s)
    """
    dict1 = list()
    num=int((2020-y)*4)
    #这个是分组做的，因为有空行之类的
    for i in range(1, 11):
        a = df.iloc[num, i]
        dict1.append(a)
    for i in range(12, 24):
        b = df.iloc[num, i]
        dict1.append(b)
    for i in range(25, 41):
        c = df.iloc[num, i]
        dict1.append(c)
    for i in range(42, 75):
        d = df.iloc[num, i]
        dict1.append(d)
    dict1.append(y)
    cursor.execute(sql1, dict1)
    # 提交到数据库执行
    db.commit()





































