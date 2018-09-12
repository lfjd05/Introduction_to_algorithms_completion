# 列表
# random = [(0, 2, 0), (1, 4, 1), (2, 1, 1), (3, 3, 1)]
#
# # 指定第二个元素排序
# random.sort(key=lambda item: (item[1]+item[2], item[1], item[0]))
#
# # 输出类别
# print('排序列表：', random)
#
# add = lambda item: (item[1]+item[2], item[1], item[0])

a = [1, 2, 4, 5,6, 4,4]
print(a.count)
print(max(set(a), key=a.count))
a[a.count(max(a))]