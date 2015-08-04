# coding=utf-8

from threading import Thread
import time
import random
import queue

equque = queue.Queue()


def run_thread(n):
    if n == 1:
        for j in range(9):
            print('等待队列：')
            print(str(j)+' 线程的值为：'+str(equque.get()))


threads = {}
for i in range(10):
    if i > 1:
        equque.put(random.randint(10, 30))

    Thread(target=run_thread, args={i, }).start()
    time.sleep(random.randint(1, 3))
