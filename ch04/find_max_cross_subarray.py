# 找最大跨越子数组


def find_max_crossing_subarray(A, mid):
    left_sum = float('-inf')
    sum = 0
    # for i in range(mid, low-1, -1):
    for i in range(mid, 0, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1, len(A)):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
    return left_sum+right_sum


def find_maximum_subarray(A):
    if len(A)==1:
        return A[0]
    else:
        mid = len(A) // 2
        left_sum = find_maximum_subarray(A[: mid])  # 左侧最大
        right_sum = find_maximum_subarray(A[mid:])
        cross_sum = find_max_crossing_subarray(A, mid)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum>=left_sum and right_sum>= cross_sum:
            return right_sum
        else:
            return cross_sum


lists = [0, -1, 3, -4]
list1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
list2 = [-1, -2, -3, -10, -10, -23]
print(find_maximum_subarray(list2))
