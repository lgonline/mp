#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang9'

import json
import requests
from urlparse import urlparse

def _query_es(url, json_param, proxy=False):
    proxies = {'http':'http://172.16.169.99:80'} if proxy else {}
    flag = 'fields' if json_param.get('fields') else '_source'
    result = {'total':0,'data':[]}
    size = json_param['size']

    if size >= 10000:
        if json_param.get('sort'):
            url_start = url + '?scroll=1m'
            json_param['size'] = 10000
        else:
            url_start = url + '?search_type=scan&scroll=1m'
            json_param['size'] = 500

        r = requests.post(url_start, json.dumps(json_param), proxies = proxies)
        json_obj = json.loads(r.content)
        print json_obj

        _scroll_id = json_obj['_scroll_id']
        """
        hits = json_obj['hits']['hits']
        if json_param.get('sort'):
            if len(hits) > 0:
                result['total'] += len(hits)
                for hit in hits:
                    try:
                        tmp = format_data(hit[flag])
                        result['data'].append(tmp)
                    except:
                        continue
        """

        url = 'http://%s/_search/scroll?scroll=1m' % urlparse(url).netloc
        while True:
            if result['total'] >= size:
                result['data'] = result['data'][0:size]
                result['total'] = size
                break
            try:
                r = requests.post(url, _scroll_id, proxies = proxies)
                json_obj = json.loads(r.content)
                print json_obj
                """
                hits = json_obj['hits']['hits']
                if len(hits) > 0:
                    result['total'] += len(hits)
                    for hit in hits:
                        try:
                            tmp = format_data(hit[flag])
                            result['data'].append(tmp)
                        except:
                            continue
                    _scroll_id = json_obj['_scroll_id']

                else:
                    break
                """
            except Exception,e:
                print e

    else:
        try:
            r = requests.post(url, json.dumps(json_param), proxies = proxies)
            json_obj = json.loads(r.content)
            hits = json_obj['hits']['hits']
            result['total'] = len(hits)
            for hit in hits:
                try:
                    tmp = format_data(hit[flag])
                    result['data'].append(tmp)
                except:
                    continue
        except Exception,e:
            print e

    return result

def format_data(data):
    #格式化ES返回list中的元素
    return data

if __name__ == '__main__':
    url = 'http://172.20.73.73:9216/databaseprocessinfo/_search'
    json_param = {"query" : {"filtered" : {"query" : {"bool" : {"must" : [{"range" : {"exec_time" : {"gte" : "2016-12-12 00:00:00","lt" : "2016-12-19 00:00:00"}}} ],"must_not" : [{"match_phrase" : {"INFO" : "SELECT * FROM PROCESSLIST"}}]}}}},"from" : 0,"size" : 1000}
    result = _query_es(url, json_param, True)
	#print result['data']
    print result['data']
    #print result['total']
    #with open('sql_result', 'w') as f:
    #    f.write(json.dumps(result))