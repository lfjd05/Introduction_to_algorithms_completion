"""
    计数排序：输入一个元素x，如果有17个元素小于x那他应该在18的位置上
"""


# 计数
def counting_sort(A, B, k):
    C = [0] * (k+1)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] += C[i - 1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [0]*8
counting_sort(A, B, 5)
print(B)
