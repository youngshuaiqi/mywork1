import requests
import bs4
import os
kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
url = 'https://www.baidu.com/s?wd=%E6%9D%A8%E5%B8%85%E6%97%97&rsv_spt=1&rsv_iqid=0xbe10f4b200078221&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=16&rsv_sug1=16&rsv_sug7=100'
titles_urls = []
response = requests.get(url,headers = kv)
status_code = response.status_code
content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
for i in range(1,11):
    element = content.find_all(id=i)
    for per in element:
        psrc = per.find_all(class_='c-tools')
        for a in psrc:
            b = str(a)
            d = b.find('{')
            c = b.find('}')
            title_url = b[d:c+1]
            titles_urls.append(title_url)
print(titles_urls)
os.system("pause")