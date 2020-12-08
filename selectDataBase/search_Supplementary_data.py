# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects1
# @File     :search_Supplementary_data
# @Date     :2020/12/1 14:13
# @Author   :陈荣
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
#查询基础表——辅助数据表
import pymysql

def search_Supplementary_data(company_id,company_years):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='fangpiisyou',  # 密码
        db='grss',  # 库名
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cursor = db.cursor()
    a = list()
    for company_year in company_years:
        cursor.execute("""select total_number_employees,profit_before_interest_tax,nterest_payments,ebitda,gasoline_usage,
                          gasoline_density,water_use,water_resource_utilization_density,power_usage,power_usage_density,
                          gas_usage,natural_gas_density,packing_material_usage,packing_material_density,greenhouse_gas_emissions,
                          greenhouse_gas_emission_density,harmless_waste_discharge,harmless_waste_discharge_density,hazardous_waste_discharge,edhwg
                          from supplementary_data
                          where company_id=%s and company_year=%s""",(company_id, company_year))
        result = cursor.fetchall()[0]
        a.append(result)
    print(a)
    return a

search_Supplementary_data(1,[2018,2019])

