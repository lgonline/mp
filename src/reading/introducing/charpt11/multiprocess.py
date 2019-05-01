#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: multiprocess.py
@time: 19-4-8 下午10:26 
Description: 用队列解决相关的问题
"""

import multiprocessing as mp

# 重构洗盘子
import threading, queue
import time


# 模拟一个洗盘子的人和多个烘干的进程，使用一个中间队列dish_queue
def washer(dishes,output):
    for dish in dishes:
        print('Washing',dish,'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying',dish,'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer,args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ['salad','bread','entree','dessert']
washer(dishes,dish_queue)
dish_queue.join()

print('----------------使用线程来重构这个洗盘子的例子--------------------')

def new_washer(dishes,dish_queue):
    for dish in dishes:
        print('Washing ',dish)
        time.sleep(5)
        dish_queue.put(dish)

def new_dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('drying',dish)
        time.sleep(10)
        dish_queue.task_done

new_dish_queue = queue.Queue
for n in range(2):
    new_dryer_thread = threading.Thread(target=dryer,args=(dish_queue,))
    new_dryer_thread.start()

dishes = ['salad','bread','entree','dessert']
washer(dishes,dish_queue)
dish_queue.join()

if __name__ == '__main__':




    pass