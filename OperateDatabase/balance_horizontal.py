# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :balance_horizontal
# @Date     :2020/11/28 18:13
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""

import pymysql


def insert_into_balance_horizontal(companys, years):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    for year in years:
        for company in companys:
            a=[]
            sql_avg_gross_profit_margin = "select avg(gross_profit_margin) from basic_indicators"
            cur.execute(sql_avg_gross_profit_margin)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_gross_profit_margin = "select gross_profit_margin from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_gross_profit_margin, (company, year))
            results_this_gross_profit_margin = cur.fetchall()[0][0]
            gross_profit_margin = float(results_this_gross_profit_margin) - float(results_avg)
            a.append(gross_profit_margin)

            sql_avg_sales_margin = "select avg(sales_margin) from basic_indicators"
            cur.execute(sql_avg_sales_margin)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_sales_margin = "select sales_margin from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_sales_margin, (company, year))
            results_this_sales_margin = cur.fetchall()[0][0]
            sales_margin = float(results_this_sales_margin) - float(results_avg)
            a.append(sales_margin)

            sql_avg_roe = "select avg(roe) from basic_indicators"
            cur.execute(sql_avg_roe)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_roe = "select roe from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_roe, (company, year))
            results_this_roe = cur.fetchall()[0][0]
            roe = float(results_this_roe) - float(results_avg)
            a.append(roe)

            sql_avg_mbigr = "select avg(mbigr) from basic_indicators"
            cur.execute(sql_avg_mbigr)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_mbigr = "select mbigr from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_mbigr, (company, year))
            results_this_mbigr = cur.fetchall()[0][0]
            mbigr = float(results_this_mbigr) - float(results_avg)
            a.append(mbigr)

            sql_avg_net_profit_growth_rate = "select avg(net_profit_growth_rate) from basic_indicators"
            cur.execute(sql_avg_net_profit_growth_rate)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_net_profit_growth_rate = "select net_profit_growth_rate from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_net_profit_growth_rate, (company, year))
            results_this_net_profit_growth_rate = cur.fetchall()[0][0]
            net_profit_growth_rate = float(results_this_net_profit_growth_rate) - float(results_avg)
            a.append(net_profit_growth_rate)

            sql_avg_net_assets_growth_rate = "select avg(net_assets_growth_rate) from basic_indicators"
            cur.execute(sql_avg_net_assets_growth_rate)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_net_assets_growth_rate = "select net_assets_growth_rate from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_net_assets_growth_rate, (company, year))
            results_this_net_assets_growth_rate = cur.fetchall()[0][0]
            net_assets_growth_rate = float(results_this_net_assets_growth_rate) - float(results_avg)
            a.append(net_assets_growth_rate)

            sql_avg_rdiaapor = "select avg(rdiaapor) from basic_indicators"
            cur.execute(sql_avg_rdiaapor)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_rdiaapor = "select rdiaapor from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_rdiaapor, (company, year))
            results_this_rdiaapor = cur.fetchall()[0][0]
            rdiaapor = float(results_this_rdiaapor) - float(results_avg)
            a.append(rdiaapor)

            sql_avg_accounts_receivable_turnover_days = "select avg(accounts_receivable_turnover_days) from basic_indicators"
            cur.execute(sql_avg_accounts_receivable_turnover_days)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_accounts_receivable_turnover_days = "select accounts_receivable_turnover_days from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_accounts_receivable_turnover_days, (company, year))
            results_this_accounts_receivable_turnover_days = cur.fetchall()[0][0]
            accounts_receivable_turnover_days = float(results_this_accounts_receivable_turnover_days) - float(
                results_avg)
            a.append(accounts_receivable_turnover_days)

            sql_avg_inventory_turnover_days = "select avg(inventory_turnover_days) from basic_indicators"
            cur.execute(sql_avg_inventory_turnover_days)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_inventory_turnover_days = "select inventory_turnover_days from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_inventory_turnover_days, (company, year))
            results_this_inventory_turnover_days = cur.fetchall()[0][0]
            inventory_turnover_days = float(results_this_inventory_turnover_days) - float(results_avg)
            a.append(inventory_turnover_days)

            sql_avg_sales_to_cash_ratio = "select avg(sales_to_cash_ratio) from basic_indicators"
            cur.execute(sql_avg_sales_to_cash_ratio)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_sales_to_cash_ratio = "select sales_to_cash_ratio from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_sales_to_cash_ratio, (company, year))
            results_this_sales_to_cash_ratio = cur.fetchall()[0][0]
            sales_to_cash_ratio = float(results_this_sales_to_cash_ratio) - float(results_avg)
            a.append(sales_to_cash_ratio)

            sql_avg_current_ratio = "select avg(current_ratio) from basic_indicators"
            cur.execute(sql_avg_current_ratio)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_current_ratio = "select current_ratio from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_current_ratio, (company, year))
            results_this_current_ratio = cur.fetchall()[0][0]
            current_ratio = float(results_this_current_ratio) - float(results_avg)
            a.append(current_ratio)

            sql_avg_quick_ratio = "select avg(quick_ratio) from basic_indicators"
            cur.execute(sql_avg_quick_ratio)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_quick_ratio = "select quick_ratio from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_quick_ratio, (company, year))
            results_this_quick_ratio = cur.fetchall()[0][0]
            quick_ratio = float(results_this_quick_ratio) - float(results_avg)
            a.append(quick_ratio)

            sql_avg_interest_payment_multiple = "select avg(interest_payment_multiple) from basic_indicators"
            cur.execute(sql_avg_interest_payment_multiple)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_interest_payment_multiple = "select interest_payment_multiple from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_interest_payment_multiple, (company, year))
            results_this_interest_payment_multiple = cur.fetchall()[0][0]
            interest_payment_multiple = float(results_this_interest_payment_multiple) - float(results_avg)
            a.append(interest_payment_multiple)

            sql_avg_assets_and_liabilities = "select avg(assets_and_liabilities) from basic_indicators"
            cur.execute(sql_avg_assets_and_liabilities)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_assets_and_liabilities = "select assets_and_liabilities from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_assets_and_liabilities, (company, year))
            results_this_assets_and_liabilities = cur.fetchall()[0][0]
            assets_and_liabilities = float(results_this_assets_and_liabilities) - float(results_avg)
            a.append(assets_and_liabilities)

            sql_avg_cash_short_debt_ratio = "select avg(cash_short_debt_ratio) from basic_indicators"
            cur.execute(sql_avg_cash_short_debt_ratio)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_cash_short_debt_ratio = "select cash_short_debt_ratio from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_cash_short_debt_ratio, (company, year))
            results_this_cash_short_debt_ratio = cur.fetchall()[0][0]
            cash_short_debt_ratio = float(results_this_cash_short_debt_ratio) - float(results_avg)
            a.append(cash_short_debt_ratio)

            sql_avg_per_capita_output_value = "select avg(per_capita_output_value) from basic_indicators"
            cur.execute(sql_avg_per_capita_output_value)
            results_avg = cur.fetchall()[0][0]

            sql_avg_per_capita_salary = "select avg(per_capita_salary) from basic_indicators"
            cur.execute(sql_avg_per_capita_salary)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_per_capita_salary = "select per_capita_salary from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_per_capita_salary, (company, year))
            results_this_per_capita_salary = cur.fetchall()[0][0]
            per_capita_salary = float(results_this_per_capita_salary) - float(results_avg)
            a.append(per_capita_salary)

            sql_avg_seaapor = "select avg(seaapor) from basic_indicators"
            cur.execute(sql_avg_seaapor)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_seaapor = "select seaapor from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_seaapor, (company, year))
            results_this_seaapor = cur.fetchall()[0][0]
            seaapor = float(results_this_seaapor) - float(results_avg)
            a.append(seaapor)

            sql_avg_meaapor = "select avg(meaapor) from basic_indicators"
            cur.execute(sql_avg_meaapor)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_meaapor = "select meaapor from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_meaapor, (company, year))
            results_this_meaapor = cur.fetchall()[0][0]
            meaapor = float(results_this_meaapor) - float(results_avg)
            a.append(meaapor)

            sql_avg_eaapor = "select avg(eaapor) from basic_indicators"
            cur.execute(sql_avg_eaapor)
            results_avg = cur.fetchall()[0][0]

            sql_this_avg_eaapor = "select eaapor from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_eaapor, (company, year))
            results_this_eaapor = cur.fetchall()[0][0]
            eaapor = float(results_this_eaapor) - float(results_avg)
            a.append(eaapor)

            sql_this_avg_per_capita_output_value = "select per_capita_output_value from basic_indicators where company_id=%s and company_year=%s"
            cur.execute(sql_this_avg_per_capita_output_value, (company, year))
            results_this_per_capita_output_value = cur.fetchall()[0][0]
            per_capita_output_value = float(results_this_per_capita_output_value) - float(results_avg)
            a.append(per_capita_output_value)
            a.append(company)
            a.append(year)
            sql="insert into balance_horizontal(gross_profit_margin,sales_margin,roe,mbigr,net_profit_growth_rate,net_assets_growth_rate,rdiaapor,artd,inventory_turnover_days,sales_to_cash_ratio,current_ratio,quick_ratio,interest_payment_multiple,assets_and_liabilities,cash_short_debt_ratio,per_capita_salary,seaapor,meaapor,ebitda,per_capita_output_value,company_id,company_year) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cur.execute(sql,a)

    db.commit()
    cur.close()
    db.close()
    pass


insert_into_balance_horizontal([1, 2, 3, 4, 5], [2017, 2018, 2019])
