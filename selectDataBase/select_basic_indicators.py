# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_basic_indicators
# @Date     :2020/12/1 11:40 上午
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

create_sql = """
CREATE TABLE calculate_reference (
  calculate_reference_id int(11) NOT NULL AUTO_INCREMENT,
  known_table varchar(400) DEFAULT NULL,
  known_table_attribute varchar(400) DEFAULT NULL,
  original_table varchar(400) DEFAULT NULL,
  original_table_attribute varchar(400) DEFAULT NULL,
  PRIMARY KEY (calculate_reference_id) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8 COLLATE = utf8_bin;
"""

insert_sql = """
insert into calculate_reference1('known_table','known_table_attribute','original_table','original_table_attribute') values 

('basic_indicators','gross_profit_margin','basis_profit','operating_income'),

('basic_indicators','gross_profit_margin','basis_profit','operating_costs'),

('basic_indicators','sales_margin','basis_profit','trpbttpco'),

('basic_indicators','sales_margin','basis_profit','operating_income'),

('basic_indicators','roe','basis_profit','trpbttpco'),

('basic_indicators','roe','basis_profit','tciatootp'),

('basic_indicators','mbigr','basis_profit','operating_income'),

('basic_indicators','net_profit_growth_rate','basis_profit','trpbttpco'),

('basic_indicators','net_assets_growth_rate','basis_assets','teatsotpc'),

('basic_indicators','rdiaapor','basis_profit','rd_expenses'),

('basic_indicators','rdiaapor','basis_profit','operating_income'),

('basic_indicators','accounts_receivable_turnover_days','basis_assets','accounts_receivable'),

('basic_indicators','accounts_receivable_turnover_days','basis_profit','operating_income'),

('basic_indicators','inventory_turnover_days','basis_assets','stock'),

('basic_indicators','inventory_turnover_days','basis_profit','operating_costs'),

('basic_indicators','sales_to_cash_ratio','basis_cash','crfsgapls'),

('basic_indicators','sales_to_cash_ratio','basis_profit','operating_income'),

('basic_indicators','current_ratio','basis_assets','total_current_assets'),

('basic_indicators','current_ratio','basis_assets','total_current_liabilities'),

('basic_indicators','quick_ratio','basis_assets','money_funds'),

('basic_indicators','quick_ratio','basis_assets','bfaura'),

('basic_indicators','quick_ratio','basis_assets','total_current_liabilities'),

('basic_indicators','interest_payment_multiple','basis_profit','the_total_profit'),

('basic_indicators','interest_payment_multiple','supplementary_data','nterest_payments'),

('basic_indicators','assets_and_liabilities','basis_assets','total_liabilities'),

('basic_indicators','assets_and_liabilities','basis_assets','total_assets'),

('basic_indicators','cash_short_debt_ratio','basis_cash','ncffoa'),

('basic_indicators','cash_short_debt_ratio','basis_assets','total_current_liabilities'),

('basic_indicators','per_capita_output_value','basis_profit','operating_income'),

('basic_indicators','per_capita_output_value','supplementary_data','total_number_employees'),

('basic_indicators','per_capita_output_value','basis_cash','cptfe'),

('basic_indicators','per_capita_output_value','supplementary_data','total_number_employees'),

('basic_indicators','seaapor','basis_profit','sales_expense'),

('basic_indicators','seaapor','basis_profit','operating_income'),

('basic_indicators','meaapor','basis_profit','management_costs'),

('basic_indicators','meaapor','basis_profit','operating_income'),

('basic_indicators','eaapor','supplementary_data','ebitda'),

('basic_indicators','eaapor','basis_profit','operating_income'),

('basic_indicators', 'gross_profit_margin', 'basis_profit', 'operating_income'),

('basic_indicators', 'gross_profit_margin', 'basis_profit', 'operating_costs'),

('basic_indicators', 'sales_margin', 'basis_profit', 'trpbttpco'),

('basic_indicators', 'sales_margin', 'basis_profit', 'operating_income'),

('basic_indicators', 'roe', 'basis_profit', 'trpbttpco'),

('basic_indicators', 'roe', 'basis_profit', 'tciatootp'),

('basic_indicators', 'mbigr', 'basis_profit', 'operating_income'),

('basic_indicators', 'net_profit_growth_rate', 'basis_profit', 'trpbttpco'),
('basic_indicators', 'net_assets_growth_rate', 'basis_assets', 'teatsotpc'),
('basic_indicators', 'rdiaapor', 'basis_profit', 'rd_expenses'),
('basic_indicators', 'rdiaapor', 'basis_profit', 'operating_income'),
('basic_indicators', 'accounts_receivable_turnover_days', 'basis_assets', 'accounts_receivable'),
('basic_indicators', 'accounts_receivable_turnover_days', 'basis_profit', 'operating_income'),
('basic_indicators', 'inventory_turnover_days', 'basis_assets', 'stock'),
('basic_indicators', 'inventory_turnover_days', 'basis_profit', 'operating_costs'),
('basic_indicators', 'sales_to_cash_ratio', 'basis_cash', 'crfsgapls'),
('basic_indicators', 'sales_to_cash_ratio', 'basis_profit', 'operating_income'),
('basic_indicators', 'current_ratio', 'basis_assets', 'total_current_assets'),
('basic_indicators', 'current_ratio', 'basis_assets', 'total_current_liabilities'),
('basic_indicators', 'quick_ratio', 'basis_assets', 'money_funds'),
('basic_indicators', 'quick_ratio', 'basis_assets', 'bfaura'),
('basic_indicators', 'quick_ratio', 'basis_assets', 'total_current_liabilities'),
('basic_indicators', 'interest_payment_multiple', 'basis_profit', 'the_total_profit'),
('basic_indicators', 'interest_payment_multiple', 'supplementary_data', 'nterest_payments'),
('basic_indicators', 'assets_and_liabilities', 'basis_assets', 'total_liabilities'),
('basic_indicators', 'assets_and_liabilities', 'basis_assets', 'total_assets'),
('basic_indicators', 'cash_short_debt_ratio', 'basis_cash', 'ncffoa'),
('basic_indicators', 'cash_short_debt_ratio', 'basis_assets', 'total_current_liabilities'),
('basic_indicators', 'per_capita_output_value', 'basis_profit', 'operating_income'),
('basic_indicators', 'per_capita_output_value', 'supplementary_data', 'total_number_employees'),
('basic_indicators', 'per_capita_output_value', 'basis_cash', 'cptfe'),
('basic_indicators', 'per_capita_output_value', 'supplementary_data', 'total_number_employees'),
('basic_indicators', 'seaapor', 'basis_profit', 'sales_expense'),
('basic_indicators', 'seaapor', 'basis_profit', 'operating_income'),
('basic_indicators', 'meaapor', 'basis_profit', 'management_costs'),
('basic_indicators', 'meaapor', 'basis_profit', 'operating_income'),
('basic_indicators', 'eaapor', 'supplementary_data', 'ebitda'),
('basic_indicators', 'eaapor', 'basis_profit', 'operating_income'),
('balance_horizontal', 'gross_profit_margin', 'basic_indicators', 'gross_profit_margin'),
('balance_horizontal', 'sales_margin', 'basic_indicators', 'sales_margin'),
('balance_horizontal', 'roe', 'basic_indicators', 'roe'),
('balance_horizontal', 'mbigr', 'basic_indicators', 'mbigr'),
('balance_horizontal', 'net_profit_growth_rate', 'basic_indicators', 'net_profit_growth_rate'),
('balance_horizontal', 'net_assets_growth_rate', 'basic_indicators', 'net_assets_growth_rate'),
('balance_horizontal', 'rdiaapor', 'basic_indicators', 'rdiaapor'),
('balance_horizontal', 'artd', 'basic_indicators', 'accounts_receivable_turnover_days'),
('balance_horizontal', 'inventory_turnover_days', 'basic_indicators', 'inventory_turnover_days'),
('balance_horizontal', 'sales_to_cash_ratio', 'basic_indicators', 'sales_to_cash_ratio'),
('balance_horizontal', 'current_ratio', 'basic_indicators', 'current_ratio'),
('balance_horizontal', 'quick_ratio', 'basic_indicators', 'quick_ratio'),
('balance_horizontal', 'interest_payment_multiple', 'basic_indicators', 'interest_payment_multiple'),
('balance_horizontal', 'assets_and_liabilities', 'basic_indicators', 'assets_and_liabilities'),
('balance_horizontal', 'cash_short_debt_ratio', 'basic_indicators', 'cash_short_debt_ratio'),
('balance_horizontal', 'per_capita_output_value', 'basic_indicators', 'per_capita_output_value'),
('balance_horizontal', 'per_capita_salary', 'basic_indicators', 'per_capita_salary'),
('balance_horizontal', 'seaapor', 'basic_indicators', 'seaapor'),
('balance_horizontal', 'meaapor', 'basic_indicators', 'meaapor'),
('balance_horizontal', 'ebitda', 'basic_indicators', 'eaapor'),
('balance_vertical', 'gross_profit_margin', 'basic_indicators', 'gross_profit_margin'),
('balance_vertical', 'sales_margin', 'basic_indicators', 'sales_margin'),
('balance_vertical', 'roe', 'basic_indicators', 'roe'),
('balance_vertical', 'mbigr', 'basic_indicators', 'mbigr'),
('balance_vertical', 'net_profit_growth_rate', 'basic_indicators', 'net_profit_growth_rate'),
('balance_vertical', 'net_assets_growth_rate', 'basic_indicators', 'net_assets_growth_rate'),
('balance_vertical', 'rdiaapor', 'basic_indicators', 'rdiaapor'),
('balance_vertical', 'artd', 'basic_indicators', 'accounts_receivable_turnover_days'),
('balance_vertical', 'inventory_turnover_days', 'basic_indicators', 'inventory_turnover_days'),
('balance_vertical', 'sales_to_cash_ratio', 'basic_indicators', 'sales_to_cash_ratio'),
('balance_vertical', 'current_ratio', 'basic_indicators', 'current_ratio'),
('balance_vertical', 'quick_ratio', 'basic_indicators', 'quick_ratio'),
('balance_vertical', 'interest_payment_multiple', 'basic_indicators', 'interest_payment_multiple'),
('balance_vertical', 'assets_and_liabilities', 'basic_indicators', 'assets_and_liabilities'),
('balance_vertical', 'cash_short_debt_ratio', 'basic_indicators', 'cash_short_debt_ratio'),
('balance_vertical', 'per_capita_output_value', 'basic_indicators', 'per_capita_output_value'),
('balance_vertical', 'per_capita_salary', 'basic_indicators', 'per_capita_salary'),
('balance_vertical', 'seaapor', 'basic_indicators', 'seaapor'),
('balance_vertical', 'meaapor', 'basic_indicators', 'meaapor'),
('balance_vertical', 'ebitda', 'basic_indicators', 'eaapor')
"""

# cursor
cursor = db.cursor()

def select_basic_indicators(known_table, known_table_attribute, company_id):

    # cursor.execute(create_sql)
    # cursor.execute(insert_sql)
    tablelist = []
    columnlist = []
    alist = []
    cursor.execute(
        'select original_table,original_table_attribute from calculate_reference where known_table = %s and known_table_attribute = %s ' %
        (known_table, known_table_attribute))
    result = cursor.fetchall()
    for i in result:
        tablelist.append(i[0])
        columnlist.append(i[1])
    # print(tablelist)
    # print(columnlist)
    for listnum in range(0, len(result)):
        cursor.execute("select %s from %s where company_id=%d" %
                       (columnlist[listnum], tablelist[listnum], company_id))
        result1 = cursor.fetchall()
        for i in result1:
            alist.append(i[0])
    print(alist)
    return alist
select_basic_indicators("'basic_indicators'", "'gross_profit_margin'", 1)
