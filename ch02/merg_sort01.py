# 归并排序


def merge(left_list, right_list):
    result = []
    while len(left_list) >0 and len(right_list)>0:
        if left_list[0] <= right_list[0]:
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))
    # while循环出来之后 说明其中一个数组没有数据了，
    # 我们把另一个数组添加到结果数组后面
    result += left_list
    result += right_list
    return result


def merge_sort(lists):
    if len(lists)==1:   # 拆分到只剩下单个元素停止
        return lists
    mid = len(lists) // 2

    left = lists[:mid]
    right = lists[mid:]

    # 再拆分，直到只有一个元素
    L = merge_sort(left)
    R = merge_sort(right)

    # 排序后合并
    return merge(L, R)


A = [5, 2, 4, 6, 1, 3]
A1 = merge_sort(A)
print(A1)
