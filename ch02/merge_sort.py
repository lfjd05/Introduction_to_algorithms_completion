# 归并排序, 该版本有错误
import math


def merg(A, p, q, r):
    L = A[p: q+1]+[float('inf')]  # 牌堆底部放无穷作为哨兵
    R = A[q+1: r+1]+[float('inf')]
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            print(k, i)
            A[k] = L[i]  # 较小的一张从堆中拿开放到输出堆
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merg_sort(A, p, r):
    if p < r:
        q = (p+r)//2  # 取商整数
        merg_sort(A, p, q)
        merg_sort(A, q+1, r)
        return merg(A, p, q, r)

A = [5, 2, 4, 6, 1, 3]
merg_sort(A, 0, 7)
print(A)
