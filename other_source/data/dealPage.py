
from time import time
import requests
from lxml import etree
import json

res={
    'data':[]
}
#------------------------------获取缓存
with open('./data/ind.json','r',encoding='utf-8') as f:
    s=f.read()
    res=json.loads(s)
header_data={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
#------------------------------储存所有要获取的页面的地址
url_id=['']
for i in range(1,38):
    url_id.append('_'+str(i))
for id in url_id:
    #------------------------------获取响应
    url='http://xxgk.yq.gov.cn/yqsrmzf1/fdzdgknr_45346/lzyj/szfbgswj/index{id}.shtml'.format(id=id)
    resp=requests.get(url,headers=header_data,verify=False)
    resp.encoding='utf-8'
    text_content=resp.text
    #------------------------------查看响应源代码
    # with open("./data/page.html", 'w', encoding='utf-8') as f:
    #     print(text_content)
    #     f.write(text_content)
    # with open("./data/page.html", 'r', encoding='utf-8') as f:
    #     text_content=f.read()
    #     print(text_content)
    #------------------------------xpath处理
    parser=etree.HTMLParser(encoding='utf-8')
    tree=etree.HTML(text_content,parser=parser)
    title_list_pos='/html/body/div/div/div[3]/dl/dd[1]/dl/dd/ul/li/a'
    time_list_pos='/html/body/div/div/div[3]/dl/dd[1]/dl/dd/ul/li/em'
    time_list=tree.xpath(time_list_pos)
    title_list=tree.xpath(title_list_pos)

    # print(etree.tostring(tree,pretty_print=True).decode('utf-8'))
    for i,x in enumerate(time_list):
        cur={
            'title':title_list[i].attrib['title'].strip(),
            # 'title':title_list[i].text.strip(),
            'time':x.text.strip()
        }
        res['data'].append(cur)
        # print(cur)
        
with open('./data/ind.json','w',encoding='utf-8') as f:
    f.write(json.dumps(res,ensure_ascii=False))    


