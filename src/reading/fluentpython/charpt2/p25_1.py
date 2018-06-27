#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 20:06
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : p25_1.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
# @Description： 元组的拆包

import os

def main():
    lax_coordinates = (33.9425,-118.408056)
    latitude,longitude = lax_coordinates
    print(latitude,longitude)
    print()

    _,filename = os.path.split(os.path.abspath(__file__))
    print(filename)
    print()

    a,b,*rest = range(5)
    print(a,b,rest)

    c,d,*r1 = range(4)
    print(c,d,r1)

    e,*f,g = range(5)
    print(e,f,g)

    metro_areas = [
        ('tokyo','JP',36.933,(35.689722,139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.689722, 77.691667)),
        ('Mexico City', 'MX', 20.142, (19.689722, -99.691667)),
        ('New York-Newark', 'US', 20.104, (40.689722, -74.691667)),
        ('Sao Paulo', 'BR', 19.649, (-23.689722, -46.691667)),
    ]

    print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
    fmt = '{:15} | {:^9.4f} | {:^9.4f}'
    for name,cc,pop,(lattitudes,longitudes) in metro_areas:
        if longitudes <= 0:
            print(fmt.format(name,lattitudes,longitudes))
    pass


if __name__ == '__main__':
    main()
