# 简易堆排序


#  维护最大堆， 从根，左，右中选出最大的
def max_heapify(A, i, heap_size):
    l = (i << 1) + 1     # 2i+1
    r = (i + 1) << 1     # 2i+2
    if l < heap_size and A[l] > A[i]:
        largest = l  # 最大是左
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r     # 最大的是右
    if largest != i:
        # 如果找到了最大的，交换
        A[i], A[largest] = A[largest], A[i]
        # largest是原来的A[i],又有可能违反最大堆
        max_heapify(A, largest, heap_size)


def build_max_heap(A, heap_size):
    for i in range((heap_size)//2, -1, -1):
        max_heapify(A, i, heap_size)


def heapsort(A):
    heap_size = len(A)
    # 构建最大堆
    build_max_heap(A, heap_size)
    for i in range(heap_size-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)


A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
heapsort(A)
print(A)
