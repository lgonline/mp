#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = '330mlcc'

import urlparse

if __name__ == '__main__':
    urls = urlparse.urlparse("https://get3.adobe.com/cn/flashplayer/download/?installer=FP_25_for_Firefox_-_NPAPI&os=Windows%2010&browser_type=KHTML&browser_dist=Chrome&a=McAfee_Security_Scan_Plus_Chrome_Browser&dualoffer=false&mdualoffer=false&type=au&browser_vers=57.0.2987.133&stype=6564")
    for url in urls:
        print(url)

    request_method = urls[1]
    print(request_method)
    pass

