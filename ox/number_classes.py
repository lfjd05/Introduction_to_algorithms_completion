"""
    数字分类 (20)
    给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：

    A1 = 能被5整除的数字中所有偶数的和；

    A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；

    A3 = 被5除后余2的数字的个数；

    A4 = 被5除后余3的数字的平均数，精确到小数点后1位；

    A5 = 被5除后余4的数字中最大数字。
"""


# 多行输入
def mut_in():
    a = [int(each) for each in input().split()]  # 输入的行数
    n = a.pop(0)
    return a


def model(a):
    even_sum = 0
    diff_sum = 0
    cnt = 0
    count = 0
    av_list = []
    max_list = []
    result = []
    for i in a:
        if i % 5 == 0 and i % 2 == 0:
            even_sum += i
        if i % 5 == 1:
            diff_sum += i*(-1)**cnt
            cnt += 1
        if i % 5 == 2:
            count += 1
        if i % 5 == 3:
            av_list.append(i)
        if i % 5 == 4:
            max_list.append(i)
    if len(av_list)==0:
        result0 = 0
    else:
        result0 = round(sum(av_list) / len(av_list), 1)
    if len(max_list)==0:
        result1=0
    else:
        result1=max(max_list)

    result.extend([even_sum, diff_sum, count, result0, result1])
    cnt = 0
    for i in result:
        if i == 0:
            print('{}'.format('N'), end='')
            if cnt<4:
                print(' ', end='')
        else:
            print('{}'.format(i), end='')
            if cnt<4:
                print(' ', end='')
        cnt +=1
    print('')


data= mut_in()
model(data)
