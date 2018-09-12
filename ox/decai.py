# 牛客网德才论
"""
    现给出一批考生的德才分数，请根据司马光的理论给出录取排名。

    输入第1行给出3个正整数，分别为：N（<=105），即考生总数；L（>=60），为录取最低分数线，即德分和才分均不低于L的考生才有资格

被考虑录取；H（<100），为优先录取线——德分和才分均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；

才分不到但德分到线的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；
德才分均低于H，但是德分不低于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；
其他达到最低线L的考生也按总分排序，但排在第三类考生之后。


随后N行，每行给出一位考生的信息，包括：准考证号、德分、才分，其中准考证号为8位整数，德才分为区间[0, 100]内的整数。数字间以空格分隔。
"""


def st(ar):
    # ar.sort(key=lambda item: item[0])
    ar.sort(key=lambda item: (item[1]+item[2], item[1], item[0]), reverse=True)
    return ar


def mut_input():
    N, L, H = [int(each) for each in input().split()]

    data = []
    while N > 0:
        data.append([int(each) for each in input().split()])
        N -= 1
    return N, L, H, data


# 对考生进行分类
def divide_class(n, l, h, data):
    classes_data = []  # 两项都超过60的
    classes_1 = []
    classes_2 = []
    classes_3 = []
    classes_4 = []
    for student in data:
        # 添加总分
        student = [student[0], student[1], student[2], student[1]+student[2]]
        if student[1] >= l and student[2] >= l:
            classes_data.append(student)
            if student[1] >= h and student[2] >= h:  # 第一类
                classes_1.append(student)
            elif student[1] >= h > student[2]:   # 德到才不到
                classes_2.append(student)
            elif (student[1] < h and student[2]<h) and (student[1]>= student[2]):
                classes_3.append(student)  # 第三类
            else:
                classes_4.append(student)  # 第四类

    print(len(classes_data))  # 过线考生人数
    # print(len(classes_1), len(classes_2), len(classes_3), len(classes_4))

    # 排序
    classes_1 = st(classes_1)
    classes_2 = st(classes_2)
    classes_3 = st(classes_3)
    classes_4 = st(classes_4)

    # 删除总分.
    classes_1 = [i[0:3] for i in classes_1]
    classes_2 = [i[0:3] for i in classes_2]
    classes_3 = [i[0:3] for i in classes_3]
    classes_4 = [i[0:3] for i in classes_4]

    # print(classes_1, classes_2, classes_3, classes_4)
    mut_output(classes_1)
    mut_output(classes_2)
    mut_output(classes_3)
    mut_output(classes_4)


def mut_output(data):
    for a in data:
        print(' '.join(str(i) for i in a))

# N, L, H, Data = mut_input()

# 模拟数据
N = 14
L = 60
H = 80
Data = [[10000001, 64, 90],
        [10000002, 90, 60],
        [10000011, 85, 80],
        [10000003, 85, 80],
        [10000004, 80, 85],
        [10000005, 82, 77],
        [10000006, 83, 76],
        [10000007, 90, 78],
        [10000008, 75, 79],
        [10000009, 59, 90],
        [10000010, 88, 45],
        [10000012, 80, 100],
        [10000013, 90, 99],
        [10000014, 66, 60]]
# 以上对应的输出是
"""
12
10000013 90 99
10000012 80 100
10000003 85 80
10000011 85 80
10000004 80 85
10000007 90 78
10000006 83 76
10000005 82 77
10000002 90 60
10000014 66 60
10000008 75 79
10000001 64 90
"""
divide_class(N, L, H, Data)

