#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 冒泡排序
"""
    Topic: sample
    Desc : 冒泡排序
    描述： 比较相邻元素，值大的交换到右边，如果有N个数需要排，一般从N-1开始起泡
"""


def bubbleSort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-1, i, -1):
            if seq[j] < seq[j-1]:                    # 左边的比较大那就交换
                seq[j-1], seq[j] = seq[j], seq[j-1]  # 交换

if __name__ == '__main__':
    s = [4, 6, 2, 5, 7, 9, 8, 1]
    bubbleSort(s)
    print(s)
