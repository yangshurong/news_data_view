import json
from json.tool import main
from re import sub
import requests
from lxml import etree
import random
import base64

from sqlalchemy import true

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

def get_num_tag():
  main_data={}
  with open('data\div_by_title.json', 'r', encoding='utf-8') as f:
    main_data = json.loads(f.read())
  res={}
  for sub_title,x_title in main_data.items():
    for time_info,x_time in x_title.items():
      if int(time_info)<2017 or int(time_info)>2021:continue
      for locate_name,x in x_time.items():
        if (locate_name in res)==False:res[locate_name]={}
        if (time_info in res[locate_name])==False:res[locate_name][time_info]={}
        if (vis[sub_title] in res[locate_name][time_info])==False:
          res[locate_name][time_info][vis[sub_title]]=[]
          res[locate_name][time_info][vis[sub_title]].append(['sub_title','avg','num'])
        res[locate_name][time_info][vis[sub_title]].append([sub_title,x['avg'],x['num'],x['sum']])  

  with open('data\deal_web_data\locate_tag_num_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))

def get_speed_average():  
  main_data={}
  with open('data\deal_web_data\locate_tag_num_1.json', 'r', encoding='utf-8') as f:
    main_data = json.loads(f.read())
  tmp_bar={}
  for locate_name,l_x in main_data.items():
      tmp_bar[locate_name]={}
      title_v={}
      for time,t_x in l_x.items():
        for title,title_x in t_x.items():
          for i in range(1,len(title_x)):
            cur=title_x[i]
            if (title in title_v)==False:
              title_v[title]={
                'sum':0,
                'num':0
              }
            title_v[title]['sum']+=cur[3]
            title_v[title]['num']+=cur[2]

      t_res={}
      for title,x in title_v.items():
        t_res[title]=x['sum']/x['num']
      tmp_bar[locate_name]=t_res

  tmp_scar={}
  for locate_name,l_x in main_data.items():
    title_v={}
    for time,t_x in l_x.items():
      for title,title_x in t_x.items():
        for i in range(1,len(title_x)):
          cur=title_x[i]
          if (title in title_v)==False:title_v[title]={}
          if (time in title_v[title])==False:
            title_v[title][time]={
              'sum':0,
              'num':0
            }
          title_v[title][time]['sum']+=cur[3]
          title_v[title][time]['num']+=cur[2]    
    t_res={}
    for title,t_x in title_v.items():
      t_res[title]=[]
      sort_obj={}
      for time,x in t_x.items():
        sort_obj[time]=x['sum']/x['num']
        # t_res[title].append([time,x['sum']/x['num']])
      sort_obj_keys=sorted(sort_obj.keys())
      for time in sort_obj_keys:
        t_res[title].append([time,sort_obj[time]])
    tmp_scar[locate_name]=t_res

  res={
    'bar':tmp_bar,
    'scar':tmp_scar
  }
  with open('data\deal_web_data\speed_average.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))

def get_main_tooltip():
  main_data={}
  with open('data\deal_web_data\locate_tag_num.json', 'r', encoding='utf-8') as f:
    main_data = json.loads(f.read())
  res={}  
  for locate,l_x in main_data.items():
    res[locate]={}
    for t,t_x in l_x.items():
      res[locate][t]=[]
      for m_title,m_x in t_x.items():
        cur={
          'value':0,
          'name':m_title,
          'children':[]
        }
        for i in range(1,len(m_x)):
          sub_title=m_x[i][0]
          avg=m_x[i][1]
          cur['value']+=avg
          cur['children'].append({
            'name':sub_title,
            'value':avg
          })
        res[locate][t].append(cur)   
  with open('data\deal_web_data\main_tooltip.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))    

def get_one_test():
  main_data={}
  with open('data\\all_info.json', 'r', encoding='utf-8') as f:
    main_data = json.loads(f.read())
  res=[]  
  for main_t,main_x in final_div.items():
    cur={
      'name':main_t,
      'children':[]
    }
    for sub_t in main_x:
      now_item={
        'name':sub_t,
        'children':[],
        'collapsed':random.randint(1,10)>2
      }
      now_info=main_data[sub_t]
      for _,_x in now_info.items():
        for tmp in _x:
          now_item['children'].append({
            'name':tmp['title'],
            'collapsed':True
          })
          if len(now_item['children'])>6:break

      cur['children'].append(now_item)
    res.append(cur)
  res=res[0]  
  with open('data\\deal_web_data\\test_mind_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))           

def deal_word_cloud_data():
  main_data={}
  with open(r'data\deal_web_data\word_cloud.json', 'r', encoding='utf-8') as f:
    main_data = json.loads(f.read())
  list_data=main_data['value']
  res={
    'value':[]
  }  
  for x in list_data:
    res['value'].append(x['name'])
    if len(res['value'])>35:break
  with open('data\\deal_web_data\\word_cloud_3ddata.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(res, ensure_ascii=False))        

deal_word_cloud_data()