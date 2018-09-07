# 桶排序，假设数据是均匀分布的，速度较快。
"""
    桶排序最精髓的地方是假设待排序序列是均匀分布的。这样我们可以构造一系列‘桶’
    桶是从小到大排好的，把数均匀的放在各个桶里面，把各个桶里面的数分别排好序，合并桶即可
"""
from ch02.insert_sort import insertion_sort


def bucket_sort(A):
    n = len(A)
    # B = [0] * n
    B = [[] for i in range(n)]
    # 按照均匀分布把数据放到各个桶中
    for i in range(n):
        B[int(n * A[i])].append(A[i])
    print('排序前的B', B)
    # 对每隔桶中的元素分别排序
    for buck in B:
        insertion_sort(buck)
    # 把桶合并
    for i in range(len(B)):
        B += B[i]
    return B[-n:]


A = [.31, .41, .59, .26, .41, .58]
A1 = [.87, .17, .39, .26, .72, .94, .21, .12, .23, .68]
print(bucket_sort(A1))
