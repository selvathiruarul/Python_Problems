#! usr/bin/env python3.5.2
# -*- coding:utf-8 -*-

"""
Created on Thu Nov 19 18:31:10 2016

@author: selva
"""

from Python_Problems import joseph
import threading
from Python_Problems import sorting
import logging
import queue
from datetime import datetime
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    direction = 'r'
    queue=queue.Queue()
    total_people = int(input("Enter the Number of people"))
    kill_index = int(input("Enter the number of people to skip"))
    start_position = int(input("Enter the starting position") or 1)
    direction = input("Enter the direction (r/l)").lower() or 'r'
    while direction.lower() not in ['r', 'l']:
        direction = input("Enter the direction (r/l)").lower()
    log.info("Starting without thread {date}".format(date=datetime.now()))
    items = [2, 3, 5, 6, 7, 1, 152, 100, 97]
    process1 = threading.Thread(target=joseph.kill_people, args=(total_people, kill_index, start_position, direction))
    process2 = threading.Thread(target=sorting.bubble_sort, args=(items,queue,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    log.info('The safest position is {safe}'.format(safe=queue.get()))

