import requests
import pandas as pd

def download_taifex_data(url):
    # 发送HTTP请求获取CSV文件内容
    response = requests.get(url)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 使用pandas读取CSV文件内容
        df = pd.read_csv(url)
        return df
    else:
        print("请求失败，状态码：", response.status_code)
        return None

# 三大法人数据的URL地址
url = "https://www.taifex.com.tw/cht/3/futAndOptDate"
# 调用函数并传入URL
taifex_data = download_taifex_data(url)

# 打印数据的前几行
print(taifex_data.head())
