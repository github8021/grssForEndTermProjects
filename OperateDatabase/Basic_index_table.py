# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :study
# @File     :Basic_index_table
# @Date     :2020/11/28 11:56
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#基础指标表
"""
1、销售毛利率=(基础利润表)营业收入-(基础利润表)营业成本/(基础利润表)营业收入;
2、销售净利率=(基础利润表)归属于母公司所有者的净利润/(基础利润表)营业收入;
3、净资产收益率=(基础利润表)归属于母公司所有者的净利润/(基础资产表)归属于母公司股东权益合计;
4、主营业务收入增长率=(基础利润表)当年营业收入-(基础利润表)去年营业收入/(基础利润表)去年营业收入;
5、净利润增长率=((基础利润表)当年归属于母公司所有者的净利润-(基础利润表)去年归属于母公司所有者的净利润)/(基础利润表)去年归属于母公司所有者的净利润;
6、净资产增长率=((基础资产表)当年归属于母公司股东权益合计-(基础资产表)去年归属于母公司股东权益合计)/(基础资产表)去年归属于母公司股东权益合计;
7、研发投入占收比=(基础利润表)研发费用/(基础利润表)营业收入;
8、应收账款周转天数=((基础资产表)当年应收账款+(基础资产表)去年应收账款)/2*365/(基础利润表)营业收入;
9、存货周转天数=(((基础资产表)当年存货+(基础资产表)去年存货))/2*365/（基础利润表）营业成本
10、销售收现比=(基础现金表)销售商品、提供劳务收到的现金/(基础利润表)营业收入
11、流动比率=(基础资产表) 流动资产合计/(基础资产表) 流动负债合计
12、速动比率=SUM((基础资产表)货币资金:买入返售金融资产)/(基础资产表)流动负债合计
13、利息支付倍数=((（基础利润表) 利润总额+ （辅助数据表）利息支出))/ （辅助数据表）利息支出
14、资产负债率=(基础资产表) 负债合计/(基础资产表) 资产总计
15、现金短债比=(基础现金表) 经营活动产生的现金流量净额/(基础资产表) 流动负债合计
16、人均产值=(基础利润表)营业收入/（辅助数据表）员工总数/10000
17、人均薪酬=(基础现金表) 支付给职工以及为职工支付的现金/ （辅助数据表）员工总数/10000
18、销售费用占收比=（基础利润表）销售费用/(基础利润表)营业收入
19、管理费用占收比=（基础利润表）管理费用/(基础利润表)营业收入
20、EBITDA占收比=(辅助数据表)EBITDA/(基础利润表)营业收入
"""
import pymysql
db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',#密码
        db='grss',#库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
cursor = db.cursor()
def Basic_index_table(company_id):
        for company_year in range(2018,2019):
                # 1、销售毛利率=(基础利润表)营业收入-(基础利润表)营业成本/(基础利润表)营业收入;
                cursor.execute("select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                     for j in i:
                          aa.append(j)
                cursor.execute("select operating_costs from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                     for j in i:
                          bb.append(j)
                gross_profit_margin = list()
                for i in range(len(aa)):
                        gross_profit_margin.append(aa[i] - (bb[i] / aa[i]))
                sql = """insert into basic_indicators(gross_profit_margin) VALUES (%s)"""
                cursor.execute(sql, gross_profit_margin)
                db.rollback()#db.commit()

                # 2、销售净利率=(基础利润表)归属于母公司所有者的净利润/(基础利润表)营业收入;
                cursor.execute("select trpbttpco from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                     for j in i:
                          aa.append(j)
                cursor.execute("select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                     for j in i:
                          bb.append(j)
                sales_margin = list()
                for i in range(len(aa)):
                     sales_margin.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(sales_margin) VALUES (%s)"""
                cursor.execute(sql, sales_margin)
                db.rollback()#db.commit()

                # 3、净资产收益率=(基础利润表)归属于母公司所有者的净利润/(基础资产表)归属于母公司股东权益合计;
                cursor.execute("select trpbttpco from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute("select teatsotpc from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                roe = list()
                for i in range(len(aa)):
                        roe.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(roe) VALUES (%s)"""
                cursor.execute(sql, roe)
                db.rollback()#db.commit()

                # 4、主营业务收入增长率=((基础利润表)当年营业收入-(基础利润表)去年营业收入)/(基础利润表)去年营业收入;
                cursor.execute(
                        "select operating_income from basis_profit where  company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year-1))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                mbigr = list()
                for i in range(len(aa)):
                        mbigr.append((aa[i] - bb[i]) / bb[i])
                sql = """insert into basic_indicators(mbigr) VALUES (%s)"""
                cursor.execute(sql, mbigr)
                db.rollback()#db.commit()

                # 5、净利润增长率=((基础利润表)当年归属于母公司所有者的净利润-(基础利润表)去年归属于母公司所有者的净利润)/(基础利润表)去年归属于母公司所有者的净利润;
                cursor.execute(
                        "select trpbttpco from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select trpbttpco from  basis_profit where company_id=%s and company_year=%s",(company_id,company_year-1))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                net_profit_growth_rate = list()
                for i in range(len(aa)):
                        net_profit_growth_rate.append((aa[i] - bb[i]) / bb[i])
                sql = """insert into basic_indicators(net_profit_growth_rate) VALUES (%s)"""
                cursor.execute(sql, net_profit_growth_rate)
                db.rollback()#db.commit()

                # 6、净资产增长率=((基础资产表)当年归属于母公司股东权益合计-(基础资产表)去年归属于母公司股东权益合计)/(基础资产表)去年归属于母公司股东权益合计;
                cursor.execute("select teatsotpc from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select teatsotpc from basis_assets where company_id=%s and company_year=%s",(company_id,company_year-1))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                net_profit_growth_rate = list()
                for i in range(len(aa)):
                        net_profit_growth_rate.append((aa[i] - bb[i]) / bb[i])
                sql = """insert into basic_indicators(net_profit_growth_rate) VALUES (%s)"""
                cursor.execute(sql, net_profit_growth_rate)
                db.rollback()#db.commit()

                # 7、研发投入占收比=(基础利润表)研发费用rd_expenses/(基础利润表)营业收入operating_income
                cursor.execute("select rd_expenses from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute("select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                rdiaapor = list()
                for i in range(len(aa)):
                        rdiaapor.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(rdiaapor) VALUES (%s)"""
                cursor.execute(sql, rdiaapor)
                db.rollback()#db.commit()

                # 8、应收账款周转天数=((基础资产表)当年应收账款+(基础资产表)去年应收账款)/2*365/(基础利润表)营业收入;
                cursor.execute(
                        "select accounts_receivable from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select accounts_receivable from basis_assets where company_id=%s and company_year=%s",(company_id,company_year-1))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                c = cursor.fetchall()
                cc = list()
                for i in c:
                        for j in i:
                                cc.append(j)
                accounts_receivable_turnover_days = list()
                for i in range(len(aa)):
                        accounts_receivable_turnover_days.append((aa[i] + bb[i]) / 2 * 365 / cc[i])
                sql = """insert into basic_indicators(accounts_receivable_turnover_days) VALUES (%s)"""
                cursor.execute(sql, accounts_receivable_turnover_days)
                db.rollback()#db.commit()

                # 9、存货周转天数=(((基础资产表)当年存货+(基础资产表)去年存货))/2*365/（基础利润表）营业成本
                cursor.execute("select stock from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute("select stock from basis_assets where company_id=%s and company_year=%s",(company_id,company_year-1))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                cursor.execute(
                        "select operating_costs from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                c = cursor.fetchall()
                cc = list()
                for i in c:
                        for j in i:
                                cc.append(j)
                inventory_turnover_days = list()
                for i in range(len(aa)):
                        inventory_turnover_days.append((aa[i] + bb[i]) / 2 * 365 / cc[i])
                sql = """insert into basic_indicators(inventory_turnover_days) VALUES (%s)"""
                cursor.execute(sql, inventory_turnover_days)
                db.rollback()#db.commit()

                # 10、销售收现比=(基础现金表)销售商品、提供劳务收到的现金/(基础利润表)营业收入
                cursor.execute("select crfsgapls from basis_cash where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                sales_to_cash_ratio = list()
                for i in range(len(aa)):
                        sales_to_cash_ratio.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(sales_to_cash_ratio) VALUES (%s)"""
                cursor.execute(sql, sales_to_cash_ratio)
                db.rollback()#db.commit()

                # 11、流动比率=(基础资产表) 流动资产合计/(基础资产表) 流动负债合计
                cursor.execute(
                        "select total_current_assets from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_current_liabilities from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                current_ratio = list()
                for i in range(len(aa)):
                        current_ratio.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(current_ratio) VALUES (%s)"""
                cursor.execute(sql, current_ratio)
                db.rollback()#db.commit()

                # 12、速动比率=SUM((基础资产表)货币资金:买入返售金融资产)/(基础资产表)流动负债合计
                cursor.execute("select bfaura from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_current_liabilities from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                quick_ratio = list()
                for i in range(len(aa)):
                        quick_ratio.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(quick_ratio) VALUES (%s)"""
                cursor.execute(sql, quick_ratio)
                db.rollback()#db.commit()

                # 13、利息支付倍数=((（基础利润表) 利润总额+ （辅助数据表）利息支出))/ （辅助数据表）利息支出
                cursor.execute(
                        "select the_total_profit from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select nterest_payments from supplementary_data where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                interest_payment_multiple = list()
                for i in range(len(aa)):
                        interest_payment_multiple.append((aa[i] + bb[i]) / bb[i])
                sql = """insert into basic_indicators(interest_payment_multiple) VALUES (%s)"""
                cursor.execute(sql, interest_payment_multiple)
                db.rollback()#db.commit()

                # 14、资产负债率=(基础资产表) 负债合计/(基础资产表) 资产总计
                cursor.execute(
                        "select total_liabilities from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_assets from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                assets_and_liabilities = list()
                for i in range(len(aa)):
                        assets_and_liabilities.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(assets_and_liabilities)VALUES (%s)"""
                cursor.execute(sql, assets_and_liabilities)
                db.rollback()#db.commit()

                # 15、现金短债比=(基础现金表) 经营活动产生的现金流量净额/(基础资产表) 流动负债合计
                cursor.execute("select ncffoa from basis_cash where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_current_liabilities from basis_assets where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                cash_short_debt_ratio = list()
                for i in range(len(aa)):
                        cash_short_debt_ratio.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(cash_short_debt_ratio) VALUES (%s)"""
                cursor.execute(sql, cash_short_debt_ratio)
                db.rollback()#db.commit()

                # 16、人均产值=(基础利润表)营业收入/（辅助数据表）员工总数/10000 def per_capita_output_value():
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_number_employees from supplementary_data where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                per_capita_output_value = list()
                for i in range(len(aa)):
                        per_capita_output_value.append(aa[i] / bb[i] / 10000)
                sql = """insert into basic_indicators(per_capita_output_value) VALUES (%s)"""
                cursor.execute(sql, per_capita_output_value)
                db.rollback()#db.commit()

                # 17、人均薪酬=(基础现金表) 支付给职工以及为职工支付的现金/ （辅助数据表）员工总数/10000
                cursor.execute("select cptfe from basis_cash where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select total_number_employees from supplementary_data where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                per_capita_salary = list()
                for i in range(len(aa)):
                        per_capita_salary.append(aa[i] / bb[i] / 10000)
                sql = """insert into basic_indicators(per_capita_salary) VALUES (%s)"""
                cursor.execute(sql, per_capita_salary)
                db.rollback()#db.commit()

                # 18、销售费用占收比=（基础利润表）销售费用/(基础利润表)营业收入
                cursor.execute(
                        "select sales_expense from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                seaapor = list()
                for i in range(len(aa)):
                        seaapor.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(seaapor) VALUES (%s)"""
                cursor.execute(sql, seaapor)
                db.rollback()#db.commit()

                # 19、管理费用占收比=（基础利润表）管理费用/(基础利润表)营业收入
                cursor.execute(
                        "select management_costs from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                meaapor = list()
                for i in range(len(aa)):
                        meaapor.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(meaapor) VALUES (%s)"""
                cursor.execute(sql, meaapor)
                db.rollback()#db.commit()

                #20、EBITDA占收比=(辅助数据表)EBITDA/(基础利润表)营业收入
                cursor.execute(
                        "select ebitda from supplementary_data where company_id=%s and company_year=%s",(company_id,company_year))
                a = cursor.fetchall()
                aa = list()
                for i in a:
                        for j in i:
                                aa.append(j)
                cursor.execute(
                        "select operating_income from basis_profit where company_id=%s and company_year=%s",(company_id,company_year))
                b = cursor.fetchall()
                bb = list()
                for i in b:
                        for j in i:
                                bb.append(j)
                eaapor = list()
                for i in range(len(aa)):
                        eaapor.append(aa[i] / bb[i])
                sql = """insert into basic_indicators(eaapor) VALUES (%s)"""
                cursor.execute(sql, eaapor)
                db.commit()
                db.rollback()
        # 4. 关闭游标
        cursor.close()
        # 5. 关闭连接
        db.close()

Basic_index_table(1)