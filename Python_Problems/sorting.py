#! usr/bin/env python3.5.2
# -*- coding:utf-8 -*-

import logging


def bubble_sort(items,q):
    logging.basicConfig(level=logging.INFO)
    log=logging.getLogger(__name__)
    not_sorted = 1
    while not_sorted > 0:
        not_sorted = 0
        for item in range(len(items) - 1):
            if items[item] > items[item + 1]:
                items[item], items[item + 1] = items[item + 1], items[item]
                not_sorted += 1

    q.put("Sorted {sorted}".format(sorted=items))
