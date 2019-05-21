# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import os
import sys
import telegram
from pymongo import MongoClient

# Regex expression
import re
import urllib
import time
#import codecs

main_url = 'http://www.ppomppu.co.kr/zboard/zboard.php'
title_link = 'https://m.ppomppu.co.kr/new/bbs_view.php'

main_params = {
  'id' : 'phone'
}

headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.53.4 Safari/537.36'}

#@ppomppu_monitoring
#monitor_start('localhost','5555','/postanal/?post=',1,'Y','KT','Y','localhost','27017','50026600','629922483:AAGIdLbJN4dHhOgI02TawJAe4CHFymsJOcI')
def monitor_start(p_host,p_port,p_param,p_count,p_text_yn,p_kt,p_db_save,p_db_host,p_db_port,p_chat_id,p_token_id):
    m_soup = get_soup(main_url,main_params,headers)
    get_title(m_soup,p_host,p_port,p_param,p_count,p_text_yn,p_db_save,p_db_host,p_db_port,p_chat_id, p_token_id)

# weppage crawing 으로 리스트 가져오기  
def get_soup(p_url,p_params,p_headers):
    resp = requests.get(p_url, params = p_params, headers = p_headers)
    resp.encoding = 'euc-kr'
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(resp.text)
    return soup

#  번호 / 제목 가져오기 
def get_title(p_soup,p_host,p_port,p_param,p_count,p_text_yn,p_db_save,p_db_host,p_db_port, p_chat_id,p_token_id):
    v_count = 0
    v_str_list = []
    p_lists = p_soup.findAll('tr', {'class': ['list0','list1']})
    for idx, p_list in enumerate(p_lists,1):   
        #   번호 가져오기 <td class='eng list_vspace' colspan=2>3510256</td>
        num = p_list.select('td[class="eng list_vspace"]')
        num_val = num[0].contents[0].strip()
        #   제목 가져오기 <font class=list_title>죽기전까지 완전 자급제는 안될려나보네요..</font>
        titles = p_list.select('font[class=list_title]')
        title = titles[0].contents[0].strip()
        # 값이 있으면 skip
        #if p_db_save == 'N' :
        #   continue
        if check_db(p_db_host,p_db_port,num_val,title) == 0 :
           continue
        params_link = {
           'id' : 'phone',
           'no' : num_val
        }
        body_str = get_contents(title_link,params_link,title,headers)
#        print(body_str)
        carrier = validate_carrier(p_host,p_port,p_param,body_str,headers)
        if carrier == '<answer>KT</answer>':
           v_count = v_count + 1
       	   v_str = '<a href=\"' + title_link + '?id=phone&no=' + num_val + '\">['+ num_val + ']</a>' + ' : ' +title
           v_str_list.append(v_str)
    if v_count > int(p_count):
        msg_notify(v_count,v_str_list,p_chat_id,p_token_id)

# 본문 보기    
def get_contents(p_url, p_params, p_title, headers):  
    soup_link = get_soup(p_url,p_params,headers)
    link_lists = soup_link.find_all("div", {"class":"cont"})
    body_str = '' 
    for idx,link_list in enumerate(link_lists,1):
        body_str = body_str + link_list.get_text().replace('\n\r','')
    body_str = p_title + body_str
    return body_str

# 통신사 확인
def validate_carrier(p_host,p_port,p_param,p_req_str,headers):
    #url_ai = 'http://localhost:5555/postanal/?post=나는kt가  좋아'
    url_ai = 'http://' + p_host + ':' + p_port + p_param + p_req_str
#    url_ai = 'http://' + p_host + ':' + p_port + p_param + urllib.quote(p_req_str)   
    resp_ai = requests.get(url_ai, headers = headers)
    resp_ai.encoding = 'euc-kr'
    print(resp_ai.text)
    return resp_ai.text   

# message 전송
def msg_notify(p_count,p_str_list,p_chat_id,p_token_id):
    #my_token = '676003420:AAGIdLbJN4dHhOgI02TawJAe4CHFymsJOcI'
    my_token = p_token_id
    bot = telegram.Bot(token = my_token)
    chat_id = p_chat_id #50026600
    title_text = '뽐뿌 게시판에서 KT 관련 메시지가 ' + str(p_count) + ' 건 발생했습니다'
    bot.sendMessage(chat_id = chat_id, text=title_text)
    for ret_val in p_str_list:
        bot.sendMessage(chat_id = chat_id, text=ret_val,parse_mode='html')


def check_db(p_host,p_port,p_header,p_body):
    conn = MongoClient(p_host + ':' + p_port)
    db = conn.test_db
    collect = db.collect
    doc1 = {p_header:p_body}
    if collect.find({p_header:p_body}).count() > 0 :
       return 0
    else:
       collect.insert(doc1)
       return 1

#monitor_start('localhost','5555','/postanal/?post=',1,'N','KT','Y','localhost','27017','50026600','676003420:AAH7fq_HZzxbmWurz-IWdeUh6vZN1QTQxsE')

