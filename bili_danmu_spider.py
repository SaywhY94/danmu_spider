# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import argparse

import re
import time

def write_down(html, filename='test.html'):
    with open(filename, 'w') as f:
        f.write(html)

header = {
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer': 'http://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0'
}

def get_danmuku(cid, filename):
    danmuku_api = "https://api.bilibili.com/x/v1/dm/list.so?oid="
    r2 =requests.get(danmuku_api+cid, headers=header)
    soup = BeautifulSoup(r2.content, 'lxml')
    danmus = soup.find_all('d')
    with open(filename, 'w') as fw:
        print(u"写入弹幕ing...")
        for danmu in danmus:
            content = danmu.string
            attr = danmu['p'].split(',')
            t1 = str(attr[0])  # 电影时间
            t2 = attr[4]  # 发布时间
            t3 = str(attr[6])  # 发送者ID
            timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(t2)))
            fw.write(content.encode('utf-8')+ ',' + t1 + ',' + timestr + ',' + t3 + '\n')
    print(u"写入完成...请查看"+filename)   

def get_input_id():
    parser = argparse.ArgumentParser(description='弹幕爬取脚本说明')
    parser.add_argument('-i', '--input', help='set the cid')
    parser.add_argument('-o', '--output',  help='set the filename to store')
    args = parser.parse_args()
    if args.output:
        filename = args.output
    else:
        filename = 'test.csv'
    cid = str(args.input)
    print ("cid = " + cid)
    return (cid, filename)

def main():
    cid, filename = get_input_id()
    get_danmuku(cid, filename)
    
if __name__ == '__main__':
    main()