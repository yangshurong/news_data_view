import requests
from lxml import etree
import json
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
def change(s):
    s=s.replace('年','-')
    s=s.replace('月','-')
    return s[0:10]
web = Chrome()
web.get('https://zwgk.sxxz.gov.cn/xzsrmzf/wj/zfwj/xzf/index.shtml')
# with open("./data/page.html", 'w', encoding='utf-8') as f:
#     f.write(web.page_source)
#     print(web.page_source)
time.sleep(3)

res = {
    'data': []
}
# with open('./data/ind.json','r',encoding='utf-8') as f:
#     s=f.read()
#     res=json.loads(s)
nxt_tab_pos = '/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div/a[3]'
titles_pos = '/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/ul[2]/li/ul/li[6]'
times_pos = '/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/ul[2]/li/ul/li[8]'
for _ in range(130):
    titles = web.find_elements(by=By.XPATH, value=titles_pos)
    times_list = web.find_elements(by=By.XPATH, value=times_pos)
    # titles=titles[1:]
    # times_list=times_list[1:]
    # 第一个不要
    for i, x in enumerate(titles):
        cur_time=times_list[i].text
        cur_time=change(times_list[i].text)
        # 如果要是从2021年4月6日这种的转换的话
        cur_data = {
            'title': x.text,
            'time': cur_time
        }
        print(cur_data)
        res['data'].append(cur_data)
    if _ % 1 == 0:
        with open('./data/ind.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(res, ensure_ascii=False))
    nxt_tab = web.find_element(by=By.XPATH, value=nxt_tab_pos).click()
    time.sleep(3)
with open('./data/ind.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))

#     f.write(resp.text)
