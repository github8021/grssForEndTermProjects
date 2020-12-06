# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :Financial_sub_table
# @Date     :2020/12/5 21:43
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
财务总分表 计算并新增数据（财务汇总表）
"""
import pymysql

def insert_Financial_sub_table(company_id,company_years):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8'
    )
    cursor = db.cursor()
    for company_year in company_years:
        #gross_profit_margin 销售毛利率(%)
        cursor.execute("""select gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,
                          net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,sales_to_cash_ratio,
                          current_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,
                          per_capita_output_value,per_capita_salary,seaapor,meaapor,ebitda
                          from financial_score_summary 
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        a = cursor.fetchall()
        aa=list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute("""select gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,
                                  net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,sales_to_cash_ratio,
                                  current_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,
                                  per_capita_output_value,per_capita_salary,seaapor,meaapor,ebitda
                                  from power_weight""")
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        score=list()
        score1=aa[1]*bb[1]+aa[2]*bb[2]+aa[0]*bb[0]
        score2 = aa[3] * bb[3] + aa[4] * bb[4] + aa[5] * bb[5]+ aa[6] * bb[6]
        score3 = aa[7] * bb[7] + aa[8] * bb[8] + aa[9] * bb[9]
        score4 = aa[10] * bb[10] + aa[11] * bb[11] + aa[12] * bb[12]+ aa[13] * bb[13]+ aa[14] * bb[14]
        score5 = aa[15] * bb[15] + aa[16] * bb[16] + aa[17] * bb[17]+ aa[18] * bb[18]+ aa[19] * bb[19]
        score.append(score1)
        score.append(score2)
        score.append(score3)
        score.append(score4)
        score.append(score5)
        cursor.execute("""select profitability,growth_ability,operating_capacity,solvency,management_ability
                          from first_power_weight""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        total_score=score[0]*cc[0]+score[1]*cc[1]+score[2]*cc[2]+score[3]*cc[3]+score[4]*cc[4]
        cursor.execute("insert into total_financial_score(company_id,company_year) value (%s,%s)",
                       (company_id, company_year))
        cursor.execute("""UPDATE total_financial_score set score=%s  where company_id=%s and company_year=%s""",(
                total_score, company_id, company_year))
        db.commit()
    # 4. 关闭游标
    cursor.close()
    # 5. 关闭连接
    db.close()

insert_Financial_sub_table(1,[2018,2019])



























