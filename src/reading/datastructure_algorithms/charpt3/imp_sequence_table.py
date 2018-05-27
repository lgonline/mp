#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: 330mlcc 
@license: Apache Licence  
@contact: lg_online@126.com 
@site:  
@software: PyCharm 
@file: imp_sequence_table
@time: 18-5-27 下午5:13 
Description: 
"""

class SequenceList(object):
    def __init__(self,max=8):
        self.max = max
        self.num = 0
        self.date = [None] * self.max

    def is_empyt(self):
        return self.num is 0

    def is_full(self):
        return self.num is self.max

    # 获取线性表某一位值的元素
    def __getitem__(self, i):
        if not isinstance(i,int):# 如果i不是int型，判断输入错误
            raise TypeError

        if 0 <= i < self.num:
            return self.date[i]
        else:
            raise IndexError

    # 修改线性表中某一位置的元素
    def __setitem__(self, key, value):
        if not isinstance(key,int):
            raise TypeError
        if 0<= key < self.num:
            self.date[key] = value
        else:
            raise IndexError

    # 查找元素的位置
    def getLoc(self,value):
        n = 0
        for j in range(self.num):
            if self.date[j] == value:
                return j

        if j == self.num:
            return -1

    # 统计线性表种元素的个数
    def Count(self):
        return self.num

    # 表尾的插入操作
    def appendLast(self,value):
        if self.num >= self.max:
            print('The list is full.')
            return
        else:
            self.date[self.num] = value
            self.num += 1

    # 表任意位置的插入
    def insert(self,i,value):
        if not isinstance(i,int):
            raise TypeError

        if i < 0 and i > self.num:
            raise IndexError

        for j in range(self.num,i,-1):
            self.date[j] = self.date[j-1]
            # print(self.date[j])

        self.date[i] = value
        self.num += 1

    #删除某一位置的操作
    def remove(self,i):
        if not isinstance(i,int):
            raise TypeError

        if i<0 and i>=self.num:
            raise IndexError

        for j in range(i,self.num):
            self.date[j] = self.date[j+1]

        self.num -= 1

    # 输出操作
    def printList(self):
        for i in range(0,self.num):
            print(self.date[i])

    # 销毁操作
    def destroy(self):
        self.__init__()

if __name__ == '__main__':
    list = SequenceList()
    list.appendLast(5)
    list.appendLast(10)
    list.appendLast(15)

    list.insert(0,0)
    list.appendLast(20)
    list.insert(0,-5)
    list.insert(0,-15)
    list.insert(1,-10)
    list.printList()
    print('list中有多少个元素：', list.Count())
    pass 
    
    