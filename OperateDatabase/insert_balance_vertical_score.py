# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :insert_balance_vertical
# @Date     :2020/12/3 12:31 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

from selectDataBase.select_company import select_company_by_id

db_username = 'root'
db_password = 'root1234'
db_name = 'grss'
db = pymysql.connect("localhost", db_username, db_password, db_name)

# cursor
cursor = db.cursor()

indicators_list = ['gross_profit_margin', 'sales_margin', 'roe', 'mbigr', 'net_profit_growth_rate',
                   'net_assets_growth_rate', 'rdiaapor',
                   'artd', 'inventory_turnover_days', 'sales_to_cash_ratio', 'current_ratio', 'quick_ratio',
                   'interest_payment_multiple', 'assets_and_liabilities',
                   'cash_short_debt_ratio', 'per_capita_output_value', 'per_capita_salary', 'seaapor', 'meaapor',
                   'ebitda']


def select_profitability_ability_list(company_id, company_year):
    profitability_ability_list = []
    for i in range(0, 3):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        profitability_ability_list.append(cursor.fetchone()[0])
    return profitability_ability_list


def select_growth_ability_list(company_id, company_year):
    growth_ability_list = []
    for i in range(3, 7):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        growth_ability_list.append(cursor.fetchone()[0])
    return growth_ability_list


def select_artd_list(company_id, company_year):
    artd_list = []
    for i in range(7, 8):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        artd_list.append(cursor.fetchone()[0])
    return artd_list


def select_inventory_turnover_days_list(company_id, company_year):
    inventory_turnover_days_list = []
    for i in range(8, 9):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        inventory_turnover_days_list.append(cursor.fetchone()[0])
    return inventory_turnover_days_list


def select_sales_to_cash_ratio_list(company_id, company_year):
    sales_to_cash_ratio_list = []
    for i in range(9, 10):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        sales_to_cash_ratio_list.append(cursor.fetchone()[0])
    return sales_to_cash_ratio_list


def select_debt_paying_ability_list(company_id, company_year):
    debt_paying_ability_list = []
    for i in range(10, 15):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        debt_paying_ability_list.append(cursor.fetchone()[0])
    return debt_paying_ability_list


def select_management_ability_list(company_id, company_year):
    management_ability_list = []
    for i in range(15, 20):
        cursor.execute("select %s from balance_vertical where company_id=%d and company_year=%d" %
                       ("{}".format(indicators_list[i]), company_id, company_year))
        management_ability_list.append(cursor.fetchone()[0])
    return management_ability_list


def calculate_score(company_id, company_year):
    score_list = []
    # 盈利能力
    for i in range(0, len(select_profitability_ability_list(company_id, company_year))):
        profitability_ability = select_profitability_ability_list(company_id, company_year)[i]
        # print(profitability_ability)
        if profitability_ability >= 0.1:
            score = 5
        elif profitability_ability >= 0.05:
            score = 4
        elif profitability_ability >= -0.05:
            score = 3
        elif profitability_ability >= -0.1:
            score = 2
        else:
            score = 1
        score_list.append(score)

    # 成长能力
    for i in range(0, len(select_growth_ability_list(company_id, company_year))):
        growth_ability = select_growth_ability_list(company_id, company_year)[i]
        # print(growth_ability)
        if growth_ability >= 0.1:
            score = 5
        elif growth_ability >= 0.05:
            score = 4
        elif growth_ability >= -0.05:
            score = 3
        elif growth_ability >= -0.1:
            score = 2
        else:
            score = 1
        score_list.append(score)

    # 应收账款周转天数
    for i in range(0, len(select_artd_list(company_id, company_year))):
        artd = select_artd_list(company_id, company_year)[i]
        # print(artd)
        if artd <= -10:
            score = 5
        elif artd <= -1:
            score = 4
        elif artd <= -1:
            score = 3
        elif artd <= 10:
            score = 2
        else:
            score = 1
        score_list.append(score)
    # 
    #  存货周转天数
    for i in range(0, len(select_inventory_turnover_days_list(company_id, company_year))):
        inventory_turnover_days = select_inventory_turnover_days_list(company_id, company_year)[i]
        # print(inventory_turnover_days)
        if inventory_turnover_days <= -20:
            score = 5
        elif inventory_turnover_days <= -1:
            score = 4
        elif inventory_turnover_days <= 1:
            score = 3
        elif inventory_turnover_days <= 20:
            score = 2
        else:
            score = 1
        score_list.append(score)
    # 
    # 销售收现比
    for i in range(0, len(select_sales_to_cash_ratio_list(company_id, company_year))):
        sales_to_cash_ratio = select_sales_to_cash_ratio_list(company_id, company_year)[i]
        # print(sales_to_cash_ratio)
        if sales_to_cash_ratio >= 0.1:
            score = 5
        elif sales_to_cash_ratio >= 0.05:
            score = 4
        elif sales_to_cash_ratio >= -0.05:
            score = 3
        elif sales_to_cash_ratio >= -0.1:
            score = 2
        else:
            score = 1
        score_list.append(score)
    # 
    # 偿债能力
    for i in range(0, len(select_debt_paying_ability_list(company_id, company_year))):
        debt_paying_ability = select_debt_paying_ability_list(company_id, company_year)[i]
        # print(debt_paying_ability)
        if debt_paying_ability >= 0.1:
            score = 5
        elif debt_paying_ability >= 0.05:
            score = 4
        elif debt_paying_ability >= -0.05:
            score = 3
        elif debt_paying_ability >= -0.1:
            score = 2
        else:
            score = 1
        score_list.append(score)
    # 
    # 管理能力
    for i in range(0, len(select_management_ability_list(company_id, company_year))):
        management_ability = select_management_ability_list(company_id, company_year)[i]
        # print(management_ability)
        if management_ability >= 0.1:
            score = 5
        elif management_ability >= 0.05:
            score = 4
        elif management_ability >= -0.05:
            score = 3
        elif management_ability >= -0.1:
            score = 2
        else:
            score = 1
        score_list.append(score)
    return score_list


def calculate_profitability_ability_score(company_id, company_year):
    cpasl_total = 0
    calculate_profitability_ability_score_list = []
    for i in range(0, 3):
        cursor.execute("select * from power_weight")
        result = cursor.fetchall()[0]
        calculate_profitability_ability_score_list.append(calculate_score(company_id, company_year)[i] * result[i + 1])

    for ele in range(0, len(calculate_profitability_ability_score_list)):
        cpasl_total = cpasl_total + calculate_profitability_ability_score_list[ele]
    return cpasl_total


def calculate_growth_ability_score(company_id, company_year):
    cgas_total = 0
    calculate_growth_ability_score_list = []
    for i in range(3, 7):
        cursor.execute("select * from power_weight")
        result = cursor.fetchall()[0]
        calculate_growth_ability_score_list.append(calculate_score(company_id, company_year)[i] * result[i + 1])

    for ele in range(0, len(calculate_growth_ability_score_list)):
        cgas_total = cgas_total + calculate_growth_ability_score_list[ele]
    return cgas_total


def calculate_operation_ability_score(company_id, company_year):
    coas_total = 0
    calculate_operation_ability_score_list = []
    for i in range(7, 10):
        cursor.execute("select * from power_weight")
        result = cursor.fetchall()[0]
        calculate_operation_ability_score_list.append(calculate_score(company_id, company_year)[i] * result[i + 1])

    for ele in range(0, len(calculate_operation_ability_score_list)):
        coas_total = coas_total + calculate_operation_ability_score_list[ele]
    return coas_total


def calculate_debt_paying_ability_score(company_id, company_year):
    cdpas_total = 0
    calculate_debt_paying_ability_score_list = []
    for i in range(10, 15):
        cursor.execute("select * from power_weight")
        result = cursor.fetchall()[0]
        calculate_debt_paying_ability_score_list.append(calculate_score(company_id, company_year)[i] * result[i + 1])

    for ele in range(0, len(calculate_debt_paying_ability_score_list)):
        cdpas_total = cdpas_total + calculate_debt_paying_ability_score_list[ele]
    return cdpas_total


def calculate_management_ability_score(company_id, company_year):
    cmas_total = 0
    calculate_management_ability_score_list = []
    for i in range(15, 20):
        cursor.execute("select * from power_weight")
        result = cursor.fetchall()[0]
        calculate_management_ability_score_list.append(calculate_score(company_id, company_year)[i] * result[i + 1])

    for ele in range(0, len(calculate_management_ability_score_list)):
        cmas_total = cmas_total + calculate_management_ability_score_list[ele]
    return cmas_total


def insert_balance_vertical_score(company_id, company_year):
    insert_sql = "INSERT INTO score_longitudinal VALUES (NULL,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%d,%s,%d);" % \
                 (company_id, calculate_score(company_id, company_year)[0],
                  calculate_score(company_id, company_year)[1], calculate_score(company_id, company_year)[2],
                  calculate_score(company_id, company_year)[3], calculate_score(company_id, company_year)[4],
                  calculate_score(company_id, company_year)[5], calculate_score(company_id, company_year)[6],
                  calculate_score(company_id, company_year)[7], calculate_score(company_id, company_year)[8],
                  calculate_score(company_id, company_year)[9],
                  calculate_score(company_id, company_year)[10], calculate_score(company_id, company_year)[11],
                  calculate_score(company_id, company_year)[12], calculate_score(company_id, company_year)[13],
                  calculate_score(company_id, company_year)[14], calculate_score(company_id, company_year)[15],
                  calculate_score(company_id, company_year)[16], calculate_score(company_id, company_year)[17],
                  calculate_score(company_id, company_year)[18], calculate_score(company_id, company_year)[19],
                  calculate_profitability_ability_score(company_id, company_year),
                  calculate_growth_ability_score(company_id, company_year),
                  calculate_operation_ability_score(company_id, company_year),
                  calculate_debt_paying_ability_score(company_id, company_year),
                  calculate_management_ability_score(company_id, company_year), company_year,"'{}'".format(select_company_by_id(company_id)), company_id)
    try:
        cursor.execute(insert_sql)
        db.commit()
    except:
        db.rollback()
    print('Done!')
    return True


insert_balance_vertical_score(1, 2017)
