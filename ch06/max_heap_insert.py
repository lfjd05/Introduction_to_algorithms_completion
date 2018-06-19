# 元素插入到最大堆中


# 给新节点添加关键字，维护最大堆性质
def heap_increase_key(A, i, key):
    if key < A[i]:
        print('new key is smaller than current key')
    A[i] = key
    while i > 0 and A[i // 2 - 1] < A[i]:  # 如果比父节点大
        A[i], A[i // 2 - 1] = A[i // 2 - 1], A[i]
        i = i // 2 - 1


def max_heap_insert(A, key):
    heap_size = len(A) + 1
    # 增加一个新的叶子节点
    A += [float('-inf')]
    heap_increase_key(A, heap_size-1, key)


A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
max_heap_insert(A, 45)
print(A)
