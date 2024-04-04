import requests
from bs4 import BeautifulSoup


def getTX(Date_ID):
    #期交所 
    url = 'https://www.taifex.com.tw/cht/3/futAndOptDate'

    # Post 資訊，
    form_data = {
        'queryType': '1',
        'goDay': '',
        'dateaddcnt': '-1',
        'doQuery': '1',
        'queryDate': Date_ID
    }


   # 发送HTTP请求获取网站的HTML内容
    response = requests.post(url, params= form_data )

    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')        
        tr_element = soup.find_all('tr', class_='12bk')
            
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



if __name__ == "__main__":

    Date = '2024/03/30'
    getTX(Date)
