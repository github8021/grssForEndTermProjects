# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :Financial_summary_table
# @Date     :2020/12/3 21:53
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
财务汇总表 计算并新增数据（通过横向评分表和纵向评分表）
备注：财务汇总表的次一级指标是通过横纵差额表，一级指标是通过次一级指标
"""
import pymysql

def insert_Financial_summary_table(company_id,company_years):
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
        #gross_profit_margin 销售毛利率(%)
        cursor.execute("""select gross_profit_margin from score_horizontal where company_id=%s and company_year=%s""",(
            company_id, company_year))
        a = cursor.fetchall()
        aa=list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute("select gross_profit_margin from score_longitudinal where company_id=%s and company_year=%s""", (
        company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute("""select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='gross_profit_margin'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        cursor.execute("insert into financial_score_summary(company_id,company_year) value (%s,%s)",
                           (company_id, company_year))
        cursor.execute("""UPDATE  financial_score_summary set gross_profit_margin=%s  where company_id=%s and company_year=%s""",(
            result,company_id, company_year))

        #sales_margin 销售净利率(%)
        cursor.execute("""select sales_margin from score_horizontal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute("select sales_margin from score_longitudinal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='sales_margin'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        #print(result)
        cursor.execute("""UPDATE  financial_score_summary set sales_margin=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #roe 净资产收益率
        cursor.execute("""select roe from score_horizontal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute("select roe from score_longitudinal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='roe'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE  financial_score_summary set roe=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #mbigr 主营业务收入增长率(%)
        cursor.execute("select mbigr from score_longitudinal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            """select power_longitudinal from index_weight_table where primary_indicators='mbigr'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item]
        # print(result)
        cursor.execute(
            """UPDATE  financial_score_summary set mbigr=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #net_profit_growth_rate 净利润增长率(%)
        cursor.execute("select net_profit_growth_rate from score_longitudinal where company_id=%s and company_year=%s""", (
            company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            """select power_longitudinal from index_weight_table where primary_indicators='net_profit_growth_rate'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set net_profit_growth_rate=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #net_assets_growth_rate 净资产增长率(%)
        cursor.execute(
            "select net_assets_growth_rate from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            """select power_longitudinal from index_weight_table where primary_indicators='net_assets_growth_rate'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set net_assets_growth_rate=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #rdiaapor 研发投入占收比
        cursor.execute(
            "select rdiaapor from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            """select power_firm from index_weight_table where primary_indicators='rdiaapor'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set rdiaapor=%s  where company_id=%s and company_year=%s""",(
                result, company_id, company_year))

        #artd 应收账款周转天数(天)
        cursor.execute(
            """select artd from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select artd from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='artd'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set artd=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #inventory_turnover_days 存货周转天数(天)
        cursor.execute(
            """select inventory_turnover_days from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select inventory_turnover_days from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='inventory_turnover_days'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set inventory_turnover_days=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #sales_to_cash_ratio 销售收现比
        cursor.execute(
            """select sales_to_cash_ratio from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select sales_to_cash_ratio from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='sales_to_cash_ratio'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set sales_to_cash_ratio=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #current_ratio 流动比率
        cursor.execute(
            """select current_ratio from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select current_ratio from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='current_ratio'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set current_ratio=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #quick_ratio 速动比率
        cursor.execute(
            """select quick_ratio from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select quick_ratio from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='quick_ratio'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set quick_ratio=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #interest_payment_multiple 利息支付倍数
        cursor.execute(
            """select interest_payment_multiple from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select interest_payment_multiple from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='interest_payment_multiple'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set interest_payment_multiple=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #assets_and_liabilities 资产负债率(%)
        cursor.execute(
            """select assets_and_liabilities from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select assets_and_liabilities from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_firm from index_weight_table where primary_indicators='assets_and_liabilities'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set assets_and_liabilities=%s  where company_id=%s and company_year=%s""", (
                result, company_id, company_year))

        #cash_short_debt_ratio 现金短债比
        cursor.execute(
            """select cash_short_debt_ratio from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select cash_short_debt_ratio from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='cash_short_debt_ratio'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set cash_short_debt_ratio=%s  where company_id=%s and company_year=%s""",(
                result, company_id, company_year))

        #per_capita_output_value 人均产值
        cursor.execute(
            """select per_capita_output_value from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select per_capita_output_value from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='per_capita_output_value'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set per_capita_output_value=%s  where company_id=%s and company_year=%s""",(
                result, company_id, company_year))

        #per_capita_salary 人均薪酬
        cursor.execute(
            """select per_capita_salary from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select per_capita_salary from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='per_capita_salary'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set per_capita_salary=%s  where company_id=%s and company_year=%s""",
            (
                result, company_id, company_year))

        #seaapor 销售费用占收比
        cursor.execute(
            """select seaapor from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select seaapor from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='seaapor'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set seaapor=%s  where company_id=%s and company_year=%s""",
            (
                result, company_id, company_year))

        #meaapor 管理费用占收比
        cursor.execute(
            """select meaapor from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select meaapor from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='meaapor'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set meaapor=%s  where company_id=%s and company_year=%s""",
            (
                result, company_id, company_year))

        #ebitda EBITDA占收比
        cursor.execute(
            """select ebitda from score_horizontal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        a = cursor.fetchall()
        aa = list()
        for i in a:
            for j in i:
                aa.append(j)
        cursor.execute(
            "select ebitda from score_longitudinal where company_id=%s and company_year=%s""", (
                company_id, company_year))
        b = cursor.fetchall()
        bb = list()
        for i in b:
            for j in i:
                bb.append(j)
        cursor.execute(
            """select power_horizontal,power_longitudinal from index_weight_table where primary_indicators='ebitda'""")
        c = cursor.fetchall()
        cc = list()
        for i in c:
            for j in i:
                cc.append(j)
        for item in range(len(aa)):
            result = cc[0] * aa[item] + cc[1] * bb[item]
        # print(result)
        cursor.execute(
            """UPDATE financial_score_summary set ebitda=%s  where company_id=%s and company_year=%s""",(
                result, company_id, company_year))
        db.commit()
    # 4. 关闭游标
    cursor.close()
    # 5. 关闭连接
    db.close()
insert_Financial_summary_table(1,[2018,2019])
