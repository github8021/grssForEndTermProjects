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
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_assets where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_basis_cash(company, years):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_cash where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_basis_profit(company, years):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from basis_profit where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


def is_empty_supplementary_data(company, years):
    db = pymysql.connect("localhost", "root", "root", "grss")
    cur = db.cursor()
    for year in years:
        sql = "select * from supplementary_data where company_id=%s and company_year=%s"
        cur.execute(sql, (company, year))
        result = cur.fetchall()
        if (result):
            return True
    return False


