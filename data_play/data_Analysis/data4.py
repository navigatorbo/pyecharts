import requests
import re
import json
import csv
import  pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s'%(stock_code,stock_code)
    try:
        r=requests.get(url)
    except ConnectionError as err:
        print(err)
    m=re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"',r.text)
    if m:
        quotes =json.loads(m[0])
        quotes=quotes[::-1]
    return [item for item in quotes if not 'type' in item]

if __name__ == '__main__':
    quotes = retrieve_quotes_historical('AXP')
    # print(quotes)
    list1= []
    for i in range(len(quotes)):
        x=date.fromtimestamp(quotes[i]['date'])
        y=date.strftime(x,'%Y-%m-%d')   #将时间戳转化为常见的时间形式
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes,index=list1)
    quotesdf_m = quotesdf_ori.drop(['adjclose'],axis=1)  #删除此列
    quotesdef = quotesdf_m.drop(['date'],axis=1)
    print(quotesdef)


