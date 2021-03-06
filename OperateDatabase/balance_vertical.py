# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :balance_vertical
# @Date     :2020/11/26 5:42 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

db_username = 'root'
db_password = 'root1234'
db_name = 'dymtest'
db = pymysql.connect("localhost", db_username, db_password, db_name)

# cursor
cursor = db.cursor()


def calculate_gross_profit(years, company):
    print('gross_profit:')
    alist = []
    gross_profit_list = []
    for year in years:
        cursor.execute(
            "select gross_profit_margin from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        gross_profit_margin_now = cursor.fetchone()[0]
        alist.append(gross_profit_margin_now)

    for i in range(0, len(years) - 1):
        gross_profit_list.append(alist[i + 1] - alist[i])
    print(gross_profit_list)
    print('==============================')
    return gross_profit_list


def calculate_sales_margin(years, company):
    print('sales_margin:')
    alist = []
    sales_margin_list = []
    for year in years:
        cursor.execute(
            "select sales_margin from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        sales_margin_now = cursor.fetchone()[0]
        alist.append(sales_margin_now)

    for i in range(0, len(years) - 1):
        sales_margin_list.append(alist[i + 1] - alist[i])
    print(sales_margin_list)
    print('==============================')
    return sales_margin_list


def calculate_roe(years, company):
    print('==============================')
    print('roe:')
    alist = []
    roe_list = []
    for year in years:
        cursor.execute(
            "select roe from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        roe_now = cursor.fetchone()[0]
        alist.append(roe_now)

    for i in range(0, len(years) - 1):
        roe_list.append(alist[i + 1] - alist[i])
    print(roe_list)
    print('==============================')
    return roe_list


def calculate_mbigr(years, company):
    print('==============================')
    print('mbigr:')
    alist = []
    mbigr_list = []
    for year in years:
        cursor.execute(
            "select mbigr from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        mbigr_now = cursor.fetchone()[0]
        alist.append(mbigr_now)

    for i in range(0, len(years) - 1):
        mbigr_list.append(alist[i + 1] - alist[i])
    print(mbigr_list)
    print('==============================')
    return mbigr_list


def calculate_net_profit_growth_rate(years, company):
    print('==============================')
    print('net_profit_growth_rate:')
    alist = []
    net_profit_growth_rate_list = []
    for year in years:
        cursor.execute(
            "select net_profit_growth_rate from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        net_profit_growth_rate_now = cursor.fetchone()[0]
        alist.append(net_profit_growth_rate_now)

    for i in range(0, len(years) - 1):
        net_profit_growth_rate_list.append(alist[i + 1] - alist[i])
    print(net_profit_growth_rate_list)
    print('==============================')
    return net_profit_growth_rate_list


def calculate_net_assets_growth_rate(years, company):
    print('==============================')
    print('net_assets_growth_rate:')
    alist = []
    net_profit_assets_rate_list = []
    for year in years:
        cursor.execute(
            "select net_assets_growth_rate from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        net_assets_growth_rate_now = cursor.fetchone()[0]
        alist.append(net_assets_growth_rate_now)
    for i in range(0, len(years) - 1):
        net_profit_assets_rate_list.append(alist[i + 1] - alist[i])
    print(net_profit_assets_rate_list)
    print('==============================')
    return net_profit_assets_rate_list


def calculate_rdiaapor(years, company):
    print('==============================')
    print('rdiaapor:')
    alist = []
    rdiaapor_list = []
    for year in years:
        cursor.execute(
            "select rdiaapor from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        rdiaapor_now = cursor.fetchone()[0]
        alist.append(rdiaapor_now)

    for i in range(0, len(years) - 1):
        rdiaapor_list.append(alist[i + 1] - alist[i])
    print(rdiaapor_list)
    print('==============================')
    return rdiaapor_list


def calculate_artd(years, company):
    print('==============================')
    print('artd:')
    alist = []
    artd_list = []
    for year in years:
        cursor.execute(
            "select accounts_receivable_turnover_days from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        artd_now = cursor.fetchone()[0]
        alist.append(artd_now)

    for i in range(0, len(years) - 1):
        artd_list.append(alist[i + 1] - alist[i])
    print(artd_list)
    print('==============================')
    return artd_list


def calculate_inventory_turnover_days(years, company):
    print('==============================')
    print('inventory_turnover_days:')
    alist = []
    inventory_turnover_days_list = []
    for year in years:
        cursor.execute(
            "select inventory_turnover_days from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        inventory_turnover_days_now = cursor.fetchone()[0]
        alist.append(inventory_turnover_days_now)

    for i in range(0, len(years) - 1):
        inventory_turnover_days_list.append(alist[i + 1] - alist[i])
    print(inventory_turnover_days_list)
    print('==============================')
    return inventory_turnover_days_list


def calculate_sales_to_cash_ratio(years, company):
    print('==============================')
    print('sales_to_cash_ratio:')
    alist = []
    sales_to_cash_ratio_list = []
    for year in years:
        cursor.execute(
            "select sales_to_cash_ratio from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        sales_to_cash_ratio_now = cursor.fetchone()[0]
        alist.append(sales_to_cash_ratio_now)

    for i in range(0, len(years) - 1):
        sales_to_cash_ratio_list.append(alist[i + 1] - alist[i])
    print(sales_to_cash_ratio_list)
    print('==============================')
    return sales_to_cash_ratio_list


def calculate_current_ratio(years, company):
    print('==============================')
    print('current_ratio:')
    alist = []
    current_ratio_list = []
    for year in years:
        cursor.execute(
            "select current_ratio from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        current_ratio_now = cursor.fetchone()[0]
        alist.append(current_ratio_now)

    for i in range(0, len(years) - 1):
        current_ratio_list.append(alist[i + 1] - alist[i])
    print(current_ratio_list)
    print('==============================')
    return current_ratio_list


def calculate_quick_ratio(years, company):
    print('==============================')
    print('quick_ratio:')
    alist = []
    quick_ratio_list = []
    for year in years:
        cursor.execute(
            "select quick_ratio from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        quick_ratio_now = cursor.fetchone()[0]
        alist.append(quick_ratio_now)

    for i in range(0, len(years) - 1):
        quick_ratio_list.append(alist[i + 1] - alist[i])
    print(quick_ratio_list)
    print('==============================')
    return quick_ratio_list


def calculate_interest_payment_multiple(years, company):
    print('==============================')
    print('interest_payment_multiple:')
    alist = []
    interest_payment_multiple_list = []
    for year in years:
        cursor.execute(
            "select interest_payment_multiple from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        interest_payment_multiple_now = cursor.fetchone()[0]
        alist.append(interest_payment_multiple_now)

    for i in range(0, len(years) - 1):
        interest_payment_multiple_list.append(alist[i + 1] - alist[i])
    print(interest_payment_multiple_list)
    print('==============================')
    return interest_payment_multiple_list


def calculate_assets_and_liabilities(years, company):
    print('==============================')
    print('assets_and_liabilities:')
    alist = []
    assets_and_liabilities_list = []
    for year in years:
        cursor.execute(
            "select assets_and_liabilities from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        assets_and_liabilities_now = cursor.fetchone()[0]
        alist.append(assets_and_liabilities_now)

    for i in range(0, len(years) - 1):
        assets_and_liabilities_list.append(alist[i + 1] - alist[i])
    print(assets_and_liabilities_list)
    print('==============================')
    return assets_and_liabilities_list


def calculate_cash_short_debt_ratio(years, company):
    print('==============================')
    print('cash_short_debt_ratio:')
    alist = []
    cash_short_debt_ratio_list = []
    for year in years:
        cursor.execute(
            "select assets_and_liabilities from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        cash_short_debt_ratio_now = cursor.fetchone()[0]
        alist.append(cash_short_debt_ratio_now)

    for i in range(0, len(years) - 1):
        cash_short_debt_ratio_list.append(alist[i + 1] - alist[i])
    print(cash_short_debt_ratio_list)
    print('==============================')
    return cash_short_debt_ratio_list


def calculate_per_capita_output_value(years, company):
    print('==============================')
    print('per_capita_output_value:')
    alist = []
    per_capita_output_value_list = []
    for year in years:
        cursor.execute(
            "select per_capita_output_value from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        per_capita_output_value_now = cursor.fetchone()[0]
        alist.append(per_capita_output_value_now)

    for i in range(0, len(years) - 1):
        per_capita_output_value_list.append(alist[i + 1] - alist[i])
    print(per_capita_output_value_list)
    print('==============================')
    return per_capita_output_value_list


def calculate_per_capita_salary(years, company):
    print('==============================')
    print('per_capita_salary:')
    alist = []
    per_capita_salary_list = []
    for year in years:
        cursor.execute(
            "select per_capita_salary from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        per_capita_salary_now = cursor.fetchone()[0]
        alist.append(per_capita_salary_now)

    for i in range(0, len(years) - 1):
        per_capita_salary_list.append(alist[i + 1] - alist[i])
    print(per_capita_salary_list)
    print('==============================')
    return per_capita_salary_list


def calculate_seaapor(years, company):
    print('==============================')
    print('seaapor:')
    alist = []
    seaapor_list = []
    for year in years:
        cursor.execute(
            "select seaapor from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        seaapor_now = cursor.fetchone()[0]
        alist.append(seaapor_now)

    for i in range(0, len(years) - 1):
        seaapor_list.append(alist[i + 1] - alist[i])
    print(seaapor_list)
    print('==============================')
    return seaapor_list


def calculate_meaapor(years, company):
    print('==============================')
    print('meaapor:')
    alist = []
    meaapor_list = []
    for year in years:
        cursor.execute(
            "select meaapor from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        meaapor_now = cursor.fetchone()[0]
        alist.append(meaapor_now)

    for i in range(0, len(years) - 1):
        meaapor_list.append(alist[i + 1] - alist[i])
    print(meaapor_list)
    print('==============================')
    return meaapor_list


def calculate_ebitda(years, company):
    print('==============================')
    print('ebitda:')
    alist = []
    ebitda_list = []
    for year in years:
        cursor.execute(
            "select eaapor from basic_indicators where company_year=%d and company_id=%d" %
            (year, company))
        ebitda_now = cursor.fetchone()[0]
        alist.append(ebitda_now)

    for i in range(0, len(years) - 1):
        ebitda_list.append(alist[i + 1] - alist[i])
    print(ebitda_list)
    print('==============================')
    return ebitda_list


sql_create_balance_vertical = """
CREATE TABLE balance_vertical (
  balance_vertical_id int(11) NOT NULL AUTO_INCREMENT COMMENT '纵向差额表ID',
  gross_profit_margin float(11, 9) NOT NULL COMMENT '销售毛利率(%)',
  sales_margin float(11, 9) NOT NULL COMMENT '销售净利率(%)',
  roe float(20, 9) NULL DEFAULT NULL COMMENT '净资产收益率(%)',
  mbigr float(20, 9) NULL DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  net_profit_growth_rate float(20, 9) NULL DEFAULT NULL COMMENT '净利润增长率(%)',
  net_assets_growth_rate float(20, 9) NULL DEFAULT NULL COMMENT '净资产增长率(%)',
  rdiaapor float(20, 9) NULL DEFAULT NULL COMMENT '研发投入占收比(%)',
  artd float(20, 9) NULL DEFAULT NULL COMMENT '应收账款周转天数(天)\r\n',
  inventory_turnover_days float(20, 9) NULL DEFAULT NULL COMMENT '存货周转天数(天)',
  sales_to_cash_ratio float(20, 9) NULL DEFAULT NULL COMMENT '销售收现比',
  current_ratio float(20, 9) NULL DEFAULT NULL COMMENT '流动比率',
  quick_ratio float(20, 9) NULL DEFAULT NULL COMMENT '速动比率',
  interest_payment_multiple float(20, 9) NULL DEFAULT NULL COMMENT '利息支付倍数',
  assets_and_liabilities float(20, 9) NULL DEFAULT NULL COMMENT '资产负债率(%)',
  cash_short_debt_ratio float(20, 9) NULL DEFAULT NULL COMMENT '现金短债比',
  per_capita_output_value float(20, 9) NULL DEFAULT NULL COMMENT '人均产值',
  per_capita_salary float(20, 9) NULL DEFAULT NULL COMMENT '人均薪酬',
  seaapor float(20, 9) NULL DEFAULT NULL COMMENT '销售费用占收比',
  meaapor float(20, 9) NULL DEFAULT NULL COMMENT '管理费用占收比',
  ebitda float(20, 9) NULL DEFAULT NULL COMMENT 'EBITDA占收比',
  company_year int(11) NULL DEFAULT NULL COMMENT '公司报表年份',
  company_name varchar(25) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '公司名',
  company_id int(11) NULL DEFAULT NULL COMMENT '公司表ID',
  PRIMARY KEY (balance_vertical_id) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '纵向差额表' ROW_FORMAT = DYNAMIC;
"""


def year_list(years):
    year_list = []
    for year in years:
        year_list.append(year + 1)
    return year_list


def insert_balance_vertical(years, company):
    for j in range(0, len(years) - 1):
        sql_insert_balance_vertical = """
        INSERT INTO balance_vertical VALUES (%d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d, NULL, %d);
        """ % \
                                      (int(str(company) + str(j + 1)),
                                       calculate_gross_profit(years, company)[j],
                                       calculate_sales_margin(years, company)[j],
                                       calculate_roe(years, company)[j],
                                       calculate_mbigr(years, company)[j],
                                       calculate_net_profit_growth_rate(years, company)[j],
                                       calculate_net_assets_growth_rate(years, company)[j],
                                       calculate_rdiaapor(years, company)[j], calculate_artd(years, company)[j],
                                       calculate_inventory_turnover_days(years, company)[j],
                                       calculate_sales_to_cash_ratio(years, company)[j],
                                       calculate_current_ratio(years, company)[j],
                                       calculate_quick_ratio(years, company)[j],
                                       calculate_inventory_turnover_days(years, company)[j],
                                       calculate_assets_and_liabilities(years, company)[j],
                                       calculate_cash_short_debt_ratio(years, company)[j],
                                       calculate_per_capita_output_value(years, company)[j],
                                       calculate_per_capita_salary(years, company)[j],
                                       calculate_seaapor(years, company)[j], calculate_meaapor(years, company)[j],
                                       calculate_ebitda(years, company)[j],
                                       year_list(years)[j],
                                       company
                                       )
        try:
            cursor.execute(sql_insert_balance_vertical)
            db.commit()
        except:
            db.rollback()
    return True


insert_balance_vertical([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], 1)
db.close()
