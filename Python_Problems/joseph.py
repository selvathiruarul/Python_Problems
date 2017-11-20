#! usr/bin/env python3.5.2
# -*- coding:utf-8 -*-

"""
Created on Thu Nov 19 18:31:10 2016

@author: selva
"""


def kill_people(total, killing_position, start=0, kill_direction='r'):
    """
    Method kill people in josephus problem
    :param total: 
    :param killing_position: 
    :param start: 
    :param kill_direction: 
    :return: 
    """
    people = total
    killing_position = int(killing_position)
    people = range(1, int(people))
    people_list = [*people]
    if kill_direction == 'l':
        people_list.reverse()
        index = len(people_list) - start - 2
    else:
        index = start - 1
    while len(people_list) > 1:
        del people_list[index]
        index = (index + killing_position) % len(people_list)
        print(people_list)
    return people_list[0]


if __name__ == '__main__':
    direction = 'r'
    total_people = int(input("Enter the Number of people"))
    kill_index = int(input("Enter the number of people to skip"))
    start_position = int(input("Enter the starting position") or 1)
    direction = input("Enter the direction (r/l)").lower() or 'r'
    while direction.lower() not in ['r', 'l']:
        direction = input("Enter the direction (r/l)").lower()
    safe_position = kill_people(total_people, kill_index, start_position, direction)
    print('The safest position is {safe}'.format(safe=safe_position))
