#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - banker.py
# 2018/11/11 11:31
# Author:Kencin <myzincx@gmail.com>


# 银行家算法

import copy


class Banker(object):
    available = []  # 可利用资源
    max = []  # 资源的最大需求
    allocation = []  # 已分配的资源
    need = []  # 资源的当前需求
    request = []  # 资源的当前请求

    safe = []  # 安全序列

    process = 0  # 进程数目
    src = 0  # 资源种类数目

    def __init__(self):
        pass

    def pre_allocation(self):
        tmp = input("请输入要手动进行资源分配的进程号：")
        while int(tmp) > int(self.process):
            tmp = input("进程号不存在，请重新输入要手动进行资源分配的进程号：")
        tmp2 = input("请输入对%d号进程分配的资源数目：" % int(tmp))
        self.request = list(tmp2.split())
        for i in range(int(self.src)):
            self.request[i] = int(self.request[i])
        for i in range(int(self.src)):
            if self.request[i] > self.available[i]:
                print("分配资源大于可用资源！")
                return False
        for i in range(int(self.src)):
            if self.request[i] > self.need[int(tmp)][i]:
                print("分配资源大于所需资源！")
                return False
        for i in range(int(self.src)):
            self.available[i] -= self.request[i]
            self.allocation[int(tmp)][i] += self.request[i]
            self.need[int(tmp)][i] -= self.request[i]
        if self.is_safe():
            return True
        else:
            for i in range(int(self.src)):
                self.available[i] += self.request[i]
                self.allocation[int(tmp)][i] -= self.request[i]
                self.need[int(tmp)][i] += self.request[i]
            print("无法获得安全序列！")
            return False

    def is_safe(self):
        self.safe.clear()
        a = 0
        finish = []
        tmp = copy.copy(self.available)
        for i in range(int(self.process)):
            finish.append(False)
        while a < int(self.process):
            if not finish[a]:
                for j in range(int(self.src)):
                    if self.need[a][j] > tmp[j]:
                        break
                    if j == (int(self.src) - 1):
                        self.safe.append(a+1)
                        for m in range(int(self.src)):
                            tmp[m] += self.allocation[a][m]
                        finish[a] = True
                        a = -1
            a += 1
        if False in finish:
            return False
        return True

    def make_bank(self):
        # self.process = input("请输入进程数：")
        # self.src = input("请输入资源种类数：")
        # for i in range(int(self.process)):
        #     tmp = input("请输入进程%d最大需求资源数：" % i)
        #     while len(list(tmp.split())) != int(self.src):
        #         tmp = input("资源种类数不合，请重新输入进程%d最大需求资源数：" % i)
        #     self.max.append(list(tmp.split()))
        # for i in range(int(self.process)):
        #     tmp = input("请输入进程%d已分配资源数：" % i)
        #     while len(list(tmp.split())) != int(self.src):
        #         tmp = input("资源种类数不合，请重新输入进程%d已分配资源数：" % i)
        #     self.allocation.append(list(tmp.split()))
        # tmp = input("请输入各个资源当前可用资源数：")
        # while len(list(tmp.split())) != int(self.src):
        #     tmp = input("资源种类数不合，请重新输入各个资源当前可用资源数：")
        # self.available = list(tmp.split())
        # tmp = []
        # for i in range(int(self.src)):
        #     self.available[i] = int(self.available[i])
        # for i in range(int(self.process)):  # need赋值并  max， allocation， available str to int
        #     for j in range(int(self.src)):
        #         self.max[i][j] = int(self.max[i][j])
        #         self.allocation[i][j] = int(self.allocation[i][j])
        #         tmp.append(self.max[i][j] - self.allocation[i][j])
        #     self.need.append(list(tmp))
        #     tmp.clear()

        self.process = 3
        self.src = 3
        self.max = [[4, 5, 6], [2, 3, 4], [1, 2, 3]]
        self.allocation = [[2, 2, 2], [1, 1, 1], [0, 0, 1]]
        self.available = [1, 3, 3]
        self.need = [[2, 3, 4], [1, 2, 3], [1, 2, 2]]
        print(self.max)
        print(self.allocation)
        print(self.available)
        print(self.need)



