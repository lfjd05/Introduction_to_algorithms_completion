# 剪刀锤子布
"""
    大家应该都会玩“锤子剪刀布”的游戏：
现给出两人的交锋记录，请统计双方的胜、平、负次数，
并且给出双方分别出什么手势的胜算最大。
"""
name_list = ['B', 'C', 'J']


def mut_input():
    n = int(input())
    data = []
    while n > 0:
        data.append([each for each in input().split()])
        n -= 1
    return n, data


# 多行输出
def mut_out(a):
    print(' '.join(str(i) for i in a))


def count(n, data):
    jia = [0, 0, 0]
    yi = [0, 0, 0]

    # 获胜最多的手势
    count1 = [0, 0, 0]
    count2 = [0, 0, 0]

    # 计算谁赢了
    for line in data:
        if (line[0] == 'C' and line[1] == 'J') or (line[0] == 'J' and line[1] == 'B') or (
                        line[0] == 'B' and line[1] == 'C'):  # 甲赢了
            if line[0] == 'C':
                count1[1] += 1
            elif line[0] == 'J':
                count1[2] += 1
            elif line[0] == 'B':
                count1[0] += 1
            jia[0] += 1
            yi[2] += 1
        elif (line[0] == 'C' and line[1] == 'B') or (line[0] == 'J' and line[1] == 'C') or (
                        line[0] == 'B' and line[1] == 'J'):  # 甲输了
            if line[1] == 'C':
                count2[1] += 1
            elif line[1] == 'J':
                count2[2] += 1
            elif line[1] == 'B':
                count2[0] += 1
            jia[2] += 1
            yi[0] += 1
        else:  # 平了
            jia[1] += 1
            yi[1] += 1
    # print(jia, yi)
    mut_out(jia)
    mut_out(yi)

    # print(count1, count2)
    maxjia = count1.index(max(count1))
    maxyi = count2.index(max(count2))
    print(name_list[maxjia], name_list[maxyi])

# n = 10
# data = [['C', 'J'],
#         ['J', 'B'],
#         ['C', 'B'],
#         ['B', 'B'],
#         ['B', 'C'],
#         ['C', 'C'],
#         ['C', 'B'],
#         ['J', 'B'],
#         ['B', 'C'],
#         ['J', 'J']]
n,data = mut_input()
count(n, data)
