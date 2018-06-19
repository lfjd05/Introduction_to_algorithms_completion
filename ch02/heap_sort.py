# -*- encoding: utf-8 -*-
# 堆排序
"""
    Topic: sample
    Desc : 堆排序
        堆排序的时间复杂度是O(nlg(n))，并且具有空间原址性
        二叉堆heap是一种数据结构，可用来实现优先队列
        给定一个节点的下标i(下标从0开始)，则其父节点、坐孩子、右孩子坐标：
        parent(i) = floor((i+1)/2 - 1) = ((i + 1) >> 1) - 1
        left(i) = 2*i + 1 = (i << 1) + 1
        right(i) = 2*i + 2 = (i + 1) << 1
        最小堆定义： 所有i必须满足A[parent(i)] <= A[i]
        最大堆定义： 所有i必须满足A[parent(i)] >= A[i]
        在堆排序中，我们使用最大堆
        在优先队列算法中，使用最小堆
"""


# 定义堆
class Heap:
    def __init__(self, seq, heapSize, length):
        self.seq = seq
        self.heapSize = heapSize  # 堆大小, 因为不一定序列中所有元素都用在堆上
        self.length = length  # 元素个数


# 堆排序
def heapSort(seq):
    # 定义堆
    heap = Heap(seq, len(seq), len(seq))
    __buildMaxHeap(heap)
    s = heap.seq
    for i in range(heap.length - 1, 0, -1):
        s[0], s[i] = s[i], s[0]
        heap.heapSize -= 1
        __maxHeapify(heap, 0)  # 维护最大堆


# 维护最大堆，假设两个孩子都是最大堆，加入i后，A[i]有可能小于孩子
def __maxHeapify(heap, i):    # i是最后一个父节点
    seq = heap.seq
    slen = heap.heapSize
    while True:
        left = (i << 1) + 1
        right = (i + 1) << 1  # 由于下标0开始，和算法导论说的有不同
        if left < slen and seq[left] > seq[i]:
            largest = left
        else:
            largest = i
        if right < slen and seq[right] > seq[largest]:
            largest = right
        if largest != i:  # 如果找到了最大的，交换
            seq[largest], seq[i] = seq[i], seq[largest]
            i = largest   # 交换完了新产生的节点会不会又比它的儿子小，所以要用它重新看看排序
        else:
            break


# 无序数组构造最大堆
def __buildMaxHeap(heap):
    slen = heap.heapSize
    for i in range(((slen + 1) >> 1) - 1, -1, -1):  # 循环到0, 起始slen/2-1
        __maxHeapify(heap, i)


if __name__ == '__main__':
    iSeq = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    heapSort(iSeq)
    print(iSeq)
