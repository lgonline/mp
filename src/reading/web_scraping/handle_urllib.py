#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 9:40
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : handle_urllib.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description: 
#   
#

# import urllib.request
from urllib import request
import urllib.parse


def main():
    target_urls = 'https://movie.douban.com/chart'
    target_urls1 = 'https://zhidao.baidu.com/question/120615642.html'

    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh; q = 0.9, zh - TW; q = 0.8',
        'Cache - Control': 'max - age = 0',
        'Connection': 'keep - alive',
        'Cookie':'IKUT=108; BAIDUID=2E1719C92ED27EBA51A27AA485A86AE3:FG=1; PSTM=1530269587; BIDUPSID=2E1719C92ED27EBA51A27AA485A86AE3; '
                 'H_PS_PSSID=1428_21081; BDSFRCVID=_ttsJeC62xqxol57hO63KwlL_HIMdMOTH6aIP6fMeXtYbQei00vjEG0PDU8g0Ku-KA06ogKK0mOTHvOP; '
                 'H_BDCLCKID_SF=tJIDoIL2JC_3qn5zqROHhRIJhpo-KnLXKKOLVM--X-Okeq8CDxQxK6kPMGJu2fcvW5vQ2U770RoFVxo2y5jHhpkNDROBKqc82DT7Qbrt0bQpsIJMM4DWbT8U5fKL2lOzaKviaKJEBMb1fl7Me6t5D6oyjN8s-bbfHj50WtnVKRrJKROvhjRr5b0yyxomtjjO-6byWIK52pA-hpv6hMvryMFIb-c9LUkqKm5T_JQz5xnMoJohbtu2DbKqQttjQU3PfIkja-KEWhD2MR7TyU42hf47yhj9QTT2-DA_oC0XJCQP; '
                 'PSINO=2; MCITY=-131%3A; BDRCVFR[yPEwirh9ez_]=aeXf-1x8UdYcs; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; '
                 'Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1531130111,1531130255,1531130353,1531130918; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1531130991',
        # 'Cookie': 'IKUT=108; BAIDUID=2E1719C92ED27EBA51A27AA485A86AE3: FG=1; PSTM=1530269587; BIDUPSID=2E1719C92ED27EBA51A27AA485A86AE3; H_PS_PSSID=1428_21081;'
        #           'BDSFRCVID=_ttsJeC62xqxol57hO63KwlL_HIMdMOTH6aIP6fMeXtYbQei00vjEG0PDU8g0Ku-KA06ogKK0mOTHvOP; '
        #           'H_BDCLCKID_SF=tJIDoIL2JC_3qn5zqROHhRIJhpo-KnLXKKOLVM--X-Okeq8CDxQxK6kPMGJu2fcvW5vQ2U770RoFVxo2y5jHhpk'
        #           'NDROBKqc82DT7Qbrt0bQpsIJMM4DWbT8U5fKL2lOzaKviaKJEBMb1fl7Me6t5D6oyjN8s-bbfHj50WtnVKRrJKROvhjRr5b0y'
        #           'yxomtjjO-6byWIK52pA-hpv6hMvryMFIb-c9LUkqKm5T_JQz5xnMoJohbtu2DbKqQttjQU3PfIkja-KEWhD2MR7TyU42hf47yhj9QTT2-DA_oC0XJCQP; '
        #           'PSINO=2; MCITY=-131%3A; BDRCVFR[yPEwirh9ez_] = aeXf-1x8UdYcs; BDORZ = FFFB88E999055A3F8A630C64834BD6D0; '
        #           'Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925 = 1531130111, 1531130255, 1531130353, 1531130918;Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925 = 1531130991',
        'Host': 'zhidao.baidu.com',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 66.0.3359.139 Safari / 537.36'
    }

    dicts = {'name':'baidu'}


    # urllib.parse，通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中。这样就完成了一次post请求。
    data = bytes(urllib.parse.urlencode(dicts),encoding='utf-8')
    # print(data)

    # req = request.Request(url=target_urls,data=data,headers=headers,method='GET')
    req = request.Request(url=target_urls,data=data,method='GET')
    req.add_header(headers)


    # 在某些网络情况不好或者服务器端异常的情况会出现请求慢的情况，或者请求异常，所以这个时候我们需要给请求设置一个超时时间，而不是让程序一直在等待结果。
    # response = urllib.request.urlopen(target_urls1,timeout=3)
    response = urllib.request.urlopen(req)


    content = response.read().decode('gbk')

    # 通过response.status、response.getheaders().response.getheader("server")，获取状态码以及头部信息
    # print(type(response))
    # print(response.status)
    print('response.getheaders() is : ',response.getheaders())
    print(content)
    pass


if __name__ == '__main__':
    main()
    pass