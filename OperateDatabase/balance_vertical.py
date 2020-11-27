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

db = pymysql.connect("localhost", "root", "root1234", "dymtest")
cursor_gross_profit_margin = db.cursor()
cursor_sales_margin = db.cursor()
cursor_roe = db.cursor()
cursor_mbigr = db.cursor()
cursor_net_profit_growth_rate = db.cursor()
cursor_net_assets_growth_rate = db.cursor()
cursor_rdiaapor = db.cursor()
cursor_artd = db.cursor()
cursor_inventory_turnover_days = db.cursor()
cursor_sales_to_cash_ratio = db.cursor()
cursor_current_ratio = db.cursor()
cursor_quick_ratio = db.cursor()
cursor_interest_payment_multiple = db.cursor()
cursor_assets_and_liabilities = db.cursor()
cursor_cash_short_debt_ratio = db.cursor()
cursor_per_capita_output_value = db.cursor()
cursor_per_capita_salary = db.cursor()
cursor_seaapor = db.cursor()
cursor_meaapor = db.cursor()
cursor_ebitda = db.cursor()
start_year=2010
end_year=2020
# year = [2019,2018,2017,2016,2015,2014,2013,2012,2011]
print('gross_profit:')
alist = []
for year in range(start_year, end_year):
    cursor_gross_profit_margin.execute(
        "select gross_profit_margin from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    gross_profit_margin_now = cursor_gross_profit_margin.fetchone()[0]
    alist.append(gross_profit_margin_now)
print(alist)
gross_profit_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(gross_profit_list)
print('==============================')
print('sales_margin:')
alist = []
for year in range(start_year, end_year):
    cursor_sales_margin.execute(
        "select sales_margin from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    sales_margin_now = cursor_sales_margin.fetchone()[0]
    alist.append(sales_margin_now)
print(alist)
sales_margin_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(sales_margin_list)
print('==============================')
print('roe:')
alist = []
for year in range(start_year, end_year):
    cursor_roe.execute(
        "select roe from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    roe_now = cursor_roe.fetchone()[0]
    alist.append(roe_now)
print(alist)
roe_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(roe_list)
print('==============================')
print('mbigr:')
alist = []
for year in range(start_year, end_year):
    cursor_mbigr.execute(
        "select mbigr from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    mbigr_now = cursor_mbigr.fetchone()[0]
    alist.append(mbigr_now)
print(alist)
mbigr_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(mbigr_list)
print('==============================')
print('net_profit_growth_rate:')
alist = []
for year in range(start_year, end_year):
    cursor_net_profit_growth_rate.execute(
        "select net_profit_growth_rate from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    net_profit_growth_rate_now = cursor_net_profit_growth_rate.fetchone()[0]
    alist.append(net_profit_growth_rate_now)
print(alist)
net_profit_growth_rate_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(net_profit_growth_rate_list)
print('==============================')
print('net_assets_growth_rate:')
alist = []
for year in range(start_year, end_year):
    cursor_net_assets_growth_rate.execute(
        "select net_assets_growth_rate from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    net_assets_growth_rate_now = cursor_net_assets_growth_rate.fetchone()[0]
    alist.append(net_assets_growth_rate_now)
print(alist)
net_assets_growth_rate_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(net_assets_growth_rate_list)
print('==============================')
print('rdiaapor:')
alist = []
for year in range(start_year, end_year):
    cursor_rdiaapor.execute(
        "select rdiaapor from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    rdiaapor_now = cursor_rdiaapor.fetchone()[0]
    alist.append(rdiaapor_now)
print(alist)
rdiaapor_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(rdiaapor_list)
print('==============================')
print('artd:')
alist = []
for year in range(start_year, end_year):
    cursor_artd.execute(
        "select accounts_receivable_turnover_days from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    artd_now = cursor_artd.fetchone()[0]
    alist.append(artd_now)
print(alist)
artd_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(artd_list)
print('==============================')
print('inventory_turnover_days:')
alist = []
for year in range(start_year, end_year):
    cursor_inventory_turnover_days.execute(
        "select inventory_turnover_days from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    inventory_turnover_days_now = cursor_inventory_turnover_days.fetchone()[0]
    alist.append(inventory_turnover_days_now)
print(alist)
inventory_turnover_days_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(inventory_turnover_days_list)
print('==============================')
print('sales_to_cash_ratio:')
alist = []
for year in range(start_year, end_year):
    cursor_sales_to_cash_ratio.execute(
        "select sales_to_cash_ratio from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    sales_to_cash_ratio_now = cursor_sales_to_cash_ratio.fetchone()[0]
    alist.append(sales_to_cash_ratio_now)
print(alist)
sales_to_cash_ratio_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(sales_to_cash_ratio_list)
print('==============================')
print('current_ratio:')
alist = []
for year in range(start_year, end_year):
    cursor_current_ratio.execute(
        "select current_ratio from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    current_ratio_now = cursor_current_ratio.fetchone()[0]
    alist.append(current_ratio_now)
print(alist)
current_ratio_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(current_ratio_list)
print('==============================')
print('quick_ratio:')
alist = []
for year in range(start_year, end_year):
    cursor_quick_ratio.execute(
        "select quick_ratio from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    quick_ratio_now = cursor_quick_ratio.fetchone()[0]
    alist.append(quick_ratio_now)
print(alist)
quick_ratio_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(quick_ratio_list)
print('==============================')
print('interest_payment_multiple:')
alist = []
for year in range(start_year, end_year):
    cursor_interest_payment_multiple.execute(
        "select interest_payment_multiple from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    interest_payment_multiple_now = cursor_interest_payment_multiple.fetchone()[0]
    alist.append(interest_payment_multiple_now)
print(alist)
interest_payment_multiple_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(interest_payment_multiple_list)
print('==============================')
print('assets_and_liabilities:')
alist = []
for year in range(start_year, end_year):
    cursor_assets_and_liabilities.execute(
        "select assets_and_liabilities from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    assets_and_liabilities_now = cursor_assets_and_liabilities.fetchone()[0]
    alist.append(assets_and_liabilities_now)
print(alist)
assets_and_liabilities_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(assets_and_liabilities_list)
print('==============================')
print('cash_short_debt_ratio:')
alist = []
for year in range(start_year, end_year):
    cursor_cash_short_debt_ratio.execute(
        "select assets_and_liabilities from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    cash_short_debt_ratio_now = cursor_cash_short_debt_ratio.fetchone()[0]
    alist.append(cash_short_debt_ratio_now)
print(alist)
cash_short_debt_ratio_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(cash_short_debt_ratio_list)
print('==============================')
print('per_capita_output_value:')
alist = []
for year in range(start_year, end_year):
    cursor_per_capita_output_value.execute(
        "select per_capita_output_value from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    per_capita_output_value_now = cursor_per_capita_output_value.fetchone()[0]
    alist.append(per_capita_output_value_now)
print(alist)
per_capita_output_value_list = [alist[9] - alist[8], alist[8] - alist[7], alist[7] - alist[6], alist[6] - alist[5], alist[5] - alist[4],
               alist[4] - alist[3], alist[3] - alist[2], alist[2] - alist[1], alist[1] - alist[0]]
print(per_capita_output_value_list)
print('==============================')
print('per_capita_salary:')
alist = []
for year in range(start_year, end_year):
    cursor_per_capita_salary.execute(
        "select per_capita_salary from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    per_capita_salary_now = cursor_per_capita_salary.fetchone()[0]
    alist.append(per_capita_salary_now)
print(alist)
per_capita_salary_list = [alist[9]-alist[8],alist[8]-alist[7],alist[7]-alist[6],alist[6]-alist[5],alist[5]-alist[4],alist[4]-alist[3],alist[3]-alist[2],alist[2]-alist[1],alist[1]-alist[0]]
print(per_capita_salary_list)
print('==============================')
print('seaapor:')
alist = []
for year in range(start_year, end_year):
    cursor_seaapor.execute(
        "select seaapor from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    seaapor_now = cursor_seaapor.fetchone()[0]
    alist.append(seaapor_now)
print(alist)
seaapor_list = [alist[9]-alist[8],alist[8]-alist[7],alist[7]-alist[6],alist[6]-alist[5],alist[5]-alist[4],alist[4]-alist[3],alist[3]-alist[2],alist[2]-alist[1],alist[1]-alist[0]]
print(seaapor_list)
print('==============================')
print('meaapor:')
alist = []
for year in range(start_year, end_year):
    cursor_meaapor.execute(
        "select meaapor from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    meaapor_now = cursor_meaapor.fetchone()[0]
    alist.append(meaapor_now)
print(alist)
meaapor_list = [alist[9]-alist[8],alist[8]-alist[7],alist[7]-alist[6],alist[6]-alist[5],alist[5]-alist[4],alist[4]-alist[3],alist[3]-alist[2],alist[2]-alist[1],alist[1]-alist[0]]
print(meaapor_list)
print('==============================')
# def list_split(items, n):
#     return [items[i:i+n] for i in range(0, len(items),n)]
print('ebitda:')
alist = []
for year in range(start_year, end_year):
    cursor_ebitda.execute(
        "select eaapor from basic_indicators where company_year=%d and company_id=1" % \
        (year))
    ebitda_now = cursor_ebitda.fetchone()[0]
    # print(ebitda_now)
    # print(year)
    alist.append(ebitda_now)
print(alist)
ebitda_list = [alist[9]-alist[8],alist[8]-alist[7],alist[7]-alist[6],alist[6]-alist[5],alist[5]-alist[4],alist[4]-alist[3],alist[3]-alist[2],alist[2]-alist[1],alist[1]-alist[0]]
print(ebitda_list)
print('==============================')

cursor_insert = db.cursor()
cursor_create = db.cursor()

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
# cursor_create.execute(sql_create_balance_vertical)


for j in range(0,9):

    sql_insert_balance_vertical = """
    INSERT INTO balance_vertical VALUES (0, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, NULL, NULL, 1);
    """ % \
                                  (gross_profit_list[j], sales_margin_list[j], roe_list[j], mbigr_list[j],
                                   net_profit_growth_rate_list[j], net_assets_growth_rate_list[j],
                                   rdiaapor_list[j], artd_list[j], inventory_turnover_days_list[j],
                                   sales_to_cash_ratio_list[j], current_ratio_list[j], quick_ratio_list[j],
                                   inventory_turnover_days_list[j], assets_and_liabilities_list[j],
                                   cash_short_debt_ratio_list[j], per_capita_output_value_list[j],
                                   per_capita_salary_list[j],
                                   seaapor_list[j], meaapor_list[j], ebitda_list[j]
                                   )
    try:
        cursor_insert.execute(sql_insert_balance_vertical)
        db.commit()
    except:
        db.rollback()
db.close()
