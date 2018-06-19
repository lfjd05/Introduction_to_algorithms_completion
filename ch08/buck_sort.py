# 桶排序，假设数据是均匀分布的，速度较快。
from ch02.insert_sort import insertion_sort


def bucket_sort(A):
    n = len(A)
    # B = [0] * n
    B = [[] for i in range(n)]
    for i in range(n):
        B[int(n * A[i])].append(A[i])
    out = []
    print('排序前的B', B)
    for buck in B:
            insertion_sort(buck)
    for i in range(len(B)):
        B+=B[i]
    return B[-n:]

A = [.31, .41, .59, .26, .41, .58]
print(bucket_sort(A))
