# 利用快速排序的分块方法进行最值选择
from ch07.quick_sort02 import randomize_partition


# 返回数组第i小的元素
def randomized_select(A, p, r, i):
    if len(A) == 1:
        return A[0]

    q = randomize_partition(A, p, r)
    k = q-p+1
    if i == k:      # 中心
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
A0 = [9, 7, 8, 10]
print(randomized_select(A0, 0, len(A0)-1, 1))
