#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 10:49
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : demoScrapBaidu.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#   

import urllib.request
import re
from bs4 import BeautifulSoup

def make_content_to_html(scrap_data):
    f = open('scrap_result.html','a+',encoding='utf-8')
    message = '''
    <html>
        <head>
            <title></title>
        </head>
        <body>
        爬取结果<br>
        <hr>
        <table border="1px">
        <tr>
        <td bgcolor="#f0f8ff" width="200">省份
        </td>
        <td bgcolor="#f0f8ff" width="300">省会城市
        </td>
        </tr>
        
    '''+scrap_data+'''
    
        </table>
        </body>
    </html>
    '''
    f.write(message)
    f.close()

def main():
    # 定义基本信息
    urls = 'https://zhidao.baidu.com/question/120615642.html'
    UserAgent = 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    Referers = 'https://www.baidu.com/link?url=qwg78ZrrBP8P-ivzTn6uKG-rTrVY5c4aKQ2hhwcEZGZc8rkQcCwLIFn69GgbxG_Q4rx9rkRBlE0mAGL1bSyM6q&wd=&eqid=9f8961540000c365000000025b4c0796'
    headers = {'UserAgent':UserAgent,'Referer':Referers}

    # 爬去数据
    req = urllib.request.Request(urls,headers=headers)
    responses = urllib.request.urlopen(req)
    soup = BeautifulSoup(responses,'lxml',from_encoding='gbk')


    # print(soup.select('div[class$="best-text mb-10"]'))，找到位置
    results = str(soup.select('div[class$="best-text mb-10"]'))
    # 正则匹配
    results = str(re.findall('<p>(.*)<h.*',results))
    # results = str(re.findall('<p>(.*)</h2>',results))
    # 去除噪声
    results = str(results.replace('p','"').replace('xa0','"'))
    # 提取所需的数据，返回一个字符串
    results = re.findall('(\w+)',results)

    # 将字符串转换为字典
    results_dict = {}
    for i in range(0,len(results),2):
        results_dict[results[i]] = results[i+1]

    # 拼接html中的内容
    resultStr = ''
    for key,value in results_dict.items():
        # ('<td>'+key+'</td>'+'<td>'+value+'</td>')
        resultStr += '<tr><td width="300">'+key+'</td>'+'<td width="300">'+value+'</td></tr>'

    # 写文件
    make_content_to_html(resultStr)

    pass


if __name__ == '__main__':
    main()
    pass