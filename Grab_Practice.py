import requests
from bs4 import BeautifulSoup
import pandas as pd

def getBalanceSheet(stock_id, year, season):
    # 公開資訊觀測站 資產負債表網站
    url = 'https://mops.twse.com.tw/mops/web/t164sb03'

    # Post 資訊，從網站直接觀察
    form_data = {
        'encodeURIComponent': '1',
        'step': '1',
        'firstin': '1',
        'off': '1',
        'keyword4': '',
        'code1': '',
        'TYPEK2': '',
        'checkbtn': '',
        'queryName': 'co_id',
        'inpuType': 'co_id',
        'TYPEK': 'all',
        'isnew': 'false',
        'co_id': stock_id,
        'year': year,
        'season': season
    }

    # Request Web. Data
    r = requests.post(url, params=form_data)
    #To parser Web by Bs4
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.find('table', class_='hasBorder')

    #嘗試把網頁-body內容存在本機端
    with open('body.txt', 'w', encoding='utf-8') as file:
        file.write(body.prettify())
    # 處理 html form

    

    # 使用 pandas 幫忙，轉換為 Dataframe



    # 輸出成 csv 格式

    



    


    
stock = '2330'
year = '109'
season = '04'
getBalanceSheet(stock, year, season)
