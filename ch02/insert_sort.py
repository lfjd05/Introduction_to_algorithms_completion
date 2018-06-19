# 算法导论第一个算法插入排序
import time


def insertion_sort(d):
    # 已经有一张在左手索引从1开始
    for j in range(1, len(d)):
        key = d[j]   # 待插入的牌
        i = j-1    # [0,j-1]是左手拍，排好顺序的牌
        while i >= 0 and d[i] > key:
            # 当排好顺序的牌里面最大的那张比右手牌大的时候
            d[i+1] = d[i]  # 左边比右边大，左手的右移，保证从小到大
            i -= 1         # 下一张左手牌
        d[i+1] = key  # 右手元素放到左手，由于已经多减1所以要加1


if __name__ == '__main__':
    source = [5, 2, 4, 6, 1, 3, 52, 68, 52, 74, 2, 5, 85, 41, 22, 3, 12, 6, 9, 43, 22, 1, 0]
    start = time.time()
    insertion_sort(source)
    print('花费时间%.20f' % (time.time()-start))
    print(source)
