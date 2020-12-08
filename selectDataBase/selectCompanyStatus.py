# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :selectCompanyStatus
# @Date     :2020/11/30 14:15
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql


def is_empty_basis_assets(company, years):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_assets where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_basis_cash(company, years):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_cash where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_basis_profit(company, years):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_profit where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_supplementary_data(company, years):
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from supplementary_data where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def select_all_company_and_status():
    db = pymysql.connect("localhost", "root", "admin", "grss")
    cur = db.cursor()
    sql = "select company_id,company_name from company"
    cur.execute(sql)
    result = cur.fetchall()
    aa = []
    for i in result:
        # print(i)
        a = []
        a.append(i)
        for j in range(2012, 2019):
            year_status =[]
            # 年份数组
            b = []
            b.append(j)

            year_status.append(j)
            year_status.append(is_empty_basis_assets(i[0], b))
            year_status.append(is_empty_basis_cash(i[0], b))
            year_status.append(is_empty_basis_profit(i[0], b))
            year_status.append(is_empty_supplementary_data(i[0], b))
            a.append(year_status)
        aa.append(a)
    return aa


select_all_company_and_status()
print(select_all_company_and_status())
