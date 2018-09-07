# 随机化版本的快速排序，随机性指的是，实际中不可能所有输入都是等概率的
# 人为因素随机性使得对所有输入都能有较好性能
# 快速排序按算法导论伪代码编写的
from random import randrange


# 根据主元把A分块
def partition(A, p, r):
    x = A[r]  # 主元
    i = p-1  # 记录分界线的位置
    for j in range(p, r):  # 从p:r-1的循环
        if A[j] <= x:  # 比主元小的放左边放最左边，原位的往右移动一下
            i += 1
            A[i], A[j] = A[j], A[i]  # 找到比主元小的，交换到左边
    A[i + 1], A[r] = A[r], A[i + 1]  # 把主元放到分界处
    return i+1     # 返回分界线位置，给下次递归用


def randomize_partition(A, p, r):
    i = randrange(p, r+1, 1)  # 产生随机主元的位置
    A[r], A[i] = A[i], A[r]   # 主元放最后省得捣乱
    return partition(A, p, r)


def quick_sort(A, p, r):
    # if len(A) > 1:
    if p < r:
        q = randomize_partition(A, p, r)
        # left = A[:q-1]
        # right = A[q+1:]
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
        # return merge(L,R)


A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
# A = [9, 7, 8, 10]
quick_sort(A, 0, len(A)-1)
print(A)
