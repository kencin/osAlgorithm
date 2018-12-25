#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - DiskSstf.py
# 2018/12/22 11:49
# Author:Kencin <myzincx@gmail.com>

# 最短寻道时间优先算法


def sstf(curr_position, disk_list):
    cost = 0
    result = []
    min_distance = 0
    next_position = 0

    while len(disk_list) != 0:
        for i in disk_list:
            if i == disk_list[0]:
                min_distance = abs(i - curr_position)
                next_position = i
            else:
                if min_distance >= abs(i - curr_position):
                    min_distance = abs(i - curr_position)
                    next_position = i
        cost += min_distance
        result.append(next_position)
        disk_list.remove(next_position)
        curr_position = next_position
    return cost, result