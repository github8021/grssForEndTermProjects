# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :operateFormula
# @Date     :2020/12/14 7:57 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

db_username = 'root'
db_password = 'root1234'
db_name = 'grss'
db = pymysql.connect("localhost", db_username, db_password, db_name)

# cursor
cursor = db.cursor()
def showFormula(formula_table,result_name):
    cursor.execute("select formula from calculate_formula where formula_table=%s and result_name=%s" %
                   (formula_table, result_name))
    result = cursor.fetchone()
    return result

# print(showFormula("'基础指标表'","'销售毛利率'"))

def updateFormula(formula_table,result_name,updateResult):
    try:
        cursor.execute("update calculate_formula set formula=%s where formula_table=%s and result_name=%s" %
                       (updateResult, formula_table, result_name))
        db.commit()
    except:
        db.rollback()
    print('Done!')
    return True

# updateFormula("'基础指标表'","'销售毛利率'","'(基础利润表)营业收入-(基础利润表)营业成本/(基础利润表)营业收入'")
