#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:04
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : tt.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""
from xml.parsers.expat import ParserCreate

#定义天气字典、天数
weather_dict = {}
which_day = 0

#定义解析类,包括三个主要函数：start_element(),end_element(),char_data()
class WeatherSaxHandler(object):
    #定义start_element函数
    def start_element(self,name,attrs):
        global weather_dict,which_day
        #判断并获取XML文档中地理位置信息
        if name == 'yweather:location':
            #将本行XML代码中'city'属性值赋予字典weather_dict中的'city'
            weather_dict['city']=attrs['city']
            weather_dict['country']=attrs['country']#执行结束后此时，weather_dict={'city':'Beijing','country'='China'}
        #同理获取天气预测信息
        if name == 'yweather:forecast':
            which_day +=1
            #第一天天气，获取气温、天气
            if which_day == 1:
                weather ={'text':attrs['text'],
                          'low':int(attrs['low']),
                          'high':int(attrs['high'])
                          }
                weather_dict['today']=weather#此时weather_dict出现二维字典
#weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}}
            #第二天相关信息
            elif which_day==2:
                weather={
                    'text':attrs['text'],
                    'low':int(attrs['low']),
                    'high':int(attrs['high'])
                }
                weather_dict['tomorrow']=weather
#weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}, 'tomorrow': {'text': 'Sunny', 'low': 21, 'high': 34}}
    #end_element函数
    def end_element(self,name):
        pass
    #char_data函数
    def char_data(self,text):
        pass

def main():
    pass


if __name__ == '__main__':
    main()
