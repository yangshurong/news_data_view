import math
from lxml import etree
import json
import datetime
import random
locate_name = r'data\shanxi_data\jinzhong.json'
now_locate = "晋中"
all_name = r'data\all_info_time.json'
is_first = False
locate_info = {}
has_show_same_num=0
final_div={
  '政治':['国务院组织机构', '综合政务','公安、安全、司法', '民政、扶贫、救灾'
  , '民族、宗教', '对外事务', '港澳台侨工作', '国防'],
  '经济':['国民经济管理、国有资产监管', '财政、金融、审计'],
  '资源':['国土资源、能源', '农业、林业、水利'],
  '生产':['工业、交通', '商贸、海关、旅游', '市场监管、安全生产监管', '城乡建设、环境保护'],
  '文化':['科技、教育', '文化、广电、新闻出版'],
  '民生':['卫生、体育', '人口与计划生育、妇女儿童工作', '劳动、人事、监察'],
}
vis={}
for k,x in final_div.items():
  for i in x:
    vis[i]=k

with open(locate_name, 'r', encoding='utf-8') as f:
    locate_info = json.loads(f.read())


def fail_equal(a, b):
    num = len(b)
    ans = 0
    for i in b:
        if a.find(i) != -1:
            ans = ans+1
    if ans > num*0.6:
        return False
    else:
        return True


def find_locate_time(policy_name, lim_d):
    global has_show_same_num
    ans = 10000000
    final_title=''
    for item_policy in locate_info['data']:
        t = item_policy['time']+' 00:00:00'
        t=change(t)
        cur_d = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
        delt_day = (cur_d-lim_d).days
        if delt_day < 0:
            continue
        if fail_equal(item_policy['title'], policy_name) == True:
            continue
        has_show_same_num+=1
        if ans>delt_day:
            ans =delt_day
            final_title=item_policy['title']
    if ans == 10000000 or ans > 400:
        ans = -1
    return ans,final_title


def work_for_tag():
    all_info = {}
    with open(all_name, 'r', encoding='utf-8') as f:
        all_info = json.loads(f.read())

    res = {}
    final_ans_position = './data/find.json'
    if is_first == False:
        with open(final_ans_position, 'r', encoding='utf-8') as f:
            res = json.loads(f.read())
    sum_num = 0
    for fr_name, fr_value in all_info.items():
        if is_first == True:
            res[fr_name] = {}
        for se_name, se_value in fr_value.items():
            if is_first == True:
                res[fr_name][se_name] = {}
            num = 0
            sum_days = 0
            for item_policy in se_value:
                this_time = item_policy['time']+" 00:00:00"
                d1 = datetime.datetime.strptime(this_time, '%Y-%m-%d %H:%M:%S')
                d2=find_locate_time(item_policy['title'],d1,)
                if d2==-1:continue
                num+=1
                sum_days+=d2
            if num == 0:
                continue
            # print("sum_days",sum_days,'nums',num)
            res[fr_name][se_name][now_locate] = {}
            res[fr_name][se_name][now_locate]['num'] = num
            res[fr_name][se_name][now_locate]['sum'] = sum_days
            res[fr_name][se_name][now_locate]['avg'] = sum_days/num

    print('sum_num', sum_num)
    with open(final_ans_position, 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False))

def work_for_time():
    all_info = {}
    with open(all_name, 'r', encoding='utf-8') as f:
        all_info = json.loads(f.read())

    res = {}
    final_ans_position = r'data\find.json'
    if is_first == False:
        with open(final_ans_position, 'r', encoding='utf-8') as f:
            res = json.loads(f.read())
    sum_num = 0
    for fr_name, fr_value in all_info.items():
        if is_first == True:
            res[fr_name] = {}
        for se_name, se_value in fr_value.items():
            if is_first == True:
                res[fr_name][se_name] = {}
            num = 0
            sum_days = 0
            # print(fr_name,se_name)
            for item_policy in se_value:
                sum_num = sum_num+1
                this_time = item_policy['time']+" 00:00:00"
                d1 = datetime.datetime.strptime(this_time, '%Y-%m-%d %H:%M:%S')
                d2=find_locate_time(item_policy['title'],d1)
                if d2==-1:continue
                
                num+=1
                sum_days+=d2
            if num == 0:
                continue
            # print("sum_days",sum_days,'nums',num)
            res[fr_name][se_name][now_locate] = {}
            res[fr_name][se_name][now_locate]['num'] = num
            res[fr_name][se_name][now_locate]['sum'] = sum_days
            res[fr_name][se_name][now_locate]['avg'] = sum_days/num
            # print('num', num,'sum',sum_days)

    with open(final_ans_position, 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False))

def change(this_time):
    this_time=this_time.replace('年','-')
    this_time=this_time.replace('月','-')
    this_time=this_time.replace('日','')
    return this_time

def work_for_city():
    all_info = {}
    with open(all_name, 'r', encoding='utf-8') as f:
        all_info = json.loads(f.read())

    res = {}
    final_ans_position = r'data\find.json'
    if is_first == False:
        with open(final_ans_position, 'r', encoding='utf-8') as f:
            res = json.loads(f.read())
    sum_num = 0
    res[now_locate]={}
    for _name, fr_value in all_info.items():
        if _name=='其他':continue
        fr_name=vis[_name]        
        # 大主题
        for se_name, se_value in fr_value.items():
            time_value=int(se_name)
            if time_value>2021 or time_value<2017:continue
            # year
            num = 0
            sum_days = 0
            # print(fr_name,se_name)
            list_new=[]
            for item_policy in se_value:
                # sum_num = sum_num+1
                this_time = item_policy['time']+" 00:00:00"
                this_time=change(this_time)
                d1 = datetime.datetime.strptime(this_time, '%Y-%m-%d %H:%M:%S')
                d2,resp_title=find_locate_time(item_policy['title'],d1)
                if d2==-1:continue                
                num+=1
                sum_days+=d2
                list_new.append({
                    'name':resp_title,
                    'collapsed':random.randint(0,10)>5
                })
            if num == 0:
                continue
            # print("sum_days",sum_days,'nums',num)
            if (se_name in res[now_locate])==False:res[now_locate][se_name]={}
            if (fr_name in res[now_locate][se_name])==False:
                res[now_locate][se_name][fr_name]={
                    'num':0,
                    'sum':0,
                }
            res[now_locate][se_name][fr_name]['num']+=num
            res[now_locate][se_name][fr_name]['sum']+=sum_days
            # print('num', num,'sum',sum_days)

    with open(final_ans_position, 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False))

def work_final_city():
    all_info = {}
    with open(r'data\speed_data.json', 'r', encoding='utf-8') as f:
        all_info = json.loads(f.read())
    for f_name, fr_value in all_info.items():
        for s_name, se_value in fr_value.items():
            sum_t=0
            num_t=0
            for t_name, t_value in se_value.items():
                if t_name=='avg':continue
                sum_t+=all_info[f_name][s_name][t_name]['sum']
                num_t+=all_info[f_name][s_name][t_name]['num']
            all_info[f_name][s_name]['avg']=sum_t/num_t        
    with open(r'data\speed_data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(all_info, ensure_ascii=False))            

work_final_city()