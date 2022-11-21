import json
import requests
def find_data_from_internet():
    header_data = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    find_list = {}
    with open('./data/main_id.json', 'r', encoding='utf-8') as f:
        s = f.read()
        find_list = json.loads(s)
    find_list = find_list['zhutitag']


    def get_one(theme):
        url = "http://xxgk.www.gov.cn/search-zhengce/?callback=jQuery1124033767114481781335_1651378507018&mode=smart&sort=relevant&page_index=1&page_size=2000&title=&theme={id}&_=1651378507030".format(
            id=theme)
        resp = requests.get(url, headers=header_data)
        resp.encoding = 'utf-8'
        text_content = resp.text
        f = text_content.find('(')
        # print('f',f)
        text_content = text_content[int(f+1):]
        text_content = text_content.strip()
        return text_content[:int(len(text_content)-1)]


    def deal(x):
        time_name = x['pubtime']
        title_name = x['title']
        time_name = time_name.replace('年', '-')
        time_name = time_name.replace('月', '-')
        time_name = time_name[:len(time_name)-1]
        cur = {
            'time':time_name,
            'title':title_name
        }
        return cur


    ans = {}
    for one_main_theme in find_list:
        main_name = one_main_theme['name']
        ans[main_name] = {}
        for sub_theme in one_main_theme['child']:
            sub_name = sub_theme['name']
            ans[main_name][sub_name] = []
            final_name = main_name+'\\'+sub_name
            print(final_name)
            res = get_one(final_name)
            res = json.loads(res)
            for x in res['data']:
                ans[main_name][sub_name].append(deal(x))



    with open('./data/find.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(ans, ensure_ascii=False))

def deal_data_to_time():
    all_name='./data/all_info.json'
    all_info={}
    with open(all_name,'r',encoding='utf-8') as f:
        all_info=json.loads(f.read())    
    res={}    
    for main_theme_name,main_theme in all_info.items():
        res[main_theme_name]={}
        # print(main_theme)
        for _sub,sub_theme in main_theme.items():
            for x in sub_theme:
                time_id=x['time'][0:4]
                print(time_id)
                print(time_id in res[main_theme_name])
                if (time_id in res[main_theme_name]) == False:
                    res[main_theme_name][time_id]=[]
                    # print(res[main_theme_name][time_id])
                res[main_theme_name][time_id].append(x)  
    with open('./data/find.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False))              

deal_data_to_time()