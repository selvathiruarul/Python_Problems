#! usr/bin/env python3.5.2
# -*- coding:utf-8 -*-

"""
Created on Thu Nov 19 18:31:10 2016

@author: selva
"""

from Python_Problems import joseph


if __name__ == '__main__':
    direction = 'r'
    total_people = int(input("Enter the Number of people"))
    kill_index = int(input("Enter the number of people to skip"))
    start_position = int(input("Enter the starting position") or 1)
    direction = input("Enter the direction (r/l)").lower() or 'r'
    while direction.lower() not in ['r', 'l']:
        direction = input("Enter the direction (r/l)").lower()
    safe_position = joseph.kill_people(total_people, kill_index, start_position, direction)
    print('The safest position is {safe}'.format(safe=safe_position))
