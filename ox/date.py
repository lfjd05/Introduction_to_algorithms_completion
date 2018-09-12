# 牛客网题目 福尔摩斯约会
import re

word_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
time_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N']
week_list = {1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 7:'SUN'}


# 输入函数
def mut_input():
    data = []
    n = 4
    while n > 0:
        data.extend([input()])
        n -= 1
    return data


def find_week(dat):
    '''
    a0 = re.findall('[A-Z]+', dat[0])
    b0 = re.findall('[A-Z]+', dat[1])
    # print(a0, b0)

    # 匹配到的元素单独放置
    a = []
    b = []
    for i in a0:
        a.extend(i)
    for i in b0:
        b.extend(i)
    '''
    # print('星期', week_list[word_dict[c[0]]])
    time = []
    # 这个循环用来找到第一个相同的大写字母，找到之后退出循环
    for i in dat[0]:
        if i in dat[1] and i in word_dict:
            time.append(i)
            break
    DAY, start, end = week_list[word_dict[time[0]]], dat[0].index(time[0]), dat[1].index(time[0])

    # 计算时
    # start, end = dat[0].index(c[0]), dat[1].index(c[0])
    for i in dat[0][start + 1:]:
        if i in dat[1][end + 1:]:
            if 'A' <= i <= 'N' or i in "0123456789":
                time.append(i)
                break
    cnt = str(time_list.index(time[1]))
    # print('时', cnt)

    # 计算分
    a0 = dat[2]
    b0 = dat[3]
    a = []
    b = []
    for i in a0:
        a.extend(i)
    for i in b0:
        b.extend(i)
    # 找到相同元素的索引
    minute = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            minute_cache = re.findall('[a-zA-Z]+', b[i])
            if len(minute_cache) > 0:
                minute = str(i)
                break
    # print('分', minute)

    # 输出
    if len(cnt)!=2:  # 如果不是两位数
        cnt = '0'+cnt
    if len(minute)!=2:
        minute = '0'+minute
    print('{} {}:{}'.format(DAY, cnt, minute))


data = mut_input()
# data = ['3485djDkxh4hhGE', '2984akDfkkkkggEdsb', 's&hgsfdk', 'd&Hyscvnm']
# data = ['3485djGkxh4hhG2',
# '2984akGfkkkkgg2dsb',
# 's&hgsfdk',
# 'd&hyscvnm']

# MON 13:04
# data = ['3485AjDkxh4hhGE',
# '2984AkDfkkkkggEdsb',
# 's&hgsfdk',
# 'd&HGscvnm']

find_week(data)
