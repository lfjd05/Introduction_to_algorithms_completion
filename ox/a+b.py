# 多行输入
def mut_in():
    n = [int(each) for each in input().split()]  # 输入的行数
    a = []
    while n[0] > 0:
        a.append([int(each) for each in input().split()])
        n[0] -= 1
    return a


def compare(a):
    times = 1
    for line in a:
        A, B, C = line
        if A+B>C:
            print('Case #{}: true'.format(times))
        else:
            print('Case #{}: false'.format(times))
        times += 1

if __name__ == '__main__':
    data = mut_in()
    compare(data)
