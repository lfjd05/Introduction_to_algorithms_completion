# python 的输入输出小程序，面试的时候省时间


# 多行输入
def mut_in():
    n = [int(each) for each in input().split()]  # 输入的行数
    a = []
    while n[0] > 0:
        a.append([int(each) for each in input().split()])
        n[0] -= 1
    return a


# 多行输出
def mut_out(a):
    for line in a:
        print(' '.join(str(i) for i in line))


if __name__ == '__main__':
    s = mut_in()
    mut_out(s)
