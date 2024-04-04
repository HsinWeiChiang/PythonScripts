import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_website_data(url):
    # 发送HTTP请求获取网站的HTML内容
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')









        
        tr_element = soup.find_all('tr', class_='12bk')
        values = []

        
        for tr in tr_element:
            tds = tr.find_all('td')
            for td in tds:
                #print(td.text)
                td_cleaned_string = td.text.strip()

                print(td_cleaned_string)
                
               
                    
            


            
            #b_tags = tr.find_all('b')
            #for b_tag in b_tags:
            #    print(b_tag.text)
           

       
    else:
        print("请求失败，状态码：", response.status_code)


url = 'https://www.taifex.com.tw/cht/3/futAndOptDate'
get_website_data(url)
