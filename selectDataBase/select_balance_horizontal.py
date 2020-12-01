# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :grssForEndTermProjects
# @File     :select_balance_vertical
# @Date     :2020/12/1 11:39 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
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

# cursor
cursor = db.cursor()

def select_balance_horizontal(known_table,known_table_attribute,company_id):
    tablelist=[]
    columnlist=[]
    alist = []
    cursor.execute('select original_table,original_table_attribute from calculate_reference where known_table = %s and known_table_attribute = %s '%
                   (known_table,known_table_attribute))
    result = cursor.fetchall()
    for i in result:
        tablelist.append(i[0])
        columnlist.append(i[1])
    # print(tablelist)
    # print(columnlist)
    for listnum in range(0, len(result)):
        cursor.execute("select %s from %s where company_id=%d" %
                       (columnlist[listnum], tablelist[listnum],company_id))
        result1 = cursor.fetchall()
        for i in result1:
            alist.append(i[0])
    print(alist)
    return alist
select_balance_horizontal("'balance_horizontal'","'meaapor'",1)
