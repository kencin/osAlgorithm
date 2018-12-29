#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - GroupLink.py
# 2018/12/25 11:57
# Author:Kencin <myzincx@gmail.com>

# 成组链接法


class FirstNode(object):
    def __init__(self):
        self.free = 0
        self.group = []


class GroupLink(object):
    group = []
    group_list = []
    blocks = 7
    blocks_in_group = 3

    def init(self):
        group = []
        number_of_group = int(self.blocks / self.blocks_in_group) \
            if self.blocks % self.blocks_in_group is 0 else int(self.blocks / self.blocks_in_group) + 1
        for i in range(self.blocks):
            group.append(i + 1)
        group = [group[i:i+self.blocks_in_group] for i in range(len(group)) if i % 3 is 0]
        first_node = [FirstNode() for i in range(number_of_group)]
        for i in range(number_of_group):
            first_node[i].free = len(group[i+1])
            first_node[i].group = group[i+1]


    def div_group(self, disk_number):
        if disk_number not in range(self.blocks + 1):
            print("请求磁盘数不合要求！")
            return
