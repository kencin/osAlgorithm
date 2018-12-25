#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - MixIndex.py
# 2018/12/16 10:51
# Author:Kencin <myzincx@gmail.com>

# 三级混合索引


import others.generateList as gl


class MixIndex(object):
    blocks_number = 0  # 数据块数量
    blocks = []  # 数据块

    def __init__(self, file_size):
        self.file_size = file_size

    def cal_blocks_number(self):
        self.blocks_number = int(self.file_size / 16)
        self.blocks = gl.generate_list(5000, self.blocks_number)

    # 八个一组划分
    def div_group(self):
        tmp = self.blocks[0:5]  # 先把0-4号盘块存起来
        for i in range(len(tmp)):
            self.blocks.pop(0)
        self.blocks = [self.blocks[i:i+8] for i in range(len(self.blocks)) if i % 8 is 0]
        while len(self.blocks) > 1:
            tmp.append(self.blocks[0])
            self.blocks.pop(0)
            self.blocks = [self.blocks[i:i + 8] for i in range(len(self.blocks)) if i % 8 is 0]
        for i in range(len(tmp)):
            self.blocks.insert(0, tmp[len(tmp)-1-i])

    def find_block(self, address):
        while address > self.file_size:
            print("地址超出文件范围！应在0到%d" % self.file_size)
            address = input("请重新输入：")
        the_block = int(address / 16) if address % 16 is 0 else int(address / 16) + 1
        # print("%d在第%d个盘块" % (address, the_block))
        # if the_block <= 5:
        #     print("盘块号是：%d" % self.blocks[the_block-1])
        # elif the_block <= 13:
        #     for i in self.blocks:
        #         if isinstance(i, list):
        #             print("盘块号是：%d" % i[int(the_block - 1 - 5)])
        # elif the_block <= 77:
        #     the_block -= 14
        #     the_block = the_block / 8
        tmp = []
        for i in self.blocks:
            if isinstance(i, list):  # 第一层间接
                for j in i:
                    if isinstance(j, list):  # 第二层间接
                        for m in j:
                            if isinstance(m, list):  # 第三层间接
                                for n in m:
                                    tmp.append(n)
                                    # 注意这里有个天坑！ python把[-5,256]的int专门缓存起来
                                    # 在这里如果还用 if len(tmp) is the_block，当len > 256时两边就id不相同了，所以得用==
                                    if len(tmp) == the_block:
                                        print("地址为第%d块盘块，在三次间址盘块号中" % the_block)
                                        print("盘块号为：%d" % tmp.pop())
                                        return
                            else:
                                tmp.append(m)
                                if len(tmp) is the_block:
                                    print("地址为第%d块盘块，在二次间址盘块号中" % the_block)
                                    print("盘块号为：%d" % tmp.pop())
                                    return
                    else:
                        tmp.append(j)
                        if len(tmp) is the_block:
                            print("地址为第%d块盘块，在一次间址盘块号中" % the_block)
                            print("盘块号为：%d" % tmp.pop())
                            return
            else:
                tmp.append(i)
                if len(tmp) is the_block:
                    print("地址为第%d块盘块，在直接盘块号中" % the_block)
                    print("盘块号为：%d" % tmp.pop())
                    return

    def show_blocks(self):
        print("文件大小为：" + str(self.file_size))
        print("共占盘块： " + str(self.blocks_number))
        print("直接盘块号为：")
        print(self.blocks[0:5])
        if len(self.blocks) > 5:
            print("一次间址盘块号为：")
            print(self.blocks[5])
        if len(self.blocks) > 6:
            print("二次间址盘块号为：")
            print(self.blocks[6])
        if len(self.blocks) > 7:
            print("三次间址盘块号为：")
            print(self.blocks[7])

    def generate_mix_index(self):
        self.cal_blocks_number()
        self.div_group()