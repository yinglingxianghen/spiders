#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: xinlan time:2017/09/02
import re
import json
import requests
import xlwt
# 信息
DATA = []
# url列表
urls = []
# 查找关键字
find_content = u'python视频'
# 初始的url
first_url = 'https://s.taobao.com/search?imgfile=&\
js=1&stats_click=search_radio_all%3A1&\
initiative_id=staobaoz_20170902&ie=utf8'
urls.append(first_url)

for i in range(1, 10):
    temp = 'https//s.taobao.com/search?&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170902&ie=utf8&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48&data-key=s&data-value={}'.format(i*44)
    urls.append(temp)
for url in urls:
    # 说明做了限制,有问题，后面解决
    print (url)

for url in urls:
    # 发送http请求
    r = requests.get(urls[1], params={'q': find_content})
    html = r.text

    # 通过正则表达式获取需要的信息
    content = re.findall(r'g_page_config = .*g_srp_loadCss', html, re.S)[0]

    content = re.findall(r'{.*}', content)[0]

    # 处理成字典
    content = json.loads(content)
    # 获取信息列表
    data_list = content['mods']['itemlist']['data']['auctions']
    for item in data_list:
        temp={
            'title': item['title'],
            'view_price': item['view_price'],
            'view_sales': item['view_sales'],
            'view_fee': '否' if float(item['view_fee']) else '是',
            'isTmall': '是' if item['shopcard']['isTmall'] else '否',
            'area': item['item_loc'],
            'name': item['nick'],
            'detail_url': item['detail_url'],
        }
        DATA.append(temp)
# 持久化
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
# 写标题
sheet01.write(0, 0, '标题')
sheet01.write(0, 1, '标价')
sheet01.write(0, 2, '购买人数')
sheet01.write(0, 3, '是否包邮')
sheet01.write(0, 4, '是否天猫')
sheet01.write(0, 5, '地区')
sheet01.write(0, 6, '店名')
sheet01.write(0, 7, 'url')

# 写内容
for i in range(len(DATA)):
    sheet01.write(i+1, 0, DATA[i]['title'])
    sheet01.write(i+1, 1, DATA[i]['view_price'])
    sheet01.write(i+1, 2, DATA[i]['view_sales'])
    sheet01.write(i+1, 3, DATA[i]['view_fee'])
    sheet01.write(i+1, 4, DATA[i]['isTmall'])
    sheet01.write(i+1, 5, DATA[i]['area'])
    sheet01.write(i+1, 6, DATA[i]['name'])
    sheet01.write(i+1, 7, DATA[i]['detail_url'])

# 保存
f.save(u'搜索%s的结果.xls' % find_content)
