# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :processDocuments2
# @Date     :2020/11/23 4:32 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd

files_path = ['./Documents/new_basis_assets.xls',
              './Documents/new_basis_cash.xls',
              './Documents/new_basis_profit.xls']

df1 = pd.read_excel(files_path[0])
df2 = pd.read_excel(files_path[1])
df3 = pd.read_excel(files_path[2])

df1 = df1.drop('报表日期', 1)
df1 = df1.drop('单位', 1)
df1 = df1.drop('其他应收款', 1)
df1 = df1.drop('长期应付款', 1)
df1 = df1.drop('在建工程(合计)', 1)
df1 = df1.drop('少数股东权益', 1)

df2 = df2.drop('报表日期', 1)
df2 = df2.drop('单位', 1)
df2 = df2.drop('一、经营活动产生的现金流量', 1)
df2 = df2.drop('二、投资活动产生的现金流量', 1)
df2 = df2.drop('三、筹资活动产生的现金流量', 1)
df2 = df2.drop('附注', 1)

df3 = df3.drop('报表日期', 1)
df3 = df3.drop('单位', 1)
df3 = df3.drop('少数股东损益', 1)

old_columns1 = ["流动资产", "货币资金", "交易性金融资产", "衍生金融资产", "应收票据及应收账款", "应收票据", "应收账款", "应收款项融资", "预付款项",
                "其他应收款(合计)", "应收利息", "应收股利", "买入返售金融资产", "存货", "划分为持有待售的资产",
                "一年内到期的非流动资产", "待摊费用", "待处理流动资产损益", "其他流动资产", "流动资产合计", "非流动资产", "发放贷款及垫款", "可供出售金融资产", "持有至到期投资",
                "长期应收款", "长期股权投资", "投资性房地产", "在建工程", "工程物资",
                "固定资产及清理(合计)", "固定资产净额", "固定资产清理", "生产性生物资产", "公益性生物资产", "油气资产", "使用权资产", "无形资产", "开发支出", "商誉",
                "长期待摊费用",
                "递延所得税资产", "其他非流动资产", "非流动资产合计", "资产总计", "流动负债", "短期借款",
                "交易性金融负债", "应付票据及应付账款", "应付票据", "应付账款", "预收款项", "应付手续费及佣金", "应付职工薪酬", "应交税费", "其他应付款(合计)", "应付利息",
                "应付股利", "其他应付款", "预提费用", "一年内的递延收益", "应付短期债券", "一年内到期的非流动负债",
                "其他流动负债", "流动负债合计", "非流动负债", "长期借款", "应付债券", "租赁负债", "长期应付职工薪酬", "长期应付款(合计)", "专项应付款",
                "预计非流动负债", "递延所得税负债", "长期递延收益", "其他非流动负债", "非流动负债合计", "负债合计", "所有者权益", "实收资本(或股本)", "资本公积",
                "减：库存股", "其他综合收益", "专项储备", "盈余公积", "一般风险准备", "未分配利润", "归属于母公司股东权益合计", "所有者权益(或股东权益)合计",
                "负债和所有者权益(或股东权益)总计"
                ]
new_columns1 = [
    "current_assets",
    "money_funds",
    "transactional_financial_assets",
    "derivative_financial_assets",
    "notes_receivable_accounts_receivable",
    "bill_receivable",
    "accounts_receivable",
    "receivable_financing",
    "prepayments",
    "other_receivables",
    "interest_receivable",
    "dividend_receivable",
    "bfaura",
    "stock",
    "diahfs",
    "ncadwoy",
    "prepaid_expenses",
    "pcagal",
    "other_current_assets",
    "total_current_assets",
    "non_current_assets",
    "loans_and_advances",
    "available_sale_financial_assets",
    "held_to_maturity_investments",
    "long_term_receivables",
    "long_term_equity_investment",
    "Investment_real_estate",
    "construction_in_progress",
    "engineer_material",
    "fixed_assets_and_liquidation",
    "net_fixed_assets",
    "fixed_assets_liquidation",
    "productive_biological_assets",
    "public_welfare_biological_assets",
    "oil_and_gas_asset",
    "right_of_use_asset",
    "intangible_assets",
    "development_expenditure",
    "goodwill",
    "long_term_prepaid_expenses",
    "deferred_tax_assets",
    "other_non_current_assets",
    "total_non_current_assets",
    "total_assets",
    "current_liabilities",
    "short_term_loan",
    "transactional_financial_liabilities",
    "notes_payable_accounts_payable",
    "bills_payable",
    "accounts_payable",
    "advance_receipt",
    "fees_and_commissions",
    "employee_compensation_payable",
    "taxes_payable",
    "other_payables_total",
    "interest_payable",
    "dividend_payable",
    "other_payables",
    "accrued_fees",
    "deferred_within_one_year",
    "short_term_bonds_payable",
    "current_liabilities_one_year",
    "other_current_liabilities",
    "total_current_liabilities",
    "non_current_liabilities",
    "long_term_loan",
    "bonds_payable",
    "lease_liability",
    "ltecp",
    "long_term_payables",
    "special_payables",
    "estimated_non_current_liabilities",
    "deferred_income_tax_liabilities",
    "long_term_deferred_income",
    "other_non_current_liabilities",
    "total_non_current_liabilities",
    "total_liabilities",
    "owners_equity",
    "paid_in_capital_or_equity",
    "capital_reserve",
    "less_treasury_stock",
    "other_comprehensive_income",
    "special_reserves",
    "surplus_reserve",
    "general_risk_preparation",
    "undistributed_profit",
    "teatsotpc",
    "toeose",
    "tlaoeose"

]

old_columns2 = ['销售商品、提供劳务收到的现金', '收到的税费返还', '收到的其他与经营活动有关的现金', '经营活动现金流入小计', '购买商品、接受劳务支付的现金',
                '支付给职工以及为职工支付的现金', '支付的各项税费', '支付的其他与经营活动有关的现金',
                '经营活动现金流出小计', '经营活动产生的现金流量净额', '收回投资所收到的现金', '取得投资收益所收到的现金',
                '处置固定资产、无形资产和其他长期资产所收回的现金净额', '处置子公司及其他营业单位收到的现金净额', '收到的其他与投资活动有关的现金',
                '投资活动现金流入小计', '购建固定资产、无形资产和其他长期资产所支付的现金', '投资所支付的现金', '取得子公司及其他营业单位支付的现金净额', '支付的其他与投资活动有关的现金',
                '投资活动现金流出小计', '投资活动产生的现金流量净额',
                '吸收投资收到的现金', '其中：子公司吸收少数股东投资收到的现金', '取得借款收到的现金', '发行债券收到的现金', '收到其他与筹资活动有关的现金', '筹资活动现金流入小计',
                '偿还债务支付的现金', '分配股利、利润或偿付利息所支付的现金', '其中：子公司支付给少数股东的股利、利润',
                '支付其他与筹资活动有关的现金', '筹资活动现金流出小计', '筹资活动产生的现金流量净额', '四、汇率变动对现金及现金等价物的影响', '五、现金及现金等价物净增加额',
                '加:期初现金及现金等价物余额', '六、期末现金及现金等价物余额', '净利润', '少数股东权益', '未确认的投资损失',
                '资产减值准备', '固定资产折旧、油气资产折耗、生产性物资折旧', '无形资产摊销', '长期待摊费用摊销', '待摊费用的减少', '预提费用的增加', '处置固定资产、无形资产和其他长期资产的损失',
                '固定资产报废损失', '公允价值变动损失', '递延收益增加（减：减少）', '预计负债', '财务费用',
                '投资损失', '递延所得税资产减少', '递延所得税负债增加', '存货的减少', '经营性应收项目的减少', '经营性应付项目的增加', '已完工尚未结算款的减少(减:增加)',
                '已结算尚未完工款的增加(减:减少)', '其他', '经营活动产生现金流量净额', '债务转为资本', '一年内到期的可转换公司债券',
                '融资租入固定资产', '现金的期末余额', '现金的期初余额', '现金等价物的期末余额', '现金等价物的期初余额', '现金及现金等价物的净增加额'
                ]
new_columns2 = [
    'crfsgapls',
    'tax_refund',
    'ocrrtoa',
    'socifoa',
    'cpfpgarls',
    'cptfe',
    'various_taxes_paid',
    'oprtoa',
    'socofoa',
    'ncffoa',
    'crfi',
    'crfii',
    'ncrfdofaiaaolta',
    'ncrfdosaobu',
    'ocrrtia',
    'soifia',
    'cpftpacofaiaaolta',
    'cash_paid_for_investment',
    'otncpbsaobu',
    'ocprtia',
    'socofia',
    'ncffia',
    'acrfi',
    'icrbsfamsi',
    'gcrfb',
    'crfiob',
    'rocrtfa',
    'sociffa',
    'cpfdr',
    'cpfdodpoip',
    'idappbstms',
    'pocrtfa',
    'socoffa',
    'ncfffa',
    'eotcotexrocate',
    'niicace',
    'abocaceatbotp',
    'bocaceateotp',
    'net_profit',
    'minority_interests',
    'unrecognized_investment_loss',
    'impairment_of_assets',
    'dofadooagadopm',
    'amortization_of_intangible_assets',
    'aoltde',
    'rope',
    'increase_accrued_expenses',
    'lodofaiaaolta',
    'lfsfa',
    'lfcifv',
    'increase_in_deferred_revenue',
    'estimated_liabilities',
    'financial_expenses',
    'investment_loss',
    'decrease_deferred_income',
    'iiditl',
    'decrease_in_inventory',
    'decrease_in_operating_receiv,ables',
    'increase_in_operating_payables',
    'reduction_completed_unsettled_payments',
    'increase_settled_unfinished_payment',
    'other',
    'from_operating_activities',
    'conversion_of_debt_capital',
    'ccbdwoy',
    'flofa',
    'ending_balance_of_cash',
    'opening_balance_of_cash',
    'ending_balance_cash_equivalents',
    'opening_balance_cash_equivalents',
    'cash_and_cash_equivalents'
]

old_columns3 = [
    '一、营业总收入', '营业收入', '二、营业总成本', '营业成本', '营业税金及附加', '销售费用', '管理费用', '财务费用', '研发费用', '资产减值损失', '公允价值变动收益',
    '投资收益', '其中:对联营企业和合营企业的投资收益', '汇兑收益',
    '三、营业利润', '加:营业外收入', '减：营业外支出', '其中：非流动资产处置损失', '四、利润总额', '减：所得税费用', '五、净利润', '归属于母公司所有者的净利润', '六、每股收益',
    '基本每股收益(元/股)', '稀释每股收益(元/股)',
    '七、其他综合收益', '八、综合收益总额', '归属于母公司所有者的综合收益总额', '归属于少数股东的综合收益总额'
]
new_columns3 = [
    'total_operating_income',
    'operating_income',
    'total_operating_costs',
    'operating_costs',
    'business_tax_and_surcharges',
    'sales_expense',
    'management_costs',
    'financial_expenses',
    'rd_expenses',
    'asset_impairment_loss',
    'Income_changes_in_value',
    'investment_income',
    'iiifaajv',
    'exchange_gains',
    'operating_profit',
    'anoi',
    'lnoe',
    'llodonca',
    'the_total_profit',
    'deduct_income_tax_expense',
    'net_profit',
    'trpbttpco',
    'earnings_per_share',
    'basic_earnings_per_share',
    'diluted_earnings_per_share',
    'other_comprehensive_income',
    'total_comprehensive_income',
    'tciatootp',
    'tciatms'
]

# 更改列名称
for i in range(0, 89):
    df1 = df1.rename(columns={str(old_columns1[i]): str(new_columns1[i])})
df1['company_year'] = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004,
                       2003, 2002]
df1['company_name'] = ['兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝',
                       '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝']
df1['company_id'] = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

for i in range(0, 71):
    df2 = df2.rename(columns={str(old_columns2[i]): str(new_columns2[i])})
df2['company_year'] = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004]
df2['company_name'] = ['兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝',
                       '兔宝宝', '兔宝宝']
df2['company_id'] = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

for i in range(0, 29):
    df3 = df3.rename(columns={str(old_columns3[i]): str(new_columns3[i])})

    df3['company_year'] = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005,
                           2004, 2003, 2002]
    df3['company_name'] = ['兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝',
                           '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝', '兔宝宝'
                           ]
    df3['company_id'] = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

df1.to_excel('./Documents/final_basis_assets.xls', index=False)
df2.to_excel('./Documents/final_basis_cash.xls', index=False)
df3.to_excel('./Documents/final_basis_profit.xls', index=False)
print('Done!')
