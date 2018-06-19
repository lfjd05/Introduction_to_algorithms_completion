# 快速排序按算法导论伪代码编写的
def partition(A, p, r):
    x = A[r]  # 主元
    i = p-1  # 记录分界线的位置
    for j in range(p, r):  # 从p:r-1的循环
        if A[j] <= x:  # 比主元小的放左边放最左边，原位的往右移动一下
            i += 1
            A[i], A[j] = A[j], A[i]  # 找到比主元小的，交换到左边
    A[i + 1], A[r] = A[r], A[i + 1]  # 把主元放到分界处
    return i+1


def quick_sort(A, p, r):
    # if len(A) > 1:
    if p < r:
        q = partition(A, p, r)
        # left = A[:q-1]
        # right = A[q+1:]
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
        # return merge(L,R)


A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
# A = [9, 7, 8, 10]
quick_sort(A, 0, len(A)-1)
print(A)
