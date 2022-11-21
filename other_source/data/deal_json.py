
import requests
from lxml import etree
import json

res={
    'data':[]
}
# with open('./data/ind.json','r',encoding='utf-8') as f:
#     s=f.read()
#     res=json.loads(s)
header_data={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url_id=[]
for i in range(1,3):
    url_id.append(str(i))
for id in url_id:
    # -------------------------------获取响应
    url=r'http://infogate.jl.gov.cn/govsearch/jsonp/zf_jd_list.jsp?page={id}&lb=134657&callback=result&sword=&searchColumn=all&searchYear=all&pubURL=http%3A%2F%2Fxxgk.jl.gov.cn%2F&SType=1&searchYear=all&pubURL=&SType=1&channelId=134657&_=1651314237358'.format(id=id)  
    resp=requests.get(url,headers=header_data)
    resp.encoding='utf-8'
    text_content=resp.text
    text_content=text_content[55:len(text_content)-1]
    # -------------------------------查看获取到的响应
    with open("./data/page.json", 'w', encoding='utf-8') as f:
        print(text_content)
        f.write(text_content)
    all_info=json.loads(text_content)['data']
    for i,x in enumerate(all_info):
        in_data=x['tip']
        cur={
            'title':x['tip']['title'],
            'time':x['tip']['dates']
        }
        res['data'].append(cur)
        print(cur)
        if i%50==0:
            with open('./data/ind.json','w',encoding='utf-8') as f:
                f.write(json.dumps(res,ensure_ascii=False))    
        
with open('./data/ind.json','w',encoding='utf-8') as f:
    f.write(json.dumps(res,ensure_ascii=False))   


