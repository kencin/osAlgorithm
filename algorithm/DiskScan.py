#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - DiskScan.py
# 2018/12/16 10:51
# Author:Kencin <myzincx@gmail.com>

# 扫描算法 (电梯算法)


def scan(curr_position, disk_list):
    min_disk = min(disk_list)
    max_dixk = max(disk_list)
    move_left = False
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
                if move_left:
                    if i <= curr_position and min_distance >= abs(i - curr_position):
                        min_distance = abs(i - curr_position)
                        next_position = i
                else:
                    if i > curr_position and min_distance >= abs(i - curr_position):
                        min_distance = abs(i - curr_position)
                        next_position = i
        cost += min_distance
        result.append(next_position)
        if next_position is min_disk:
            move_left = False
        if next_position is max_dixk:
            move_left = True
        disk_list.remove(next_position)
        curr_position = next_position
    return cost, result