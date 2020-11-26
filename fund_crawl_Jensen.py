import statsmodels.api as sm
import akshare as ak
import pandas as pd
import numpy as np
import random
import os

code_num = 10
index_code = 'sh000300'

codes = pd.read_excel('fund_codes.xlsx', index_col=0, dtype={'基金代码': 'object'})['基金代码']

# 获取指数组合index_code的收益率数据
df_M = ak.stock_zh_index_daily_em(symbol=index_code)
df_M['updown'] = 0.0
for index, row in df_M.iterrows():
    if index > 0:
        df_M['updown'][index] = (float(row['close']) - float(df_M['close'][index-1])) / float(df_M['close'][index-1])
df_M = df_M[['date', 'updown']]

# 获取最新Shibor作为无风险收益率
df_rf = ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="3月", need_page="1")
print('无风险利率:' + str(df_rf['利率(%)'][0]) + '%\n')
rf = np.power(1+df_rf['利率(%)'][0]/100, 1/360)-1  # 转为日利率

# 随机抽取code_num只基金获取收益率数据并回归
codes = random.sample(list(codes), code_num)
print('基金代码' + '\t' + 'Alpha的T值')
for code in codes:
    df_i = ak.fund_em_open_fund_info(fund=code, indicator="单位净值走势").rename(columns={'x': 'date'})
    for index, row in df_i.iterrows():
        df_i['净值日期'][index] = str(df_i['净值日期'][index])
        if index > 0:
            df_i['日增长率'][index] = (float(row['单位净值']) - float(df_i['单位净值'][index-1])) / float(df_i['单位净值'][index-1])
    df_i = df_i[['净值日期', '日增长率']]
    df = pd.merge(df_M, df_i, how='inner', left_on='date', right_on='净值日期')
    y = df['日增长率'].values - rf
    x = sm.add_constant(df['updown'].values - rf)
    df['Ri'] = y
    df['Rm'] = df['updown'].values - rf
    df.to_excel('./原始数据/' + code + '.xlsx')
    model = sm.OLS(endog=y, exog=x).fit()
    print(code + '\t' + str(model.tvalues[0]))

os.system('pause')
