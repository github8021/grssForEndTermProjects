# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :paDocuments
# @Date     :2020/11/23 3:33 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

# 设置headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# 1.找到文档url
# 兔宝宝现金流量、兔宝宝利润、兔宝宝资产负债
urls = ['http://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/002043/ctrl/all.phtml',
        'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/002043/ctrl/all.phtml',
        'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/002043/ctrl/all.phtml'
        ]
sheetName = ['basis_cash', 'basis_profit', 'basis_assets']
for i in range(0, len(urls)):
    print(urls[i])
    response = requests.get(url=urls[i], headers=headers).content
    with open('./Documents/{}.xls'.format(sheetName[i]), 'wb')as fp:
        fp.write(response)
