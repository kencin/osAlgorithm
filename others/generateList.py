#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# osAlgorithm - generateList.py
# 2018/12/16 10:51
# Author:Kencin <myzincx@gmail.com>
import random


def generate_list(max_number, number_of_disk):
    disk = random.sample(range(0, max_number), number_of_disk)
    return disk