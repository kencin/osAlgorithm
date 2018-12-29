#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - main.py
# 2018/11/11 11:49
# Author:Kencin <myzincx@gmail.com>

import others.generateList as gl
import algorithm as al
import copy

if __name__ == '__main__':
    # Disk调度测试
    # disk_list_sstf = gl.generate_list(5000, 50)
    # disk_list_scan = copy.copy(disk_list_sstf)
    # generateList = copy.copy(disk_list_scan)
    # scan_cost, scan_result = al.DiskScan.scan(2500, disk_list_scan)
    # sstf_cost, sstf_result = al.DiskSstf.sstf(2500, disk_list_sstf)
    #
    # print("随机磁道：")
    # print(generateList)
    # print("最短寻道时间优先算法花费：")
    # print(sstf_cost)
    # print("最短寻道时间优先算法结果：")
    # print(sstf_result)
    # print("扫描算法花费：")
    # print(scan_cost)
    # print("扫描算法结果：")
    # print(scan_result)

    # 混合索引测试
    mix_index = al.MixIndex.MixIndex(800 * 16)
    mix_index.generate_mix_index()
    mix_index.show_blocks()
    address = input("请输入要查找的地址：")
    mix_index.find_block(int(address))

    # 银行家算法测试
    # banker = al.banker.Banker()
    # banker.make_bank()
    # banker.is_safe()
    # print(banker.safe)
    # banker.pre_allocation()
    # print(banker.safe)

