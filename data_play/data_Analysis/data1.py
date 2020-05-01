import requests
import re
import pandas as pd
import csv

def retrieve_dji_list():
    r= requests.get('https://money.cnn.com/data/dow30/')
    search_pattern =re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text =re.findall(search_pattern,r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0],item[1],float(item[2])])
    return dji_list_in_text

if __name__ == '__main__':
    dji_list= retrieve_dji_list()
    # print(dji_list)
    djidf = pd.DataFrame(dji_list)
    clos = ['core','name','lasttrade']
    djidf.columns = clos
    # print(djidf)

    # print(list(djidf.index)) #显示行索引
    # print(djidf.values) #显示数值的值
    # print(djidf.describe) #显示数据描述
    # print(djidf.head(5))  #显示前五行  也可以用切片的方法，即djidf[:5]

