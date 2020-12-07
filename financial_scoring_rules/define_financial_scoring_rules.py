# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :define_financial_scoring_rules
# @Date     :2020/12/6 21:37
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql


def define_and_insert_profitability_rules(gross_profit_margin_up,gross_profit_margin_down,sales_margin_up,sales_margin_down,roe_up,roe_down):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql="""
    insert into financial_scoring_rules(gross_profit_margin_up,gross_profit_margin_down,sales_margin_up,sales_margin_down,roe_up,roe_down) values(%s,%s,%s,%s,%s,%s)
    """
    try:
        cur.execute(sql, (
            gross_profit_margin_up, gross_profit_margin_down, sales_margin_up, sales_margin_down, roe_up, roe_down))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()
    pass

def define_and_insert_growth_ability_rules(mbigr_up,mbigr_down,net_profit_growth_rate_up,net_profit_growth_rate_down,net_assets_growth_rate_up,net_assets_growth_rate_down,rdiaapor_up,rdiaapor_down):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = """
        insert into financial_scoring_rules(mbigr_up,mbigr_down,net_profit_growth_rate_up,net_profit_growth_rate_down,net_assets_growth_rate_up,net_assets_growth_rate_down,rdiaapor_up,rdiaapor_down) values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
    try:
        cur.execute(sql, (
            mbigr_up, mbigr_down, net_profit_growth_rate_up, net_profit_growth_rate_down, net_assets_growth_rate_up,
            net_assets_growth_rate_down, rdiaapor_up, rdiaapor_down))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()
    pass

def define_and_insert_operating_capacity_rules(artd_up,artd_down,inventory_turnover_days_up,inventory_turnover_days_down,sales_to_cash_ratio_up,sales_to_cash_ratio_down):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = """
        insert into financial_scoring_rules(artd_up,artd_down,inventory_turnover_days_up,inventory_turnover_days_down,sales_to_cash_ratio_up,sales_to_cash_ratio_down) values(%s,%s,%s,%s,%s,%s)
        """
    try:
        cur.execute(sql, (
            artd_up, artd_down, inventory_turnover_days_up, inventory_turnover_days_down, sales_to_cash_ratio_up,
            sales_to_cash_ratio_down))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()
    pass

def define_and_insert_solvency_rules(current_ratio_up,current_ratio_down,quick_ratio_up,quick_ratio_down,interest_payment_multiple_up,interest_payment_multiple_down,assets_and_liabilities_up,assets_and_liabilities_down,cash_short_debt_ratio_up,cash_short_debt_ratio_down):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = """
        insert into financial_scoring_rules(current_ratio_up,current_ratio_down,quick_ratio_up,quick_ratio_down,interest_payment_multiple_up,interest_payment_multiple_down,assets_and_liabilities_up,assets_and_liabilities_down,cash_short_debt_ratio_up,cash_short_debt_ratio_down) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    try:
        cur.execute(sql, (
            current_ratio_up, current_ratio_down, quick_ratio_up, quick_ratio_down, interest_payment_multiple_up,
            interest_payment_multiple_down, assets_and_liabilities_up, assets_and_liabilities_down,
            cash_short_debt_ratio_up, cash_short_debt_ratio_down))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()
    pass

def define_and_insert_management_ability_rules(per_capita_output_value_up,per_capita_output_value_down,per_capita_salary_up,per_capita_salary_down,seaapor_up,seaapor_down,meaapor_up,meaapor_down,ebitda_up,ebitda_down):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = """
        insert into financial_scoring_rules(per_capita_output_value_up,per_capita_output_value_down,per_capita_salary_up,per_capita_salary_down,seaapor_up,seaapor_down,meaapor_up,meaapor_down,ebitda_up,ebitda_down) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    try:
        cur.execute(sql, (
            per_capita_output_value_up, per_capita_output_value_down, per_capita_salary_up, per_capita_salary_down,
            seaapor_up, seaapor_down, meaapor_up, meaapor_down, ebitda_up, ebitda_down))
        db.commit()

    except Exception as e:
        print("新增数据库失败", e)
    cur.close()
    db.close()
    pass

def update_and_define_a_financial_scoring_rules(**identifier):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = "update financial_scoring_rules set "
    i = 1
    words = []
    for key, value in identifier.items():
        if (i != len(identifier)):
            sql = sql + str(key) + "=%s , "
        else:
            sql = sql + str(key) + "=%s"
        words.append(value)
        i += 1
    try:
        cur.execute(sql, words)
        db.commit()

    except Exception as e:
        print("修改数据库失败", e)
    cur.close()
    db.close()

update_and_define_a_financial_scoring_rules(gross_profit_margin_up=1)
# define_and_insert_profitability_rules(1,1,1,1,1,1)
# define_and_insert_growth_ability_rules(1,1,1,1,1,1,1,1)
# define_and_insert_operating_capacity_rules(1,1,1,1,1,1)
# define_and_insert_solvency_rules(1,1,1,1,1,1,1,1,1,1)
# define_and_insert_management_ability_rules(1,1,1,1,1,1,1,1,1,1)